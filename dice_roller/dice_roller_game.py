#Dice roller program in python
import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()
        self.dice_art = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        self.title = QLabel("Dice Roller", self)
        self.dice_label = QLabel("Enter the number of dice:  ", self)
        self.dice_input = QLineEdit(self)
        self.play = QPushButton("Roll Dice", self)
        self.emoji_label1 = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):

        
        self.setWindowTitle("Dice Roller")
        self.move(600, 100)

        vbox = QVBoxLayout()

        vbox.addWidget(self.title)
        vbox.addWidget(self.dice_label)
        vbox.addWidget(self.dice_input)
        vbox.addWidget(self.play)
        vbox.addWidget(self.emoji_label1)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.title.setAlignment(Qt.AlignCenter)
        self.dice_label.setAlignment(Qt.AlignCenter)
        self.dice_input.setAlignment(Qt.AlignCenter)
        self.emoji_label1.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("title")
        self.dice_label.setObjectName("dice_label")
        self.dice_input.setObjectName("dice_input")
        self.play.setObjectName("play")
        self.emoji_label1.setObjectName("emoji_label1")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
            }
            QLabel, QPushButton{
                color: #ecf0f1;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#title{
                font-size: 50px;
                margin : 20px;
                font-weight: bold;
                color: #f1c40f;
                letter-spacing: 2px;
            }
            QLabel#dice_label{
                font-size: 50px;
                font-style: italic;
                margin : 20px;
            }
            QLineEdit#dice_input{
                font-size: 50px;
                margin : 20px;
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                color: #2c3e50;
            }
            QPushButton#play{
                font-size: 30px;
                font-weight: bold;
                background-color: #27ae60;
                color: white;
                border-radius: 10px;
                padding: 15px;
            }
            QLabel#emoji_label1{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.play.clicked.connect(self.roll_dice)

    def roll_dice(self):
        try:
            num_dice = int(self.dice_input.text())
            if num_dice <= 0:
                raise ValueError
            
            dice_results = [random.randint(1, 6) for _ in range(num_dice)]
            
            display_emojis = "".join([self.dice_art[d] for d in dice_results[:10]])
            if num_dice > 10:
                display_emojis += "..."

            total = sum(dice_results)
            
            self.emoji_label1.setText(display_emojis)
            self.description_label.setText(f"Total: {total}")
            
        except ValueError:
            self.description_label.setText("Enter a valid number!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dice = DiceRoller()
    dice.show()
    sys.exit(app.exec_())