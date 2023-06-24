# from moodle_project.resources2 import get_resources
# from tkinter import *
# import tkinter.simpledialog
# import tkinter.messagebox
# import os
# import shutil
#
# class CustomDialog(tkinter.simpledialog.Dialog):
#     def __init__(self, parent, title=None, text=None):
#         self.data = text
#         tkinter.simpledialog.Dialog.__init__(self, parent, title=title)
#
#     def body(self, parent):
#         self.text = tkinter.Text(self, width=80, height=30)
#         self.text.pack(fill="both", expand=True)
#         self.text.insert("1.0", self.data)
#         self.text.config(state=DISABLED)
#         return self.text
#
#
# path = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\NEW"
# list_sub_folders = [f.path for f in os.scandir(path) if f.is_dir()]
# for folder in list_sub_folders:
#     message = "Put Course Name Here\n" + "Check this path for downloaded pdf resources\n\n"
#     for file in path:
#         message += "\nTopic: " + file + "\n"
#         something = get_resources(os.path.join(folder, file))
#         for i in something:
#             message += "Video Title: " + i['title'] + "\n"
#             message += "Video Link: " + i['link'] + "\n"
#             message += "Number of views: " + str(i['views']) + "\n" + "\n"
#     root = Tk()
#     root.title("Main Window")
#     root.withdraw()
#     CustomDialog(root, title='Youtube Recommendations', text=message)
#     new_path = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\NEW\\CSC421"
#     for file in new_path:
#         list_files = [f.path for f in os.scandir(new_path)]
#         destination_path = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\CSC421"
#         shutil.move(os.path.join(new_path, file), destination_path)

from moodle_project.actual_project.resources2 import resources_popup
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import shutil
from urllib.parse import urlparse, parse_qs
import requests

documents_directory = os.path.expanduser("~/Documents")
path = os.path.join(documents_directory, "my_notes\\courses")
new_path = os.path.join(documents_directory, "my_notes\\NEW")
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(new_path):
    os.makedirs(new_path)
# list_sub_folders = [f.path for f in os.scandir(new_path) if f.is_dir()]

options = Options()
# options.add_argument("--headless")
options.add_experimental_option('prefs', {
    "download.default_directory": new_path,
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
count = 0
file_name = None
course_group = []
for _ in range(len(courses)):
    # THIS IS BECAUSE I ENROLLED FOR CIS421 ALSO
    if _ != 0:
        driver.implicitly_wait(100)
        course = driver.find_element(By.PARTIAL_LINK_TEXT, courses[_][0:9])
        course.click()
        no_of_files = 0
        try:
            links = driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")
            for i in range(len(links)):
                exists = "false"
                mylink = links[0].get_attribute('href')
                # parsed_url = urlparse(mylink)
                # query_params = parse_qs(parsed_url.query)
                # file_id = query_params.get('id')[0] if query_params.get('id') else None
                files = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses")
                myfile = (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).text
                file_text = (myfile.split("\n"))[0]
                for file in files:
                    file_name = os.path.splitext(file)[0]
                    if file_text == file_name:
                        exists = "true"
                        break
                if exists == "false":
                    (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).click()
                    no_of_files += 1
            course_group.append(no_of_files)
                # time.sleep(10)
                # original_file_name = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses")[0]
                # ext = os.path.splitext(original_file_name)[1]
                # new_file_name = file_id + "." + ext
                # original_file_path = os.path.join("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\NEW", original_file_name)
                # new_file_path = os.path.join("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\NEW", new_file_name)
                # os.rename(original_file_path, new_file_path)
            # driver.get(mylink)
            #
            # # Find the download link element
            # download_link = driver.find_element(By.XPATH, "//a[@class='resourceworkaround']")
            #
            # # Get the actual file name from the download link
            # file_name = download_link.get_attribute("download")
            #
            # driver.quit()

                # # Access the response headers
                # response_headers = driver.execute_script("return window.performance.getEntries()[0].responseHeaders")
                #
                # # Find the Content-Disposition header
                # content_disposition = None
                # for header in response_headers.splitlines():
                #     if header.startswith("Content-Disposition"):
                #         content_disposition = header
                #         break
                #
                # # Extract the file name from the Content-Disposition header
                # if content_disposition:
                #     file_name = content_disposition.split("filename=")[1].strip('"')
                #     print("File name:", file_name)
                #
                # # Close the WebDriver
                # driver.quit()
                # driver.get(mylink.format(file_id))
                # the_file = driver.find_element(By.ID, 'file-name').text
                # print(the_file)
        except:
            continue
        driver.get(dashboard)
    # count += 1

# TO GROUP THE NOTES INTO THEIR COURSES_FOLDERS
# list_sub_folders = [f.path for f in os.scandir(path) if f.is_dir()]
# new_sub_folders = [f.path for f in os.scandir(new_path) if f.is_dir()]
# counter = 0
# source_path = os.path.join(documents_directory, "my_notes\\NEW")
# # list_files = [f.path for f in os.scandir(source_path) if f.is_file()]
# files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
# sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(source_path, x)))
# # source_dir = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW")
# for i in range(len(course_group)):
#     destination_path = list_sub_folders[i]
#     for j in range(course_group[i]):
#         shutil.move(os.path.join(source_path, sorted_files[counter]), destination_path)
#         counter += 1

# THIS IS TO RUN THE RESOURCES FUNCTION AND POPUP
# resources_popup(course_group)


