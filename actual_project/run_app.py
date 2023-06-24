import psutil
import pystray
from pystray import MenuItem as Item
import subprocess
from PIL import Image


def check_wifi_status():
    interfaces = psutil.net_if_addrs()
    if "Wi-Fi" in interfaces:
        wifi_address = interfaces["Wi-Fi"][0].address
        return wifi_address != "0.0.0.0"
    return False


def start_app(icon, item):
    # Replace 'your_app_path' with the actual path to your desktop app
    subprocess.Popen(['C:\\Users\\Demilade Sodimu\\PycharmProjects\\scrapy_tutorial\\venv\\Scripts\\python.exe',
                      'C:\\Users\\Demilade Sodimu\\PycharmProjects\\scrapy_tutorial\\moodle_project\\moodle.py'])
    print("App started successfully.")


def exit_action(icon, item):
    icon.stop()


image = Image.open("download.png")


def main():
    menu = (Item('Start App', start_app), Item('Exit', exit_action))
    icon = pystray.Icon("name", icon=image, menu=menu)
    icon.run()


# def get_icon_data(file_path):
#     with open(file_path, "rb") as icon_file:
#         return icon_file.read()


# if __name__ == "__main__":
#     main()
