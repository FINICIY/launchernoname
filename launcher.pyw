import json
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QFont
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
        self.setStyleSheet("background-color: #333333; color: white;")

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("./Resource/down_panel.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setGeometry(0, 850, 1920, 250)

        self.settings_button = QPushButton("Settings", self)
        self.settings_button.setGeometry(860, 700, 200, 52)
        self.settings_button.setStyleSheet('background-color: rgba(255, 255, 255, 20); border-radius:25px; font-size:20px;border:1px solid rgba(255, 255, 255, 20);font: small-caps bold 24px/1 sans-serif;')
        self.settings_button.clicked.connect(self.open_settings)

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap("./Resource/ml200.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setGeometry(860, 350, 200, 200)

        self.launch_button = QPushButton("PLAY", self)
        self.launch_button.setGeometry(860, 910, 200, 52)
        self.launch_button.setStyleSheet('background-color: rgba(255, 255, 255, 20); border-radius:25px; font-size:20px;border:1px solid rgba(255, 255, 255, 20);font: small-caps bold 24px/1 sans-serif;')
        self.launch_button.clicked.connect(self.launch_minecraft)

        self.label = QLabel(self)
        self.label.setText("tested version <br> launcher for <br>home usage")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.move(860, 600)
        self.label.setStyleSheet('color: white; border-left: 10px;')

    def launch_minecraft(self):
        minecraft_path = "C:/Users/drewa/AppData/Roaming/.minecraft/versions/1.20.1-OptiFine_HD_U_I5_pre9"
        os.chdir(minecraft_path)
        command = f"java -Xms8192m -Xmx15384m -jar 1.20.1-OptiFine_HD_U_I5_pre9.jar {Nickname} {Password} {ip_server}"
        os.system(command)

    def open_settings(self):
        settings_window = SettingsPage(self)
        settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = MinecraftLauncher()
    launcher.show()
    sys.exit(app.exec_())