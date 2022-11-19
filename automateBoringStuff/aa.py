# SICK Dictionary Comprehension  
team1 = {'jones': 24, 'mug': 12, 'buck': 14}
team2 = {'jagg': 24, 'killa': 12, 'bucolic': 14}
newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
print(newTeam)

#! python3
""" Multithreaded XKCD Downloader - multithreading and comic downloads."""

import requests, os, bs4, threading

os.makedirs('xfcd', exist_ok=True)  # store comics in ./xfcd


def download(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print(f'Downloading page https://xkcd.com/{urlNumber}...')
        res = requests.get(f'https://xkcd.com/{urlNumber}')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print(f'Downloading image {comicUrl}')
            res = request.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start the Thread objects.            
downloadThreads = []  # A list of all the thread objects.
for i in range(0, 140, 10):  # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1  # There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadxkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')


#! python3
# regexer.py - Script to parse clipboard contents for emails & phone numbers.

import re
import pyperclip
# import xldr

# Give the location of the file
# loc = (C:\Users\maximilian.treadway\Desktop) #path of file
# To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)

# Regex for searching for phone number or email
phoneRegex = re.compile(r'''(
      [\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|
      \(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|
      \d{3}[-\.\s]??\d{4})
      )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
      [a-zA-Z0-9._%+-]+    # username
      @                    # @ symbol
      [a-zA-Z0-9.-]+       # domain name
      (\.[a-zA-Z]{2,4})
      )''', re.VERBOSE)


def main():
    text = str(pyperclip.paste())
    matches = []
    # for groups in phoneRegex.findall(text):
    #   phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    #   if groups[8] != '':
    #   phoneNum += ' x' + group[8]
    #   matches.append(phoneNum)
    for groups in phoneRegex.findall(text):
        matches.append(groups[0])
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    # Copy results to the clipboard
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard: ')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')

if __name__ == '__main__':
          main()

# ! python3
# PDF MetaData extractor - Violent Python (pg. 94-95)
import pyPdf
import optparse
from pyPdf import PdfFileReader


def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData for: ' + str(fileName))
    for metaItem in docInfo:
        print(f'[+] {metaItem} : {docInfo[metaItem]}')


