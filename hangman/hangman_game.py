#Hangman in Python 
from hangman_wordslist import words
import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

hangman_art = {
    0: ("  +---+  ",
        "  |   |  ",
        "      |  ",
        "      |  ",
        "      |  ",
        "========="),
    1: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        "      |  ",
        "      |  ",
        "========="),
    2: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        "  |   |  ",
        "      |  ",
        "========="),
    3: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        " /|   |  ",
        "      |  ",
        "========="),
    4: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        " /|\\  |  ",
        "      |  ",
        "========="),
    5: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        " /|\\  |  ",
        " /    |  ",
        "========="),
    6: ("  +---+  ",
        "  |   |  ",
        "  O   |  ",
        " /|\\  |  ",
        " / \\  |  ",
        "=========")}

hangman_gui_art = {
        key: "\n".join(lines) for key, lines in hangman_art.items()
    }



class Hangman(QWidget):
    def __init__(self):
        super().__init__()
        self.words = words
        self.answer = random.choice(self.words).lower()
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.title = QLabel("Hangman", self)
        self.hangman_label = QLabel("Enter a letter (a, b, c...): ", self)
        self.hangman_input = QLineEdit(self)
        self.play = QPushButton("Submit", self)
        self.hint_label = QLabel(" ".join(self.hint), self)
        self.hangman_drawing = QLabel(hangman_gui_art[0], self)
        self.description_label1 = QLabel(self)
        self.description_label2 = QLabel(self)
        self.initUI()

    def initUI(self):

        
        self.setWindowTitle("Hangman")
        self.resize(800, 950)
        self.move(600, 0)

        vbox = QVBoxLayout()
        vbox.setSpacing(20)

        vbox.addWidget(self.title)
        vbox.addWidget(self.hangman_label)
        vbox.addWidget(self.hangman_input)
        vbox.addWidget(self.play)
        vbox.addWidget(self.hangman_drawing)
        vbox.addWidget(self.hint_label)
        vbox.addWidget(self.description_label1)
        vbox.addWidget(self.description_label2)

        self.setLayout(vbox)

        self.title.setAlignment(Qt.AlignCenter)
        self.hangman_label.setAlignment(Qt.AlignCenter)
        self.hangman_input.setAlignment(Qt.AlignCenter)
        self.hangman_drawing.setAlignment(Qt.AlignCenter)
        self.hint_label.setAlignment(Qt.AlignCenter)
        self.description_label1.setAlignment(Qt.AlignCenter)
        self.description_label2.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("title")
        self.hangman_label.setObjectName("hangman_label")
        self.hangman_input.setObjectName("hangman_input")
        self.play.setObjectName("play")
        self.hangman_drawing.setObjectName("hangman_drawing")
        self.hint_label.setObjectName("hint_label")
        self.description_label1.setObjectName("description_label1")
        self.description_label2.setObjectName("description_label2")

        self.setStyleSheet("""
            QWidget { 
            background-color: #000000; 
            }

            QLabel, QPushButton { 
            color: #ffffff; 
            font-family: 'Segoe UI', sans-serif; 
            }

            QLabel#title {
                font-size: 56px;
                font-weight: bold;
                color: #e94560;
                background-color: #111111;
                border-left: 10px solid #e94560;
                padding-left: 20px;
                margin-bottom: 10px;
            }

            QLabel#hangman_drawing {
                font-family: 'Courier New', monospace;
                font-size: 40px; 
                color: #bc13fe;
                background-color: #080808;
                border: 2px solid #333333;
                border-radius: 20px;
                padding: 20px;
            }

            QLabel#hint_label {
                font-size: 48px;
                color: #ffffff;
                letter-spacing: 16px;
                margin: 10px;
            }

            QLabel#hangman_label { 
            font-size: 28px; 
            color: #888888; 
            }

            QLineEdit#hangman_input {
                font-size: 40px;
                background-color: #111111;
                border: 2px solid #e94560;
                color: #e94560;
                padding: 4px;
            }

            QPushButton#play {
                font-size: 36px;
                background-color: #e94560;
                color: #000000;
                padding: 10px;
            }

            QLabel#description_label1 { 
            font-size: 28px; 
            color: #bc13fe;  
            }

            QLabel#description_label2 { 
            font-size: 44px; 
            font-weight: bold; 
            color: #e94560;
            }
            
        """)

        self.play.clicked.connect(self.hang)

    def hang(self):
        guess = self.hangman_input.text().lower().strip()
        self.hangman_input.clear()

        if len(guess) != 1 or not guess.isalpha():
            self.description_label1.setText("Invalid input")
            return

        if guess in self.guessed_letters:
            self.description_label1.setText(f"{guess} is already guessed")
            return

        self.guessed_letters.add(guess)
        self.description_label1.setText("")

        if guess in self.answer:
            for i in range(len(self.answer)):
                if self.answer[i] == guess:
                    self.hint[i] = guess
            self.hint_label.setText(" ".join(self.hint))
        else:
            self.wrong_guesses += 1

            if self.wrong_guesses in hangman_gui_art:
                self.hangman_drawing.setText(hangman_gui_art[self.wrong_guesses])

        if "_" not in self.hint:
            self.description_label2.setText("YOU WIN!")
            self.play.setEnabled(False)


        elif self.wrong_guesses >= 6:
            self.description_label2.setText(f"YOU LOSE! \n Answer: {self.answer}")
            self.play.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Hangman()
    game.show()
    sys.exit(app.exec_())
