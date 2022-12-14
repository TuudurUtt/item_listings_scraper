import requests
from bs4 import BeautifulSoup
from math import ceil

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}

leht = 0
min_hind = 0
max_hind = 0
nimi = "zenit"

# def okidoki_l(nimi, min_hind, max_hind, leht):
#     okidoki_link = ("https://www.okidoki.ee/buy/all/?query={}&price_from_value={}&price_to_value={}&p={}".format(nimi, min_hind, max_hind, leht))
#     return okidoki_link

def okidoki_l(leht, nimi):
    okidoki_link = ("https://www.okidoki.ee/buy/all/?p={}&query={}".format(leht, nimi))
    return okidoki_link

def okidoki(min_hind, max_hind, nimi):
    price = []
    title = []
    link = []
    img = []
    imgf = []
    leht = 0
    allikas = requests.get(okidoki_l(leht, nimi), headers = headers)
    r = BeautifulSoup(allikas.content, "lxml")

    kuulutuste_koguarv = (r.find(attrs={"class":"pager__current--total"})).text.strip()
    print(kuulutuste_koguarv)
    lehtede_arv = ceil(int(kuulutuste_koguarv) / 50)
    print(lehtede_arv)

    #test
    with open("html2.txt", "w", encoding="utf-8") as f:
        f.write(str(r))


    for i in range(lehtede_arv):
        leht += 1
        print(leht)
        print(okidoki_l(leht, nimi))
        allikas = requests.get(okidoki_l(leht, nimi), headers = headers)
        print(allikas)
        r = BeautifulSoup(allikas.content, "lxml")
        # .find(attrs={"class":"classifieds classifieds--big-list"})
        title.extend(r.find_all(attrs={"class":"horiz-offer-card__title-link"}))
        price.extend(r.find_all(attrs={"class":"horiz-offer-card__price-value"}))
        imgf.extend(r.find_all("img"))
    
    for i in range(len(price)):
        pricetemp = price[i]
        price[i] = pricetemp.get_text().strip(" \n€").replace(" ", "")

    for i in range(len(title)):
        titletemp = title[i]
        title[i] = titletemp.get_text()
        link.append("https://www.okidoki.ee" + titletemp.get('href'))


    for i in range(len(imgf)):
        imgtemp = imgf[i]
        imgtemp = imgtemp.get("src")
        if imgtemp.startswith("//img") or imgtemp == "/assets/svg/offers/no-image.svg":
            img.append(imgtemp)

    
    return [title, price, link, img]


x = okidoki(min_hind, max_hind, nimi)
print(len(x[0]), len(x[1]), len(x[2]), len(x[3]))