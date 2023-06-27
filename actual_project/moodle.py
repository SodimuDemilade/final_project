from moodle_project.actual_project.resources import resources_popup
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import shutil
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox


class CustomDialog(tkinter.simpledialog.Dialog):
    def __init__(self, parent, title=None, text=None):
        self.data = text
        tkinter.simpledialog.Dialog.__init__(self, parent, title=title)

    def body(self, parent):
        self.text = tkinter.Text(self, width=80, height=10, bg="white")
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", self.data)
        self.text.config(state=DISABLED)
        return self.text


class CustomEventListener(AbstractEventListener):
    def on_download(self, event):
        my_file = event.file_name
        print(my_file)


documents_directory = os.path.expanduser("~\\Documents")
path = os.path.join(documents_directory, "my_notes\\courses")
new_path = os.path.join(documents_directory, "my_notes\\NEW")
resources_path = os.path.join(documents_directory, "my_notes\\notes_resources")
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

mynote_path = 'C:\\Users\\Demilade Sodimu\\PycharmProjects\\scrapy_tutorial\\moodle_project\\actual_project' \
              '\\mynotes.txt'
if not os.path.exists(mynote_path):
    mycreate = open("mynotes.txt", "w")

dashboard = 'https://moodle.cu.edu.ng/my/'
course_group = []
for _ in range(len(courses)):
    # THIS IS BECAUSE I ENROLLED FOR CIS421 ALSO
    if _ != 0:
        driver.implicitly_wait(200)
        course = driver.find_element(By.PARTIAL_LINK_TEXT, courses[_][0:9])
        if course.text == "TMC422-Total Man Concept - Sports VIII":
            continue
        course.click()
        no_of_files = 0
        try:
            links = driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")
            for i in range(len(links)):
                exists = "false"
                myfile = (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).text
                file_text = (myfile.split("\n"))[0]
                # files = os.listdir(path)
                # for file in files:
                #     file_name = os.path.splitext(file)[0]
                #     if file_text == file_name:
                #         exists = "true"
                #         break
                fhandle = open("mynotes.txt", "r+")
                myread = fhandle.readlines()
                for line in myread:
                    line = line.rstrip()
                    if file_text == line:
                        exists = "true"
                        break
                if exists == "false":
                    writeto = open("mynotes.txt", "a")
                    writeto.write(file_text)
                    writeto.write("\n")
                    (driver.find_elements(By.CSS_SELECTOR, ".modtype_resource div div div div a")[i]).click()
                    no_of_files += 1
        except:
            continue
        course_group.append(no_of_files)
        driver.get(dashboard)


# TO GROUP THE NOTES INTO THEIR COURSES_FOLDERS
list_sub_folders = [f.path for f in os.scandir(path) if f.is_dir()]
new_sub_folders = [f.path for f in os.scandir(new_path) if f.is_dir()]
counter = 0
source_path = os.path.join(documents_directory, "my_notes\\NEW")
# list_files = [f.path for f in os.scandir(source_path) if f.is_file()]
files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(source_path, x)))
# source_dir = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW")
for i in range(len(course_group)):
    destination_path = new_sub_folders[i]
    for j in range(course_group[i]):
        shutil.move(os.path.join(source_path, sorted_files[counter]), destination_path)
        counter += 1

root = Tk()
root.title("Main Window")
root.withdraw()
CustomDialog(root, title='Notes Downloaded', text="Some new notes have been downloaded, check 'Documents\\my_notes"
                                                  "\\NEW' for these notes")

# THIS IS TO RUN THE RESOURCES FUNCTION AND POPUP
resources_popup()




