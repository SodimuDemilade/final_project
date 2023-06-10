from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

options = Options()
# options.add_argument("--headless")
options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\Demilade Sodimu\\Desktop",
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


# DETAILS
# USERNAME = '19cg026486'
# PASSWORD = 'demi1234'
file1 = open("myfile.txt", "r")
fhand = file1.readlines()
USERNAME = (fhand[0]).rstrip()
PASSWORD = (fhand[1]).rstrip()


# MOODLE
driver.get("https://moodle.cu.edu.ng/")


# LOG IN
login = driver.find_element(By.LINK_TEXT, 'Log in')
login.click()
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
signin = driver.find_element(By.ID, 'kc-login')
signin.click()


# GETTING ALL THE COURSES
time.sleep(4)
courses_info = driver.find_elements(By.CLASS_NAME, 'multiline')
courses = [course.text for course in courses_info]

dashboard = 'https://moodle.cu.edu.ng/my/'


for _ in range(len(courses)):
    if _ != 0:
        driver.implicitly_wait(100)
        course = driver.find_element(By.PARTIAL_LINK_TEXT, courses[_][0:9])
        course.click()
        try:
            links = driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")
            for i in range(len(links)):
                (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).click()
        except:
            continue
        # mylinks = []
        # for link in links:
        #     mylinks.append(link.text)
        # print(mylinks)
        # for link in mylinks:
        #     try:
        #         text = (link.split("\n"))[0]
        #         access = (link.split("\n"))[1]
        #         if access == "File":
        #             print(text)
        #     except:
        #         continue
        driver.get(dashboard)