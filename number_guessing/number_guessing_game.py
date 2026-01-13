#Python number guessing game
import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class NumberGuessing(QWidget):
    def __init__(self, lowest_num = 1, highest_num = 100):
        super().__init__()
        self.title = QLabel("Number Guessing Game", self)
        self.low_num = lowest_num
        self.high_num = highest_num
        self.answer = random.randint(self.low_num, self.high_num)
        self.guesses_count = 0
        self.num_label = QLabel(f"Select a number between {str(self.low_num)} and {str(self.high_num)}", self)
        self.num_input = QLineEdit(self)
        self.guess = QPushButton("Spin slots", self)
        self.output_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Number Guessing Game")

        vbox = QVBoxLayout()

        vbox.addWidget(self.title)
        vbox.addWidget(self.num_label)
        vbox.addWidget(self.num_input)
        vbox.addWidget(self.guess)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.title.setAlignment(Qt.AlignCenter)
        self.num_label.setAlignment(Qt.AlignCenter)
        self.num_input.setAlignment(Qt.AlignCenter)
        self.output_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("title")
        self.num_label.setObjectName("num_label")
        self.num_input.setObjectName("num_input")
        self.guess.setObjectName("guess")
        self.output_label.setObjectName("output_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
            }
            QLabel#title{
                font-size: 50px;
                margin : 20px;
                font-weight: bold;
                color: #f1c40f;
                letter-spacing: 2px;
            }
            QLabel, QPushButton{
                color: #f8fafc;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#num_label{
                font-size: 42px;
                font-weight: 800;
                color: #22c55e; 
                margin: 15px;
                letter-spacing: 1px;
            }
            QLineEdit#num_input{
                font-size: 36px;
                font-weight: bold;
                padding: 15px;
                background-color: #1e293b;
                border: 3px solid #334155;
                border-radius: 15px;
                color: #ffffff;
                margin: 10px 100px;
            }
            QLineEdit#num_input:focus {
                border: 3px solid #3b82f6; 
                background-color: #0f172a;
            }
            QPushButton#guess{
                font-size: 24px;
                font-weight: bold;
                color: white;
                background-color: #3b82f6;
                border-radius: 12px;
                padding: 18px;
                margin: 20px 120px;
                border: none;
                border-bottom: 5px solid #2563eb;
            }
            QPushButton#guess:hover {
                background-color: #60a5fa;
            }
            QPushButton#guess:pressed {
                border-bottom: 0px;
                margin-top: 25px;
            }
            QLabel#output_label{
               font-size: 34px;
                font-weight: 700;
                color: #f8fafc;
                margin-top: 15px;
            }
            QLabel#description_label{
                font-size: 24px;
                font-weight: 500;
                color: #94a3b8;
                margin-bottom: 20px;
            }
        """)

        self.guess.clicked.connect(self.number_guessing)

    def number_guessing(self):
        
        guess_text = self.num_input.text()

        if guess_text.isdigit():
            user_guess = int(guess_text)
            self.guesses_count+= 1

            if user_guess < self.low_num or user_guess > self.high_num:
                 self.output_label.setText("That number is out of range")
                 self.description_label.setText(f"Please Select a number between {self.low_num} and {self.high_num}")
            elif user_guess < self.answer:
                self.output_label.setText(f"Too low! Try again! (Number > {guess_text})")
                self.description_label.clear()
                self.num_input.clear()
            elif user_guess > self.answer:
                self.output_label.setText(f"Too high! Try again! (Number < {guess_text})")
                self.description_label.clear()
                self.num_input.clear()
            else:
                self.output_label.setText(f"CORRECT! The answer was {self.answer}")
                self.description_label.setText(f"Number of guesses: {self.guesses_count}")
        else:
            self.output_label.setText("invalid guess")
            self.description_label.setText(f"Please Select a number between {self.low_num} and {self.high_num}")


if __name__ == "__main__":
    starting_money = 100
    app = QApplication(sys.argv)
    num_guess = NumberGuessing()
    num_guess.show()
    sys.exit(app.exec_())
