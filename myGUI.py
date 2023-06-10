from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


#Define our different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class CrawlerApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.username = Label(
                        text="Enter your moodle username:",
                        font_size=18,
                        color='#00FFCE'
                        )
        self.window.add_widget(self.username)
        self.username_input = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.username_input)

        self.password = Label(
            text="Enter your moodle password:",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.password)
        self.password_input = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.password_input)

        # button widget
        self.button = Button(
                    text="SAVE",
                    size_hint=(1, 0.5),
                    bold=True,
                    background_color='#00FFCE',
                    # background_normal=""
                    )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.username.text = "Hello " + self.username_input.text + "!"
        file1 = open("myfile.txt", "w")
        file1.write(self.username_input.text)
        file1.write(self.password_input.text)


if __name__ == "__main__":
    CrawlerApp().run()