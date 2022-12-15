import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}


def scrape_listing_links(searched_item: str, iteration=1, product_links=None) -> set[str]:
    if product_links is None:
        product_links = []
    r = requests.get(f"https://soov.ee/keyword-{searched_item}/tuup-müüa/{iteration}/listings.html", headers=headers)
    html = BeautifulSoup(r.content, "lxml")
    product_links += {listing.find("a").get("href") for listing in html.find_all("h5", class_="add-title")}
    if 0 < len(html.find_all("a", class_="pagination-btn")) < 2:
        return scrape_listing_links(searched_item, iteration=iteration + 1, product_links=product_links)
    else:
        return product_links


def scrape_soov(searched_item: str) -> list[list[str]]:
    links = scrape_listing_links(searched_item)
    output_list = []
    for link in links:
        r = requests.get(link, headers=headers)
        html = BeautifulSoup(r.content, "lxml")

        if not html or not html.find("span", id="productTitle"):
            continue
        title = html.find("span", id="lid").get_text()

        if not html.find("span", class_="a-offscreen"):
            product_price = "Varies"
        else:
            product_price = html.find("span", class_="media-heading").get_text().strip()

        if not html.find("div", class_="product-image relative"):
            image_link = " "
        else:
            image_link = html.find("div", class_="product-image relative").find("img").get("src")

        output_list.append([title, product_price, image_link, link])
    return output_list
