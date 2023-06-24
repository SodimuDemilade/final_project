import os
import requests
# # i = "myname"
# source_dir = "C:\\Users\\Demilade Sodimu\\Desktop\\my_notes"
# # # os.mkdir("C:\\Users\\Demilade Sodimu\\Desktop\\my_notes\\" + i)
# # destination_dir = "C:\\Users\\Demilade Sodimu\\Desktop\\my_notes\\CSC412"
# #
# files = os.listdir(source_dir)
#
# for f in files:
#     print(f)
#     # shutil.move(os.path.join(source_dir, f), destination_dir)
# for i in range(0):
#     print("hi")
# files = os.listdir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW")
# list_sub_folders = [f.path for f in os.scandir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW") if f.is_dir()]
# list_files = [f.path for f in os.scandir("C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses") if f.is_file()]
# print(list_files)
# mylink = "https://moodle.cu.edu.ng/mod/resource/view.php?id=31130"
# response = requests.head(mylink)
#
# # Extract the filename from the 'Content-Disposition' header
# content_disposition = response.headers.get("Content-Disposition")
#
# # Extract the filename from the 'Content-Disposition' header value
# name = None
# if content_disposition:
#     file_name_start = content_disposition.find("filename=")
#     if file_name_start != -1:
#         name = content_disposition[file_name_start + len("filename="):].strip("\"'")
# print(name)
#
import os
import shutil
from pathlib import Path

# directory = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW"
#
# # Get a list of all files in the directory
# files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
#
# # Sort the files by date
# sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
#
# # Print the sorted file list
# for file in sorted_files:
#     print(file)

documents_directory = os.path.expanduser("~/Documents")
new_path = os.path.join(documents_directory, "my_notes\\NEW")
new_sub_folders = [f.path for f in os.scandir(new_path) if f.is_dir()]
for folder in new_sub_folders:
    folder = folder.split("\\")
    print(folder[5])
    print(folder[5][0:3])
print(new_sub_folders)






