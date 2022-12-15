from amazon_scraper import scrape_amazon
from okidoki import okidoki
from soov_scraper import scrape_soov
from gui import Gui
import xlsxwriter


def filter_prices(listings: list[list], price_min=None, price_max=None) -> list[list]:
    if not price_max and not price_min:
        return listings
    price_max = 0 if not price_max else price_max
    price_min = 0 if not price_min else price_min
    for scrape in listings:
        if scrape[1].translate({ord(x): None for x in '£$€.,'}).isnumeric() and\
                float(price_max) < float(scrape[1].translate({ord(x): None for x in '£$€,'})) < float(price_min):
            listings.remove(scrape)
    return listings


def add_worksheet(xlsx_file: xlsxwriter.workbook, listings_data: list[list], worksheet_name: str) -> None:
    worksheet = xlsx_file.add_worksheet(worksheet_name)
    worksheet.write(0, 0, "Name")
    worksheet.write(0, 1, "Price")
    worksheet.write(0, 2, "Image")
    worksheet.write(0, 3, "Link")

    if listings_data:
        for i, scraping in enumerate(listings_data):
            for j in range(4):
                worksheet.write(i + 1, j, scraping[j])


if __name__ == '__main__':
    input_gui = Gui()
    while True:
        if input_gui.returns is not None:
            product_name, max_price, min_price = input_gui.returns
            break

    amazon_listings_us = filter_prices(scrape_amazon(product_name, "com"), min_price, max_price)
    amazon_listings_uk = filter_prices(scrape_amazon(product_name, "co.uk"), min_price, max_price)
    amazon_listings_german = filter_prices(scrape_amazon(product_name, "de"), min_price, max_price)
    okidoki_listings = filter_prices(okidoki(product_name), min_price, max_price)
    soov_listings = filter_prices(scrape_soov(product_name), min_price, max_price)

    with xlsxwriter.Workbook("scraping_outputs.xlsx") as file:
        add_worksheet(file, amazon_listings_us, "amazon.com")
        add_worksheet(file, amazon_listings_uk, "amazon.uk")
        add_worksheet(file, amazon_listings_german, "amazon.de")
        add_worksheet(file,  okidoki_listings, "okidoki.ee")
        add_worksheet(file, soov_listings, "soov.ee")
