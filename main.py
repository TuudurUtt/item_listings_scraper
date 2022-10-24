from amazon_scraper import scrape_amazon


if __name__ == '__main__':
    toode = input("Sisestage otsitav toode: ")
    amazon_scrapes_us = scrape_amazon(toode, "com")
    amazon_scrapes_uk = scrape_amazon(toode, "co.uk")
    amazon_scrapes_german = scrape_amazon(toode, "de")
    with open("test.txt", "w", encoding="utf-8") as file:
        for listing in amazon_scrapes_german:
            file.write(f"{listing}\n")
        for listing in amazon_scrapes_uk:
            file.write(f"{listing}\n")
        for listing in amazon_scrapes_us:
            file.write(f"{listing}\n")
