import json
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,  QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtGui import QPixmap, QFont, QBrush, QColor
from PyQt5.QtCore import Qt

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

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("./Resource/down_panel.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setGeometry(0, 910, 1920, 250)

        self.settings_button = QPushButton("Settings", self)
        self.settings_button.setGeometry(50, 935, 150, 50)
        self.settings_button.setStyleSheet('background-color: rgba(255, 255, 255, 30); border-radius:25px; font-size:20px;border:1px solid rgba(255, 255, 255, 30);font: small-caps bold 24px/1 sans-serif;')
        self.settings_button.clicked.connect(self.open_settings)

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("./Resource/ametist_logo1.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setGeometry(810, 250, 300, 300)

        self.launch_button = QPushButton("Play", self)
        self.launch_button.setGeometry(860, 935, 150, 50)
        self.launch_button.setStyleSheet('background-color: rgba(255, 255, 255, 30); border-radius:25px; font-size:20px;border:1px solid rgba(255, 255, 255, 30);font: small-caps bold 24px/1 sans-serif;backdrop-filter: blur(12px);shadow:14px;')
        self.launch_button.clicked.connect(self.launch_minecraft)

        self.label = QLabel(self)
        self.label.setText("v1.1.1")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.move(940, 600,)
        self.label.setStyleSheet('color: white; border-left: 500px;')


    def launch_minecraft(nickname):
        minecraft_path = "C:/Users/drewa/AppData/Roaming/.minecraft/versions/1.20.1-OptiFine_HD_U_I5_pre9"
        os.chdir(minecraft_path)
        command = f'"C:\\Users\\drewa\\AppData\\Roaming\\.tlauncher\\legacy\\Minecraft\\jre\\java-runtime-gamma\\windows-x64\\java-runtime-gamma\\bin\\javaw.exe -Xms2048M -Xmx4096M -Dfile.encoding=UTF-8 -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j -cp C:\\Users\\drewa\\AppData\\Roaming\\.minecraft\\libraries\\optifine\\OptiFine\\1.20.1_HD_U_I5_pre9\\OptiFine-1.20.1_HD_U_I5_pre9.jar;C:\\Users\\drewa\\AppData\\Roaming\\.minecraft\\versions\\1.20.1\\1.20.1.jar net.minecraft.launchwrapper.Launch --username {nickname} --version 1.20.1 --gameDir C:\\Users\\drewa\\AppData\\Roaming\\.minecraft --assetsDir C:\\Users\\drewa\\AppData\\Roaming\\.minecraft\\assets --width 925 --height 530"'
        os.system(command)

    launch_minecraft("Drewax_")

    def open_settings(self):
        settings_window = SettingsPage(self)
        settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = MinecraftLauncher()
    launcher.show()
    sys.exit(app.exec_())