from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#Define our different screens
class FirstWindow(Screen, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
      
    def callback(self):
        self.username.text = "Hello " + self.username_input.text + "!"

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('myGUI.kv')


class CrawlerApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    CrawlerApp().run()


