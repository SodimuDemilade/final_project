import pandas as pd
import re
from tqdm import tqdm
from ecommercetools import seo
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
#
# # query_list = ['denmark, inflation', 'denmark, immigration', 'denmark, global warming', 'toronto, inflation',
# #               'toronto, immigration', 'toronto global warming', 'washington, inflation',
# #               'washington, immigration', 'washington, global warming', 'madrid, inflation', 'madrid immigration',
# #               'madrid, global warming', 'paris, inflation', 'paris, immigration', 'paris, global warming',
# #               'sweden, inflation', 'sweden, immigration', 'sweden, global warming']
#
# query_list = ['machine learning', 'Distributed systems', 'Computer Security', 'artificial intelligence',
#               'recommender systems', 'global warming sweden', 'intelligent agents', 'percepts sequence']
# # query_list = ['artificial intelligence pdf']
#
# targets = []
# for query in tqdm(query_list):
#     pages_num = 3
#     # conditions = ['wikipedia', 'twitter', 'linkedin', 'Facebook', 'news']
#     conditions = ['youtube', 'pdf', 'wikipedia']
#     # conditions = ['']
#     #use [''] to get all google search results
#     try:
#         res = seo.get_serps(query, pages=pages_num)
#     except:
#         continue
#     for c in conditions:
#         temp1 = res[res['link'].str.contains(c, case=False)]['title'].to_list()
#         temp2 = res[res['link'].str.contains(c, case=False)]['link'].to_list()
#         if len(temp1) == 0:
#             y = ''
#         else:
#             y = temp1[0]
#         if len(temp2) == 0:
#             z = ''
#         else:
#             z = temp2[0]
#         targets.append([y, z, c, query])
#         time.sleep(25)
#     time.sleep(20)
#
# targets = pd.DataFrame(targets, columns=['title', 'link', 'link category', 'query keyword used'])
# print(targets)


from googlesearch import search

query = "artificial intelligence pdf"

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)



# options = Options()
# # options.add_argument("--headless")
# options.add_experimental_option('prefs', {
#     "download.default_directory": "C:\\Users\\Demilade Sodimu\\Desktop",
#     "download.prompt_for_download": False,  # To auto download the file
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
# })
# chrome_driver_path = "C:\Development\chromedriver.exe"
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)
#
# # links will be put here for download
# driver.get("https://www.dcpehvpm.org/E-Content/BCA/BCA-III/artificial_intelligence_tutorial.pdf")
# time.sleep(1500)

# have to figure out how to rank videos