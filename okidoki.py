from turtle import end_fill
from unicodedata import numeric
import requests
from bs4 import BeautifulSoup
from math import ceil

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 Safari/537.36"
}

#[[nimi, hind, link, img], ]

leht = 0
min_hind = 0
max_hind = 1000
nimi = "bmw veljed"

def okidoki_l(nimi, min_hind, max_hind, leht):
    okidoki_link = ("https://www.okidoki.ee/buy/all/?query={}&price_from_value={}&price_to_value={}&p={}".format(nimi, min_hind, max_hind, leht))
    # okidoki_link = ("https://www.okidoki.ee/buy/all/?query={}&price_from_value={}&price_to_value={}&p={}".format(nimi, min_hind, max_hind, leht))
    return okidoki_link
# print(okidoki_l(min_hind, leht, max_hind, nimi))
def okidoki(min_hind, max_hind, nimi):
    price = []
    title = []
    link = []
    img = []
    imgf = []
    leht = 0
    allikas = requests.get(okidoki_l(nimi, min_hind, max_hind, leht), headers = headers)
    r = BeautifulSoup(allikas.content, "lxml")

    k_koguarv = (r.find(attrs={"class":"pager__current--total"})).text.strip()
    print(k_koguarv)
    lehtede_arv = ceil(int(k_koguarv) / 50)
    print(lehtede_arv)
    with open("html2.txt", "w", encoding="utf-8") as f:
        f.write(str(r))

    for i in range(lehtede_arv):
        leht += 1
        print(leht)
        print(okidoki_l(nimi, min_hind, max_hind, leht))
        allikas = requests.get(okidoki_l(nimi, min_hind, max_hind, leht), headers = headers)
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

    x = 0
    for i in range(len(imgf)):
        imgtemp = imgf[i]
        imgtemp = imgtemp.get("src")
        if imgtemp.startswith("//img") or imgtemp == "/assets/svg/offers/no-image.svg":
            img.append(imgtemp)

    print((title))    
    print((price))
    print(link)
    print(img)
    print(len(title))    
    print(len(price))
    print(len(link))
    print(len(img))
    
    # s = r.find_all("div", {"class":"classifieds classifieds--big-list"})
    # with open("html.txt", "w", encoding="utf-8") as fail:
    #     print(s, file=fail)
    #     for i in s:
    #         fail.write(i)
    #     fail.write(r)
    # r = BeautifulSoup(allikas)
    return [title, price, link, img]
x = okidoki(min_hind, max_hind, nimi)
print("aaaaaaaaaaaaaaa")
# with open("price.txt", "w", encoding="utf-8") as f:
#     f.write(str(x[0]))

# with open("title.txt", "w", encoding="utf-8") as f:
#     f.write(str(x[1]))




# pricef = open("price.txt", "r", encoding='utf-8')
# titlef = open("title.txt", "r", encoding="utf-8")

# title = titlef.readlines()
# price = pricef.readlines()
# for i in titlef:
#     title.append(i)
# for i in pricef:
#     price.append(i)

# print(len(title))
# print(len(price))