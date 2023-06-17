import os
from moodle_project.resources2 import resources_popup
# i = "myname"
# source_dir = "C:\\Users\\Demilade Sodimu\\Desktop\\my_notes"
# # os.mkdir("C:\\Users\\Demilade Sodimu\\Desktop\\my_notes\\" + i)
# destination_dir = "C:\\Users\\Demilade Sodimu\\Desktop\\my_notes\\CSC412"
#
# files = os.listdir(source_dir)
#
# for f in files:
#     print(f)
#     # shutil.move(os.path.join(source_dir, f), destination_dir)

files = os.listdir("C:\\Users\\Demilade Sodimu\\Desktop\\my_notes")
for note in files:
    resources_popup("C:\\Users\\Demilade Sodimu\\Desktop\\my_notes\\" + note)
