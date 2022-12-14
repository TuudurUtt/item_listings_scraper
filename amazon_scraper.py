import requests
from bs4 import BeautifulSoup
from googletrans import Translator


translator = Translator()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}


def scrape_listing_links(searched_item: str, suffix: str,
                         iteration=1, product_links=None, nr_of_pages=None) -> set[str]:
    if product_links is None:
        product_links = []
    r = requests.get(f"https://www.amazon.{suffix}/s?k={searched_item}&page={iteration}", headers=headers)
    html = BeautifulSoup(r.content, "lxml")
    product_links += {f"https://www.amazon.{suffix}" + listing.get("href") for listing in
                      html.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text"
                                                " s-link-style a-text-normal")
                      if not listing.get("href").startswith("/sspa/")}
    if nr_of_pages is None:
        try:
            nr_of_pages = int(html.find("span", class_="s-pagination-item s-pagination-disabled").text)
        except AttributeError:
            nr_of_pages = 1
    if nr_of_pages != iteration:
        return scrape_listing_links(searched_item, suffix,
                                    iteration=iteration + 1, product_links=product_links, nr_of_pages=nr_of_pages)
    else:
        return product_links


def scrape_amazon(searched_item: str, suffix: str) -> list[list[str]]:
    links = scrape_listing_links(searched_item, suffix)
    output_list = []
    for link in links:
        r = requests.get(link, headers=headers)
        html = BeautifulSoup(r.content, "lxml")
        title = translator.translate(html.find("span", id="productTitle").get_text().strip()).text
        product_price = html.find("span", class_="a-offscreen").get_text().strip().replace(",", ".")
        image_link = html.find("div", id="imgTagWrapperId").find("img").get("src")
        if not product_price[:-1].replace(".", "").isnumeric():
            product_price = "Varies"
        output_list.append([title, product_price, image_link, link])
    return output_list
