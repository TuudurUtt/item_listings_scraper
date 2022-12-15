import requests
from bs4 import BeautifulSoup
from math import ceil


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}


def okidoki_link(leht, nimi):
    link = ("https://www.okidoki.ee/buy/all/?p={}&query={}".format(leht, nimi))
    return link


def okidoki(product_name):
    product_name.replace(" ", "+")
    output_list = []

    r = requests.get(okidoki_link(0, product_name), headers=headers)
    html = BeautifulSoup(r.content, "lxml")
    try:
        lehtede_arv = ceil(int((html.find(class_="pager__current--total")).text.strip()) / 50)
    except AttributeError:
        return []

    product_htmls = html.find_all(class_="classifieds__item")
    if lehtede_arv > 1:
        for i in range(lehtede_arv - 1):
            r = requests.get(okidoki_link(i + 1, product_name), headers=headers)
            html = BeautifulSoup(r.content, "lxml")
            product_htmls.extend(html.find_all(class_="classifieds__item"))

    for i in range(len(product_htmls)):
        if not product_htmls[i].find(class_="horiz-offer-card__title-link"):
            continue
        title = product_htmls[i].find(class_="horiz-offer-card__title-link").get_text()

        if not product_htmls[i].find(class_="horiz-offer-card__price-value"):
            product_price = "Varies"
        else:
            product_price = product_htmls[i].find(class_="horiz-offer-card__price-value")\
                .get_text().strip(" \n€").replace(" ", "")

        if not product_htmls[i].find(class_="horiz-offer-card__title-link"):
            continue
        link = ("https://www.okidoki.ee" + product_htmls[i].find(class_="horiz-offer-card__title-link").get('href'))

        if not product_htmls[i].find("img"):
            image_link = " "
        else:
            imgtemp = product_htmls[i].find("img", ).get("src")
            image_link = "https://www.okidoki.ee" + imgtemp if imgtemp.startswith("//img") or\
                imgtemp == "/assets/svg/offers/no-image.svg" else " "

        output_list.append([title, product_price, image_link, link])
    return output_list
