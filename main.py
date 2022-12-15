from amazon_scraper import scrape_amazon
from okidoki import okidoki
from soov_scraper import scrape_soov
from gui import Gui
import xlsxwriter


def filter_prices(scrapes: list[list], price_min=None, price_max=None) -> list[list]:
    if not price_max and not price_min:
        return scrapes
    for scrape in scrapes:
        if scrape[1].replace(".£$€", "").isnumeric() and\
                float(price_max) < float(scrape[1].replace(".£$€", "")) < float(price_min):
            scrapes.remove(scrape)
    return scrapes


def write_worksheet_contents(worksheet: xlsxwriter.workbook.Worksheet, scrapings_data: list[list]) -> None:
    worksheet.write(0, 0, "Name")
    worksheet.write(0, 1, "Price")
    worksheet.write(0, 2, "Image")
    worksheet.write(0, 3, "Link")

    if scrapings_data:
        for i, scraping in enumerate(scrapings_data):
            worksheet.write(i + 1, 0, scraping[0])
            worksheet.write(i + 1, 1, scraping[1])
            worksheet.write(i + 1, 2, scraping[2])
            worksheet.write(i + 1, 3, scraping[3])


if __name__ == '__main__':
    input_gui = Gui()
    while True:
        if input_gui.returns is not None:
            product_name, max_price, min_price = input_gui.returns
            break

    amazon_scrapes_us = filter_prices(scrape_amazon(product_name, "com"), price_min=min_price, price_max=max_price)
    print(amazon_scrapes_us)
    amazon_scrapes_uk = filter_prices(scrape_amazon(product_name, "co.uk"), price_min=min_price, price_max=max_price)
    print(amazon_scrapes_uk)
    amazon_scrapes_german = filter_prices(scrape_amazon(product_name, "de"), price_min=min_price, price_max=max_price)
    print(amazon_scrapes_german)
    okidoki_scrapes = filter_prices(okidoki(product_name), price_min=min_price, price_max=max_price)
    print(okidoki_scrapes)
    soov_scrapes = filter_prices(scrape_soov(product_name), price_min=min_price, price_max=max_price)
    print(soov_scrapes)

    with xlsxwriter.Workbook("scraping_outputs.xlsx") as file:
        amazon_scrapes_us_worksheet = file.add_worksheet("amazon.com")
        amazon_scrapes_uk_worksheet = file.add_worksheet("amazon.uk")
        amazon_scrapes_german_worksheet = file.add_worksheet("amazon.de")
        okidoki_scrapes_worksheet = file.add_worksheet("okidoki.ee")
        soov_scrapes_worksheet = file.add_worksheet("soov.ee")

        write_worksheet_contents(amazon_scrapes_us_worksheet, amazon_scrapes_us)
        write_worksheet_contents(amazon_scrapes_uk_worksheet, amazon_scrapes_uk)
        write_worksheet_contents(amazon_scrapes_german_worksheet, amazon_scrapes_german)
        write_worksheet_contents(okidoki_scrapes_worksheet, okidoki_scrapes)
        write_worksheet_contents(soov_scrapes_worksheet, soov_scrapes)
