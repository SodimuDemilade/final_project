from moodle_project.resources2 import resources_popup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os


def crawl_moodle():
    path = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes"
    if not os.path.exists(path):
        os.makedirs("C:\\Users\\Demilade Sodimu\\Documents\\my_notes")
    options = Options()
    # options.add_argument("--headless")
    options.add_experimental_option('prefs', {
        "download.default_directory": "C:\\Users\\Demilade Sodimu\\Documents\\my_notes",
        # To auto download the file
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        # It will not show PDF directly in chrome
        "plugins.always_open_pdf_externally": True
    })
    chrome_driver_path = "C:\\Development\\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # DETAILS
    file1 = open("myfile.txt", "r")
    fhand = file1.readlines()
    username_input = (fhand[0]).rstrip()
    password_input = (fhand[1]).rstrip()

    # MOODLE
    driver.get("https://moodle.cu.edu.ng/")

    # LOG IN
    login = driver.find_element(By.LINK_TEXT, 'Log in')
    login.click()
    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')
    username.send_keys(username_input)
    password.send_keys(password_input)
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
            # print(course.text)
            try:
                links = driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")
                for i in range(len(links)):
                    exists = "false"
                    myfile = (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).text
                    text = (myfile.split("\n"))[0]
                    files = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes")
                    for file in files:
                        file_name = os.path.splitext(file)[0]
                        if text == file_name:
                            exists = "true"
                            continue
                    if exists == "false":
                        (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).click()
            except:
                continue
            driver.get(dashboard)

    # files = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes")
    # for note in files:
    #     resources_popup("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\" + note)


crawl_moodle()
