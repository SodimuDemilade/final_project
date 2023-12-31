from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import PyPDF2
import os
import comtypes.client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from py_youtube import Data
from googlesearch import search
from moodle_project.actual_project.extract_keywords import get_keyword
import shutil
import win32com.client as win32


# FUNCTION TO COVERT PPTX TO pdf
def ppt_to_pdf(inputfilename, outputfilename, formattype=32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputfilename[-3:] != 'pdf':
        outputfilename = outputfilename + ".pdf"
    deck = powerpoint.Presentations.Open(inputfilename)
    # formatType = 32 for ppt to pdf
    deck.SaveAs(outputfilename, formattype)
    deck.Close()
    powerpoint.Quit()
    return outputfilename


# THIS IS T DOWNLOAD PDFS
def download_pdfs(pdf_links):
    documents_directory = os.path.expanduser("~\\Documents")
    resources_path = os.path.join(documents_directory, "my_notes\\notes_resources")
    if not os.path.exists(resources_path):
        os.makedirs(resources_path)
    options = Options()
    # options.add_argument("--headless")
    options.add_experimental_option('prefs', {
        "download.default_directory": resources_path,
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
    })
    chrome_driver_path = "C:\\Development\\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # links will be put here for download
    for link in pdf_links:
        file_extension = os.path.splitext(link)[1]
        file_extension = file_extension.lstrip(".")
        if file_extension == "pdf":
            try:
                driver.get(link)
            except:
                continue
            time.sleep(20)
        else:
            continue


# THIS IS FOR YOUTUBE VIDEOS
def myvideos(video_links):
    views_list = []
    for link in video_links:
        try:
            data = Data(link).data()
            my_dict = {'title': data['title'], 'link': link, 'views': int(data['views'])}
            views_list.append(my_dict)
        except:
            continue
    sorted_views = sorted(views_list, key=lambda x: x["views"], reverse=True)
    return sorted_views


# THIS IS TO EXTRACT KEYWORD FROM FILES
def get_resources(file_path):
    # GET NO OF RESOURCES
    file1 = open("myfile.txt", "r")
    fhand = file1.readlines()
    pdf_num = int((fhand[2]).rstrip())
    video_num = int((fhand[3]).rstrip())

    # CHECK THE FILE EXTENSION
    file_extension = os.path.splitext(file_path)[1]
    file_extension = file_extension.lstrip(".")
    if file_extension == "pdf":
        actual_file = file_path
    elif file_extension == "docx" or file_extension == "doc":
        word = win32.gencache.EnsureDispatch('Word.Application')
        output_pdf_file_path = os.path.splitext(file_path)[0] + ".pdf"
        doc = word.Documents.Open(file_path)
        doc.SaveAs(output_pdf_file_path, FileFormat=win32.constants.wdFormatPDF)
        doc.Close()
        actual_file = output_pdf_file_path
    else:
        output_pdf_file_path = os.path.splitext(file_path)[0] + ".pdf"
        output_file = ppt_to_pdf(file_path, output_pdf_file_path)
        actual_file = output_file

    # CONVERT PDF TO TEXT
    mytext = ''
    reader = PyPDF2.PdfReader(actual_file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        mytext += text
    # GET KEYWORD
    keyword = get_keyword(mytext)
    print(keyword)
    pdf_query = keyword + " pdf"
    video_query = keyword + " video"
    pdf_links = []
    video_links = []
    for i in search(pdf_query, tld="com", num=pdf_num, stop=pdf_num, pause=2):
        print(i)
        pdf_links.append(i)
    for j in search(video_query, tld="com", num=video_num, stop=video_num, pause=2):
        print(j)
        video_links.append(j)
    download_pdfs(pdf_links)
    video_dictionary = myvideos(video_links)
    return video_dictionary


class CustomDialog(tkinter.simpledialog.Dialog):
    def __init__(self, parent, title=None, text=None):
        self.data = text
        tkinter.simpledialog.Dialog.__init__(self, parent, title=title)

    def body(self, parent):
        self.text = tkinter.Text(self, width=80, height=25, bg="lightblue")
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", self.data)
        self.text.config(state=DISABLED)
        return self.text


def resources_popup():
    non_resources = ["DLD", "TMC", "EDS"]
    count = 0
    documents_directory = os.path.expanduser("~\\Documents")
    path = os.path.join(documents_directory, "my_notes\\courses")
    new_path = os.path.join(documents_directory, "my_notes\\NEW")
    resources_path = os.path.join(documents_directory, "my_notes\\notes_resources")
    resources_folder = [f.path for f in os.scandir(resources_path) if f.is_file()]
    sub_folders = [f.path for f in os.scandir(path) if f.is_dir()]
    new_sub_folders = [f.path for f in os.scandir(new_path) if f.is_dir()]
    resources_sub_folders = [f.path for f in os.scandir(resources_path) if f.is_dir()]
    for folder in new_sub_folders:
        folder_split = folder.split("\\")
        if folder_split[6][0:3] in non_resources:
            continue
        message = "Course Title: " + folder_split[6] + "\n" + "Check 'Documents\\notes_resources' for downloaded pdf " \
                                                              "resources\n\n"
        the_folder = [f.path for f in os.scandir(folder) if f.is_file()]
        for file in the_folder:
            message += "\nTopic: " + file + "\n"
            something = get_resources(os.path.join(file))
            for i in something:
                message += "Video Title: " + i['title'] + "\n"
                message += "Video Link: " + i['link'] + "\n"
                message += "Number of views: " + str(i['views']) + "\n" + "\n"
            destination_path = sub_folders[count]
            shutil.move(os.path.join(new_path, file), destination_path)
            for resource in resources_folder:
                destination_path = resources_sub_folders[count]
                shutil.move(os.path.join(resources_path, resource), destination_path)
            # time.sleep()
        count += 1
        root = Tk()
        root.title("Main Window")
        root.withdraw()
        CustomDialog(root, title='Youtube Recommendations', text=message)


# resources_popup()