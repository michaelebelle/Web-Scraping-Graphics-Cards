from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)
# print(page_soup.p)

# grabs each graphic card
containers = page_soup.findAll("div", {"class": "item-container"})
containersTitles = page_soup.findAll("a", {"class": "item-title"})

container = containers[0]

filename = "products.csv"
f = open(filename, "w")

headers = "name, shipping, prices\n"
f.write(headers)

for container in containers:
    containerTitle = container.findAll("a", {"class": "item-title"})
    containerShipping = container.findAll("li",{"class": "price-ship"})
    containerPrice = container.findAll("li", {"class": "price-current"})
    shipping = "NA"

    if len(containerTitle) != 0:
        title = containerTitle[0].text


    if len(containerShipping) != 0:
        shipping = containerShipping[0].text

    if len(containerPrice) != 0:
        prices = containerPrice[0].text

    print(title)
    print(shipping)
    print(prices)
    f.write(title.replace("," ,"|") + "," + shipping.replace("," ,"|") + "," + prices.replace("," , "") + "\n")



