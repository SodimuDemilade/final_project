import traceback
import pystray
from moodle_project.resources2 import *
from moodle_project.startapp import check_wifi_status, start_app, exit_action
from pystray import MenuItem as Item
from PIL import Image
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.toast.kivytoast.kivytoast import toast
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.card import MDCard

Window.softinput_mode = "below_target"  # resize to accomodate keyboard
Window.keyboard_anim_args = {'d': 0.5, 't': 'in_out_quart'}

Builder.load_string("""
#:import utils kivy.utils

#:include login.kv
#:include category.kv
#:include home.kv
#:include job_list.kv

""")


# class JobListScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def on_enter(self):
#         for _ in range(10):
#             MDApp.get_running_app().job_list.append({"height": dp(150)})


# class JobListCard(MDCard):
#     def prepare_viewing_of_publication(self):
#         print(int(self.publication_id))
#
#     def view_job(self, job_card):
#         print(job_card)
#
#     def toggle_heart(self, widget):
#         if widget.icon == "heart":
#             widget.icon = "heart-outline" if widget.icon == "heart" else "heart-outline"
#             toast("Job unsaved")
#         else:
#             widget.icon = "heart" if widget.icon == "heart-outline" else "heart"
#             toast("Job saved")


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        MDApp.get_running_app().category_list.append({"height": dp(150)})
        MDApp.get_running_app().category_list.append({"height": dp(150)})
        MDApp.get_running_app().category_list.append({"height": dp(150)})
        MDApp.get_running_app().category_list.append({"height": dp(150)})
        MDApp.get_running_app().category_list.append({"height": dp(150)})


# class CategoryCard(CircularRippleBehavior, ButtonBehavior, MDCard):
#     def open_category(self, widget):
#         print(widget)
#
#     def on_release(self):
#         MDApp.get_running_app().manage_screens("job_list_screen", "add")
#         MDApp.get_running_app().change_screen("job_list_screen")


class Emp(MDApp):
    # job_list = ListProperty()  # contains data needed to display job list cards
    # category_list = ListProperty()  # contains data needed to display job list cards

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Moodle Web crawler"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.sm = ScreenManager()
        self.has_animated_card = False
        self.has_animated_background = False

    def callback(self, username, password):
        # self.username.text = "Hello " + self.username.text + "!"
        file1 = open("myfile.txt", "w")
        file1.write(username)
        file1.write("\n")
        file1.write(password)
        file1.write("\n")
        username = ""
        password = ""

    def main(self):
        image = Image.open("download.png")
        menu = (Item('Start App', start_app), Item('Exit', exit_action))
        icon = pystray.Icon("name", icon=image, menu=menu)
        icon.run()

    def display_videos(self):
        links = ['https://www.youtube.com/watch?v=SAaeWX_RBKc', 'https://www.youtube.com/watch?v=NzUTZj31AfM',
                 'https://www.youtube.com/watch?v=NBLD-YQDnTo&t=2s']
        to_print = myvideos(links)
        return to_print

    def account_action(self, email, password, username=None, action=None):
        print(email, password, username, action)
        if action == "register":
            pass
            # register the user
        elif action == "login":
            # login the user
            pass
        self.manage_screens("home_screen", "add")
        self.change_screen("home_screen")

    def animate_background(self, widget):
        if self.has_animated_background == False:
            anim = Animation(size_hint_y=1) + Animation(size_hint_y=0.5)
            anim.start(widget.ids.bx)
            print("background animated")
        else:
            print("background already animated")

    def animate_card(self, widget):
        # {"center_x": 0.5, "center_y": 0.6}
        if self.has_animated_card == False:
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
            "home_screen": Factory.HomeScreen
            # "job_list_screen": Factory.JobListScreen
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
        # self.sm.add_widget(Factory.HomeScreen())
        # self.sm.add_widget(HomeScreen(name="home_screen"))
        # self.sm.current = "login_screen"
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