#! python3
# webscraper from ScrapingClub - multipage
from bs4 import BeautifulSoup as bs
import requests, lxml
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = bs(response.text, 'lxml')
items = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print(f'{count}) Price: {itemPrice}, Item Name: {itemName}')
        count += 1
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
        pageNum = int(link.text) if link.text.isdigit() else None
        if pageNum != None:
                x = link.get('href')
                urls.append(x)
count = 1
for i in urls:
        newUrl = url + i
        response = requests.get(newUrl)
        soup = bs(response.text, 'lxml')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in items:
                itemName = i.find('h4', class_='card-title').text.strip('\n')
                itemPrice = i.find('h5').text
                print(f'{count}) Price: {itemPrice}, Item Name: {itemName}')
                count += 1