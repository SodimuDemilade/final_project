import cx_Freeze
import sys
base = None

if sys.platform == "win32":
    base = "Win32GUI"
sys.setrecursionlimit(10000)

executables = [cx_Freeze.Executable('App.py', base=base, icon='spider.ico')]

cx_Freeze.setup(
    name="SpiderNet",
    options={"build_exe": {"packages": ["tkinter", "traceback", "pystray", "PIL", "kivy", "kivymd", "os", "selenium",
                                        "time", "shutil", "PyPDF2", "comtypes.client", "py_youtube", "googlesearch",
                                        "psutil", "subprocess"],
                           "include_files": ["run_app.py", "moodle.py", "resources.py", "download.png", "login.kv"]}},
    version="0.01",
    description="A web crawler to download notes from Moodle and additional resources, \n Copyright: 2023-2024",
    executables=executables
)