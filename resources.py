# import requests
# from bs4 import BeautifulSoup
# import csv
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36')
# browser = webdriver.Chrome(options=chrome_options) #ChromeDriverManager().install()
#
# url = 'https://www.google.com/search?q=hello+world&num=30&gl=UK'
#
# browser.get(url)
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# items = soup.find_all('div', {'class': 'GyAeWb'})
# print(items)
#
# print('counts : ' + str(len(items)))
# for each in items:
#     try:
#         print(each.find('div', {'class': 'yuRUbf'}).find('h3').text)
#         print(each.find('div', {'class': 'Z26q7c'}).find('span').text)
#         print('-------------------------------')
#     except:
#         pass
#
#
#

import requests
from bs4 import BeautifulSoup
search="2%2B2"
link="https://www.google.com/search?q="+search
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
source=requests.get(link,headers=headers).text
soup=BeautifulSoup(source,"html.parser")
answer=soup.find('span',id="cwos")
print(answer.text)