def main():
    parser = optparse.OptionParser('usage %prog "+" -F <PDF File Name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
          main()

#! python3
# violentPython - SSH botnet py
import optparse, pxssh

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
         

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print(e)
            print('[-] Error Connecting')
         

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    def botnetCommand(command):
        for client in botNet:
            output = client.send_command(command)
            print(f'[*] Output from {client.host}')
            print(f'[+] Output from {output}\n')

    def addClient(host, user, password):
        client = Client(host, user, password)
        botNet.append(client)

    botNet = []
    addClient('10.10.10.110', 'root', 'toor')
    addClient('10.10.10.120', 'root', 'toor')
    addClient('10.10.10.130', 'root', 'toor')
    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')

# ! python3
# webscraper from quotes websitefrom bs4 import BeautifulSoup as bs
import requests

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = bs(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
tags = soup.find_all('div', class_='tags')

for i range(len(quotes)):
          print(quotes[i].text)
      print(authors[i].text)
      quoteTags = tags[i].find_all('a', class_='tags')
      for quoteTag in quoteTags:
                print(quoteTag.text)

# webscraper from ScrapingClub - single pagefrom bs4 import BeautifulSoup as bs
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = bs(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
          itemName = i.find('h4', class_='card-title').text.strip('\n')
      itemPrice = i.find('h5').text
      print(f'{count}) Price: {itemPrice}, Item Name: {itemName}')
      count += 1

#   webscraper from ScrapingClub - multipagefrom bs4 import BeautifulSoup as bs
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = bs(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
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
          newUrl = url + 1
      response = response.get(newUrl)
      soup = bs(response.text, 'lxml')
      items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
      for i in items:
                itemName = i.find('h4', class_='card-title').text.strip('\n')
            itemPrice = i.find('h5').text
            print(f'{count}) Price: {itemPrice}, Item Name: {itemName}')
            count += 1


# ! python3
# install chrome driver
# selenium easy basic webscraper/interface script
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')  # fix xpath
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('')  # add xpath
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('')  # add xpath
additionField2.send_keys('11')
getTotalButton = driver.find_element_by_xpath('')  # add xpath
getTotalButton.click()

# ! python3
# install chrome driver# drag and drop on web
# selenium easy basic webscraper/interface script
from selenium import webdriver
from selemenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath('')  # get x path
dest = driver.find_element_by_xpath('')  # add xpath
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()

#! python3
# explicit  wait with selenium to click things
from selenium import webdriver
from selemenium.webdriver.common.by import By
from selemenium.webdriver.support.ui import WebDriverWait
from selemenium.webdriver.support import expected_conditions as EC
url = 'https://www.google.com/earth'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()

#! python3
# api calls; parsing json dictionaries - drink bar codes to product info
import requests, json

baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '073366118238'}
response = requests.get(baseURL, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)

#! python3
# violent python - exif metadata img scanner/checkerimport urllib2
import optparse
from urlparse import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def findImages(url):
    print(f'[+] Finding images on {url}')
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def downloadImage(imgTag):
    try:
        print('[+] Downloading image...')
        imgSrc = imgTag['src']
        imgContent = urllib2.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e:
        return ''

def testForExif(imgFileName):
          try:
                    exifData = []

            imgFile = Image.open(imgFileName)
            info = imgFile._getexif()
            if info:
                      for (tag, value) in info.items():
                                decoded = TAGS.get(tag, tag)
                        exifData[decoded] = value
                  exifGPS = exifData['GPSInfo']
                  if exifGPS:
                            print(f'[*] {imgFileName} contains GPS MetaData')
      except:
            pass

def main():
                parser = optparse.OptionParser('usage%prog "+\"-u <target url>')

            parser.add_option('-u', dest='url', type='string', help='specify url address')
            (options, args) = parser.parse_args()
            url = options.url
            if url == None:
                      print(parser.usage)
                  exit(0)
            else:
                  imgTags = findImages(url)
                  for imgTags in imgTags:
                            imgFileName = downloadImage(imgTag)
                        testForExif(imgFileName)

      if __name__ == '__main__':
                main()

# ! python3# violent python - ftp scannerimport ftplib
def anonLogin(hostname):
          try:
                    ftp = ftplib.FTP(hostname)

            ftp.login('anonymous', 'me@your.com')
            print(f'\n[*] {hostname} FTP Anonymous Logon Succeeded.')
            ftp.quit()
            return True
      except Exception, e:
            print('\n[-] {hostname} FTP Anonymous Logon Failed.')
            return False
# change host to target of interest
host = '192.168.95.179'
anonLogin(host)

# ! python3
# webscraper for Southtowne apartment availabilityfrom bs4 import BeautifulSoup as bs
import requests, os
from datetime import date
from selenium import webdriver
from selemenium.webdriver.common.by import By
from selemenium.webdriver.support.ui import WebDriverWait
from selemenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client

e = date.today()
today = f'{e.month}/{e.day}/{e.year}'
url = f'https://bhmanagement.securecafe.com/onlineleasing/southtowne-apartments0/oleapplication.aspx?stepname=Floorplan&UnitID=18308074&FloorPlanID=3224069&MoveInDate={today}&myOlePropertyid=1125966'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 5)
oneBedButton = wait.until(EC.element_to_be_clickable((By.XPATH, '')))  # add xpath for 1bed button
oneBedButton.click()
updateButton = driver.find_element_by_xpath('')  # add xpath for update button
updateButton.click()
openApt = 0
try:
          openApt = driver.  # find results / apply now button
except Exception, e:
          print('No available Southtowne apartments at this time.')
if openApt != 0:
          accountSID = os.environ['twillioaccountsid']  # add twilio account sid
      authToken = os.environ['twillioauthtoekn']  # add twilio auth token
      client = Client('accountSID', 'authToken')
      message = client.messages.create(
from='TWILIONumber', to = '+16192460184', body = 'Urgent: SOUTHTOWNE 1 Bedroom Apartment now available.')  # get number from TWILIO
      print(message.sid)

# response = requests.get(url)
# soup = bs(response.text,'lxml')
# apt = soup.find_all('div', class_='availability-count')
# apt = soup.find_all('td colspan=\'2\'', class_='applyButton   waitlist btn btn-primary ')

# if 'apply' button presents on page instead of "join our waitlist" button, then text my number - use twilio?# or - just submit application

# maybe I don't need to even click anything because the url doesn't change.
# maybe the content is there all alogn and just isn't visible.
# maybe i can just search for apply now/apply button on page and try to click and if successful, email my self...