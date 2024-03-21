import json
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import minecraft_launcher_lib

# Замените на свои данные для Azure Application
CLIENT_ID = "YOUR CLIENT ID"
REDIRECT_URL = "YOUR REDIRECT URL"

with open('settings.json', 'r') as file:
    data = json.load(file)

Nickname = data['Nickname']
Password = data['Password']
ip_server = "realmc.space"


class SettingsPage:
    def __init__(self):
        self.data = json.load(file)
        self.setWindowTitle("Settings")
        self.setGeometry(100, 60, 500, 400)
        self.setStyleSheet("background-color: #333333; color: white;")

        # Add or modify the desired variables
        self.data['Nickname'] = "Drewax"
        self.data['Password'] = "0000000"
        self.data['windowed'] = False

        # Save the updated settings back to the JSON file
        with open('settings.json', 'w') as file:
            json.dump(self.data, file, indent=4)


class MinecraftLauncher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Quick Space Launcher")
        self.setGeometry(100, 60, 1000, 800)
        self.setStyleSheet("color: white;")

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("./Resource/background.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setGeometry(0, 0, 1920, 1080)

        # Остальной код UI опущен для краткости

    def launch_minecraft(self, nickname):
        # Получаем последнюю версию Minecraft
        latest_version = minecraft_launcher_lib.utils.get_latest_version()["release"]
        # Получаем директорию Minecraft
        minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

        # Запускаем Minecraft с помощью библиотеки
        options = {
            "username": nickname,
            "uuid": "",  # UUID можно получить из ответа на авторизацию, если необходимо
            "token": ""  # Токен доступа можно получить из ответа на авторизацию, если необходимо
        }
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
        subprocess.run(minecraft_command)

    def open_settings(self):
        settings_window = SettingsPage(self)
        settings_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = MinecraftLauncher()
    launcher.show()
    sys.exit(app.exec_())
