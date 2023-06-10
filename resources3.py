from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/search?gs_ssp=eJzj4tTP1TdILiyxNDBg9OJJyc9LzElRKCkqzS0AAGBuCBE&q=donald+trump&oq=donald+&gs_lcrp=EgZjaHJvbWUqCggBEC4YsQMYgAQyDQgAEAAY4wIYsQMYgAQyCggBEC4YsQMYgAQyBggCEEUYOTIKCAMQLhixAxiABDIHCAQQLhiABDINCAUQABiDARixAxiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQLhiABNIBCDIzODJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8')

stuff = driver.find_element(By.CLASS_NAME, 'LC201b MBeuO DKV0')
print(stuff)
# TzHB6b
