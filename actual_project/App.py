import traceback
import pystray
from moodle_project.actual_project.resources2 import *
from moodle_project.actual_project.startapp import start_app, exit_action
from pystray import MenuItem as Item
from PIL import Image
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.factory import Factory
from kivy.animation import Animation
# from kivy.metrics import dp
from kivymd.app import MDApp
# import winreg as reg
import os
from tkinter import *
from tkinter import messagebox

Window.softinput_mode = "below_target"  # resize to accommodate keyboard
Window.keyboard_anim_args = {'d': 0.5, 't': 'in_out_quart'}

Builder.load_string("""
#:import utils kivy.utils

#:include login.kv

""")


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Emp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "SpiderNet"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.sm = ScreenManager()
        self.has_animated_card = False
        self.has_animated_background = False

    def save_details(self, username, password, courses):
        file1 = open("myfile.txt", "w")
        file1.write(username)
        file1.write("\n")
        file1.write(password)
        file1.write("\n")
        file1.write("5")
        file1.write("\n")
        file1.write("5")
        file1.write("\n")
        courses_list = courses.split(',')
        for course in courses_list:
            documents_directory = os.path.expanduser("~/Documents")
            path = os.path.join(documents_directory, "my_notes\\courses", course)
            new_path = os.path.join(documents_directory, "my_notes\\NEW", course)
            resources_path = os.path.join(documents_directory, "my_notes\\notes_resources", course)
            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            if not os.path.exists(resources_path):
                os.mkdir(resources_path)

    def change_details(self, username, password):
        file1 = open("myfile.txt", "r+")
        fhand = file1.readlines()
        fhand[0] = username + "\n"
        fhand[1] = password + "\n"
        with open('myfile.txt', 'w') as file:
            file.writelines(fhand)

    def change_no_of_pdfs(self, pdf_num):
        file1 = open("myfile.txt", "r")
        fhand = file1.readlines()
        fhand[2] = str(pdf_num) + "\n"
        with open('myfile.txt', 'w') as file:
            file.writelines(fhand)

    def change_no_of_videos(self, video_num):
        file1 = open("myfile.txt", "r+")
        fhand = file1.readlines()
        fhand[3] = str(video_num) + "\n"
        with open('myfile.txt', 'w') as file:
            file.writelines(fhand)

    def main(self):
        file_path = 'C:\\Users\\Demilade Sodimu\\PycharmProjects\\scrapy_tutorial\\moodle_project\\myfile.txt'
        if os.path.getsize(file_path) == 0:
            root = Tk()
            root.title("Main Window")
            root.withdraw()
            messagebox.showerror('Error', 'Please save details first')
        image = Image.open("download.png")
        menu = (Item('Start App', start_app), Item('Exit', exit_action))
        icon = pystray.Icon("name", icon=image, menu=menu)
        icon.run()

    # def add_to_reg(self):
    #     key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0,
    #                       reg.KEY_ALL_ACCESS)
    #     reg.SetValueEx(key, "Moodle_Crawler", 0, reg.REG_SZ, "C:\\Users\\Demilade Sodimu\\PycharmProjects\\scrapy_tutorial\\moodle_project\\moodle.py")
    #     reg.CloseKey(key)

    def close(self):
        MDApp.get_running_app().stop()
        Window.close()

    def animate_background(self, widget):
        if not self.has_animated_background:
            anim = Animation(size_hint_y=1) + Animation(size_hint_y=0.5)
            anim.start(widget.ids.bx)
            print("background animated")
        else:
            print("background already animated")

    def animate_card(self, widget):
        # {"center_x": 0.5, "center_y": 0.6}
        if not self.has_animated_card:
            anim = Animation(pos_hint={"center_x": 0.5, "center_y": 0.6}, duration=2)
            anim.start(widget)
            self.has_animated_card = True
            print("card animated")
        else:
            print("card already animated")

    def change_screen(self, screen_name):
        if self.sm.has_screen(screen_name):
            self.sm.current = screen_name
        else:
            print("Screen [" + screen_name + "] does not exist.")

    def manage_screens(self, screen_name, action):
        scns = {
            "login_screen": Factory.LoginScreen,
            "registration_screen": Factory.RegistrationScreen,
            "settings_screen": Factory.SettingsScreen
        }
        try:

            if action == "remove":
                if self.sm.has_screen(screen_name):
                    self.sm.remove_widget(self.sm.get_screen(screen_name))
                print("Screen [" + screen_name + "] removed")
            elif action == "add":
                if self.sm.has_screen(screen_name):
                    print("Screen [" + screen_name + "] already exists")
                else:
                    self.sm.add_widget(scns[screen_name](name=screen_name))
                    print(screen_name + " added")
                    print("Screen [" + screen_name + "] added")
        except:
            print(traceback.format_exc())
            print("Traceback ^.^")

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def build(self):
        self.bind(on_start=self.post_build_init)
        self.sm.add_widget(Factory.LoginScreen())
        return self.sm

    def post_build_init(self, ev):
        win = self._app_window
        win.bind(on_keyboard=self._key_handler)

    def _key_handler(self, *args):
        key = args[1]
        # 1000 is "back" on Android
        # 27 is "escape" on computers
        if key in (1000, 27):
            try:
                self.sm.current_screen.dispatch("on_back_pressed")
            except Exception as e:
                print(e)
            return True
        elif key == 1001:
            try:
                self.sm.current_screen.dispatch("on_menu_pressed")
            except Exception as e:
                print(e)
            return True


if __name__ == "__main__":
    Emp().run()
