#! python3
# southtowneSearch.py
# webscraper for Southtowne apartment availability - use twilio to text myself if 1br comes available
import os
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client

openApt = 0
# function to access the southtowne apartment availability website, wait for loading of page, then select 1BR and update page to find availability.
def searchSouthTowneApts():
    e = date.today()
    today = f'{e.month}/{e.day}/{e.year}'
    url = f'https://bhmanagement.securecafe.com/onlineleasing/southtowne-apartments0/oleapplication.aspx?stepname=Floorplan&UnitID=18308074&FloorPlanID=3224069&MoveInDate={today}&myOlePropertyid=1125966'
    driver = webdriver.Chrome('/Users/max/Desktop/chromedriver')
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    oneBedButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="1Bed"]')))
    oneBedButton.click()
    updateButton = driver.find_element_by_xpath('//*[@id="btnUpdateFilter"]')
    updateButton.click()
# part of function that searches for available apartment 'apply now' links on Southtowne page
    global openApt
    # IF YOU MOVE CHROMEDRIVER OFF DESKTOP, YOU WILL NEED TO UPDATE PATH
    driver = webdriver.Chrome('/Users/max/Desktop/chromedriver')
    try:
        openAptA1 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[25]/text()')
        openAptA1.click()
        openApt += 1
        print('1BR/A2 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A1 apartments at this time.')
    try:
        openAptA2 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[24]/text()')
        openAptA2.click()
        openApt += 1
        print('1BR/A2 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A2 apartments at this time.')
    try:
        openAptA3 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[26]/text()')
        openAptA3.click()
        openApt += 1
        print('1BR/A3 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A3 apartments at this time.')
    try:
        openAptA4 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[27]/text()')
        openAptA4.click()
        openApt += 1
        print('1BR/A4 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A4 apartments at this time.')
    try:
        openAptA5 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[28]/text()')
        openAptA5.click()
        openApt += 1
        print('1BR/A5 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A5 apartments at this time.')
    try:
        openAptA6 = driver.find_element_by_xpath('//*[@id="rentcafe_onlineleasing"]/script[29]/text()')
        openAptA6.click()
        openApt += 1
        print('1BR/A6 Apartment found!')
    except Exception as e:
        print('No available Southtowne 1BR/A6 apartments at this time.')

# Use twilio to text myself if openApt variable is incremented as a result of available 1BR apartments at southtowne
def textMyself():
    if openApt >= 1:
        try:
            accountSID = os.environ['ACcf4454de4cac56dfb922b8e228491a8b']
            authToken = os.environ['7eb8ea1adfd10a9b7936dfc4cd751bce']
            client = Client('accountSID', 'authToken')
            message = client.messages.create(
                from_= '+13235082224',
                to = '+16192460184',
                body = 'Urgent: SOUTHTOWNE 1 Bedroom Apartment now available.')
            print(message.sid)
        except Exception as e:
            print('Text failed to send. ' + e)

if __name__ == '__main__':
    searchSouthTowneApts()
    if openApt >= 1:
        print('Go time.')
        #textMyself()