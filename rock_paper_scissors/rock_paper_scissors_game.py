#Python rock paper scissors game
import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt 

class RockPapersScissors(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Rock, Paper, Scissors", self)
        self.game_label2 = QLabel("Enter a choice (rock, paper, scissors): ", self)
        self.game_input = QLineEdit(self)
        self.play = QPushButton("Submit", self)
        self.player = QLabel("Player", self)
        self.vs = QLabel("VS", self)
        self.computer = QLabel("Computer", self)
        self.emoji_label1 = QLabel(self)
        self.emoji_label2 = QLabel(self)
        self.emoji_label3 = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):

        
        self.setWindowTitle("Rock, Paper, Scissors Game")
        self.move(600, 50)
        self.setFixedSize(800, 900)

        vbox = QVBoxLayout()

        vbox.addWidget(self.title)
        vbox.addWidget(self.game_label2)
        vbox.addWidget(self.game_input)
        vbox.addWidget(self.play)

        hbox1 = QHBoxLayout() 
        hbox1.addWidget(self.player)
        hbox1.addWidget(self.vs)
        hbox1.addWidget(self.computer)

        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout() 
        hbox2.addWidget(self.emoji_label1)
        hbox2.addWidget(self.emoji_label3)
        hbox2.addWidget(self.emoji_label2)

        vbox.addLayout(hbox2)

        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.title.setAlignment(Qt.AlignCenter)
        self.game_label2.setAlignment(Qt.AlignCenter)
        self.game_input.setAlignment(Qt.AlignCenter)
        self.player.setAlignment(Qt.AlignCenter)
        self.vs.setAlignment(Qt.AlignCenter)
        self.computer.setAlignment(Qt.AlignCenter)
        self.emoji_label1.setAlignment(Qt.AlignCenter)
        self.emoji_label3.setAlignment(Qt.AlignCenter)
        self.emoji_label2.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.title.setObjectName("title")
        self.game_label2.setObjectName("game_label2")
        self.game_input.setObjectName("game_input")
        self.play.setObjectName("play")
        self.player.setObjectName("player")
        self.vs.setObjectName("vs")
        self.computer.setObjectName("computer")
        self.emoji_label1.setObjectName("emoji_label1")
        self.emoji_label3.setObjectName("emoji_label3")
        self.emoji_label2.setObjectName("emoji_label2")
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
            QLabel#game_label2{
                font-size: 45px;
                font-style: italic;
                margin : 20px;
            }
            QLineEdit#game_input{
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
            QLabel#player{
                font-size: 50px;
                font-style: bold;
                margin : 40px;
            }
            QLabel#vs{
                font-size: 40px;
                font-style: bold;
                margin : 40px;
            }
            QLabel#computer{
                font-size: 50px;
                font-style: bold;
                margin : 40px;
            }
            QLabel#emoji_label1{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#emoji_label2{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#emoji_label3{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.play.clicked.connect(self.RPC)

    def RPC(self):
        options = ("rock", "paper", "scissors")
        player = self.game_input.text().lower().strip()
        computer = random.choice(options)

        if player not in options:
            self.description_label.setText("Invalid Choice! \n Type rock, paper, or scissors.")


        if player == computer:
            self.description_label.setText("It is a tie!")
            self.emoji_label3.setText('=')
            if player == "rock":
                self.emoji_label1.setText('🪨')
                self.emoji_label2.setText('🪨')

            elif player == "paper":
                self.emoji_label1.setText('📄')
                self.emoji_label2.setText('📄')

            elif player == "scissors":
                self.emoji_label1.setText('✂️')

                self.emoji_label2.setText('✂️')

        elif player == "rock" and computer == "scissors":
            self.description_label.setText("You win!")
            self.emoji_label1.setText('🪨')
            self.emoji_label3.setText('>')
            self.emoji_label2.setText('✂️')

        elif player == "paper" and computer == "rock":
            self.description_label.setText("You win!")
            self.emoji_label1.setText('📄')
            self.emoji_label3.setText('>')
            self.emoji_label2.setText('🪨')

        elif player == "scissors" and computer == "paper":
            self.description_label.setText("You win!")
            self.emoji_label1.setText('✂️')
            self.emoji_label3.setText('>')
            self.emoji_label2.setText('📄')

        elif player == "scissors" and computer == "rock":
            self.description_label.setText("You lose!")
            self.emoji_label1.setText('✂️')
            self.emoji_label3.setText('<')
            self.emoji_label2.setText('🪨')

        elif player == "rock" and computer == "paper":
            self.description_label.setText("You lose!")
            self.emoji_label1.setText('🪨')
            self.emoji_label3.setText('<')
            self.emoji_label2.setText('📄')

        elif player == "paper" and computer == "scissors":
            self.description_label.setText("You lose!")
            self.emoji_label1.setText('📄')
            self.emoji_label3.setText('<')
            self.emoji_label2.setText('✂️')
        

        #play_again = input("Play again? (y/n): ").lower()
        #if not play_again == "y":

        self.game_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = RockPapersScissors()
    game.show()
    sys.exit(app.exec_())

