import pystray
from moodle_project.startapp import check_wifi_status, start_app, exit_action
from pystray import MenuItem as Item
from PIL import Image
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window


class TestWindow(Screen):
    pass


class MainWindow(Screen):
    def main(self):
        image = Image.open("download.png")
        menu = (Item('Start App', start_app), Item('Exit', exit_action))
        icon = pystray.Icon("name", icon=image, menu=menu)
        icon.run()


    def close(self):
        App.get_running_app().stop()
        Window.close()
    

class FirstWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def callback(self):
        # self.username.text = "Hello " + self.username.text + "!"
        file1 = open("myfile.txt", "w")
        file1.write(self.username.text)
        file1.write("\n")
        file1.write(self.password.text)
        file1.write("\n")
        self.username.text = ""
        self.password.text = ""

    def close(self):
        App.get_running_app().stop()
        Window.close()


class SecondWindow(Screen):
    def main(self):
        image = Image.open("download.png")
        menu = (Item('Start App', start_app), Item('Exit', exit_action))
        icon = pystray.Icon("name", icon=image, menu=menu)
        icon.run()


    def close(self):
        App.get_running_app().stop()
        Window.close()


class KeywordWindow(Screen):
    def close(self):
        App.get_running_app().stop()
        Window.close()


class NoteWindow(Screen):
    def close(self):
        App.get_running_app().stop()
        Window.close()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('moodleGUI.kv')
sm = WindowManager()

sm.add_widget(TestWindow(name='test'))
sm.add_widget(MainWindow(name='main'))
sm.add_widget(FirstWindow(name='first'))
sm.add_widget(SecondWindow(name='second'))
sm.add_widget(KeywordWindow(name='keyword'))
sm.add_widget(NoteWindow(name='note'))


class MoodleMain(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MoodleMain().run()
