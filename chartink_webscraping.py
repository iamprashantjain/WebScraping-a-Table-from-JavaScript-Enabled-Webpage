from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests



def telegram_bot_sendtext(bot_message):
    bot_token = '5319174814:AAEh2Qs1Iny-SDU5ADl89yo__Yb_DaN-j_U'
    bot_chatID = '936570830'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
        bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message
    response = requests.get(send_text)
    return response.json()



#setting up chrome driver
s = Service(r"C:\Users\User\Desktop\webscraping_project\chromedriver.exe")
driver = webdriver.Chrome(service=s)


#open website
driver.get("https://chartink.com/screener/monthly-sip-20010")
time.sleep(5)


#click on scans to go to login page
driver.find_element_by_xpath(""" /html/body/div[1]/div/div[2]/div/div[5]/span/a[1] """).click()
time.sleep(5)


#enter login details
username = driver.find_element_by_xpath(""" /html/body/div[2]/div/div/div/div[2]/form/div[1]/div/input """)
username.send_keys("prashantthemusicvirus@gmail.com")
time.sleep(5)

password = driver.find_element_by_xpath(""" /html/body/div[2]/div/div/div/div[2]/form/div[2]/div/input """)
password.send_keys("Aspire@123")
time.sleep(5)
driver.find_element_by_xpath(""" /html/body/div[2]/div/div/div/div[2]/form/div[4]/div/button """).click()
time.sleep(5)


#enter_strategy
driver.find_element_by_xpath(""" /html/body/div[2]/div/div[2]/div[4]/div/table/tbody/tr[6]/td[1]/a/b """).click()
time.sleep(5)


#find scanner table
soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all('table')

#create df 
df = pd.read_html(str(tables))[1]
symbols = df['Symbol']


# Convert the symbols to a string
symbols_str = ', '.join(symbols)

#sent to telegram
telegram_bot_sendtext(symbols_str)