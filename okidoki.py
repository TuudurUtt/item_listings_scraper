import requests
from bs4 import BeautifulSoup
from math import ceil

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}

def okidoki_l(leht, nimi):
        okidoki_link = ("https://www.okidoki.ee/buy/all/?p={}&query={}".format(leht, nimi))
        # okidoki_link = ("https://www.okidoki.ee/buy/all/?query={}&price_from_value=0&price_to_value=0&p={}".format(nimi, leht))
        return okidoki_link

def okidoki(nimi):
    nimi.replace(" ", "+")
    products = []
    big_list = []
    price = []
    title = []
    link = []
    img = []
    leht = 0

    allikas = requests.get(okidoki_l(leht, nimi), headers = headers)
    r = BeautifulSoup(allikas.content, "lxml")
    try:
        kuulutuste_koguarv = (r.find(attrs={"class":"pager__current--total"})).text.strip()
    except:
        return []

    lehtede_arv = ceil(int(kuulutuste_koguarv) / 50)
  
    big_list.append(r.find_all(attrs={"class":"classifieds__item"}))

    if lehtede_arv > 1:
        leht = 1
        for i in range(lehtede_arv - 1):
            leht += 1

            allikas = requests.get(okidoki_l(leht, nimi), headers = headers)
            r = BeautifulSoup(allikas.content, "lxml")
            big_list.append(r.find_all(attrs={"class":"classifieds__item"}))

    for i in range(len(big_list)):
        for j in range(len(big_list[i])):
            title = (big_list[i][j].find(attrs={"class":"horiz-offer-card__title-link"}).get_text())
            
            try:
                price = (big_list[i][j].find(attrs={"class":"horiz-offer-card__price-value"}).get_text().strip(" \n€").replace(" ", ""))
            except:
                price = ""

            link = ("https://www.okidoki.ee" + big_list[i][j].find(attrs={"class":"horiz-offer-card__title-link"}).get('href'))

            imgtemp = big_list[i][j].find("img").get("src")
            if imgtemp.startswith("//img") or imgtemp == "/assets/svg/offers/no-image.svg":
                img = (imgtemp)

            products.append([title, price, img, link])

    
    return products