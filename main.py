from amazon_scraper import scrape_amazon
from okidoki import okidoki
from soov_scraper import scrape_soov
from gui import Gui


def remove_incorrectly_priced_scrapes(scrapes: list[list], min_price=None, max_price=None) -> list[list]:
    if not max_price and not min_price:
        return scrapes
    for scrape in scrapes:
        if max_price < [1] < min_price:
            scrapes.remove(scrape)


if __name__ == '__main__':
    input_gui = Gui()
    while True:
        if input_gui.returns is not None:
            product_name, max_price, min_price = input_gui.returns
            break

    amazon_scrapes_us = remove_incorrectly_priced_scrapes(scrape_amazon(product_name, "com"))
    print(amazon_scrapes_us)
    amazon_scrapes_uk = remove_incorrectly_priced_scrapes(scrape_amazon(product_name, "co.uk"))
    amazon_scrapes_german = remove_incorrectly_priced_scrapes(scrape_amazon(product_name, "de"))
    okidoki_scrapes = remove_incorrectly_priced_scrapes(okidoki(product_name))
    soov_scrapes = remove_incorrectly_priced_scrapes(scrape_soov(product_name))

    with open("test.txt", "w", encoding="utf-8") as file:
        for listing in amazon_scrapes_german:
            file.write(f"{listing}\n")
        for listing in amazon_scrapes_uk:
            file.write(f"{listing}\n")
        for listing in amazon_scrapes_us:
            file.write(f"{listing}\n")
