import requests
from pprint import pprint
from bs4 import BeautifulSoup
from time import sleep
from header import headers


num = 1
lst = []

for count in range(1,7):
    sleep(3)

    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all('div', class_='w-full rounded border')

    for item in data:
        name = item.find('h4').text.replace('\n', '')
        price = item.find('h5').text
        url_img = "https://scrapingclub.com" + item.find('img', class_="card-img-top img-fluid").get("src")
        lst.append({f'Position {num}': {"name": name, "price": price, "url_img": url_img}})
        num += 1

pprint(lst, indent=2)