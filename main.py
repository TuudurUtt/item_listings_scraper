import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}


def scrape_amazon(searched_item, suffix:str) -> list[str]:
    base_url = f"https://www.amazon.{suffix}/s?k={searched_item}"
    r = requests.get(base_url, headers=headers)
    html = BeautifulSoup(r.content, "lxml")


if __name__ == '__main__':
    toode = input("Sisestage otsitav toode: ")
    scrape_amazon(toode, "de")
