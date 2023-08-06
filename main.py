import requests
# from pprint import pprint
from bs4 import BeautifulSoup
from time import sleep
from header import headers


def download(url):
    resp = requests.get(url, stream=True)
    file = open('Statics/' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024**2):
        file.write(value)
    file.close()

def get_url():
    for count in range(1,7):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all('div', class_='w-full rounded border')

        for item in data:
            url_block = 'https://scrapingclub.com' + item.find('a').get('href')
            yield url_block


for items_url in get_url():
    card_response = requests.get(items_url, headers=headers)

    item_soup = BeautifulSoup(card_response.text, "lxml")
    item_card = item_soup.find('div', class_='my-8 w-full rounded border')

    item_title = item_card.find("h3", class_="card-title").text
    item_price = item_card.find("h4", class_="my-4 card-price").text
    item_description = item_card.find('p', class_="card-description").text
    item_img_url = "https://scrapingclub.com" + item_card.find('img').get('src')

    # download(item_img_url)

    print(item_title + '\n' + item_price + '\n' + '\n' + item_description + '\n' + item_img_url + '\n')
    sleep(1)
