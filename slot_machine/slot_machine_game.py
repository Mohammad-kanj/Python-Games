#Python Slot Machine

import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class SlotMachine(QWidget):
    def __init__(self, initial_balance=100):
        super().__init__()
        self.balance = initial_balance
        self.balance_label = QLabel(f"Your Balance is :  ${str(self.balance)}", self)
        self.slot_input = QLineEdit(self)
        self.spin_slots = QPushButton("Spin slots", self)
        self.amount = QLabel(f"Amount to play:", self)
        self.emoji_label1 = QLabel(self)
        self.emoji_label2 = QLabel(self)
        self.emoji_label3 = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):

        
        self.setWindowTitle("Slot Machine game")
        self.move(650, 250)
        self.setFixedSize(700, 600)

        vbox = QVBoxLayout()

        vbox.addWidget(self.balance_label)

        hbox1 = QHBoxLayout() 
        hbox1.addWidget(self.amount)
        hbox1.addWidget(self.slot_input)
    
        vbox.addLayout(hbox1)

        vbox.addWidget(self.spin_slots)

        hbox2 = QHBoxLayout() 
        hbox2.addWidget(self.emoji_label1)
        hbox2.addWidget(self.emoji_label2)
        hbox2.addWidget(self.emoji_label3)


        vbox.addLayout(hbox2)

        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.balance_label.setAlignment(Qt.AlignCenter)
        self.slot_input.setAlignment(Qt.AlignCenter)
        self.amount.setAlignment(Qt.AlignCenter)
        self.emoji_label1.setAlignment(Qt.AlignCenter)
        self.emoji_label2.setAlignment(Qt.AlignCenter)
        self.emoji_label3.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.balance_label.setObjectName("balance_label")
        self.slot_input.setObjectName("slot_input")
        self.amount.setObjectName("amount")
        self.spin_slots.setObjectName("spin_slots")
        self.emoji_label1.setObjectName("emoji_label1")
        self.emoji_label2.setObjectName("emoji_label2")
        self.emoji_label3.setObjectName("emoji_label3")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
            }
            QLabel, QPushButton{
                color: #f8fafc;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#balance_label{
                font-size: 42px;
                font-weight: 800;
                color: #22c55e; 
                margin: 15px;
                letter-spacing: 1px;
            }
            QLabel#amount{
                font-size: 22px;
                font-weight: 800;
                color: #ffffff;
                margin: 15px;
                letter-spacing: 1px;
            }
            QLineEdit#slot_input{
                font-size: 32px;
                padding: 5px;
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 12px;
                color: #ffffff;
                margin: 10px 10px;
            }
            QLineEdit#slot_input:focus {
                border: 2px solid #3b82f6;
            }
            QPushButton#spin_slots{
                font-size: 26px;
                font-weight: bold;
                background-color: #3b82f6;
                color: white;
                border-radius: 15px;
                padding: 15px;
                margin: 10px 100px;
                border-bottom: 4px solid #1d4ed8;
            }
            QPushButton#spin_slots:hover {
                background-color: #60a5fa;
            }
            QPushButton#spin_slots:pressed {
                border-bottom: 0px;
                margin-top: 14px;
            }
            QLabel#emoji_label1{
                font-size: 110px;
                background-color: #1e293b;
                border-radius: 20px;
                margin: 5px;
                padding: 20px;
                border: 1px solid #334155;
            }
            QLabel#emoji_label2{
                font-size: 110px;
                background-color: #1e293b;
                border-radius: 20px;
                margin: 5px;
                padding: 20px;
                border: 1px solid #334155;
            }
            QLabel#emoji_label3{
                font-size: 110px;
                background-color: #1e293b;
                border-radius: 20px;
                margin: 5px;
                padding: 20px;
                border: 1px solid #334155;
            }
            QLabel#description_label{
                font-size: 36px;
                font-weight: bold;
                color: #94a3b8;
                margin-top: 20px;
            }
        """)

        self.spin_slots.clicked.connect(self.spin_row)

    def spin_row(self):
        symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

        try:
            bet_text = self.slot_input.text()
            bet = int(bet_text)
        except ValueError:
            self.description_label.setText("Enter a valid bet!!")
            return

        if bet > self.balance or bet < 1:
            self.description_label.setText("Insufficient Funds!!")
            return

        res1 = random.choice(symbols)
        res2 = random.choice(symbols)
        res3 = random.choice(symbols)

        self.emoji_label1.setText(res1)
        self.emoji_label2.setText(res2)
        self.emoji_label3.setText(res3)

        row = [res1, res2, res3]
        payout = self.get_payout(row, bet)

        self.balance -= bet
        self.balance += payout
        self.balance_label.setText(f"Your Balance is : ${self.balance}")

        if payout > 0:
            self.description_label.setText(f"WINNER! +${payout}")
        else:
            self.description_label.setText("You Lost. Try again!!")

    def get_payout(self, row, bet):
        if row[0] == row[1] == row[2]:
            if row[0] == '🍒':
                return bet * 3
            elif row[0] == '🍉':
                return bet * 4
            elif row[0] == '🍋':
                return bet * 5
            elif row[0] == '🔔':
                return bet * 10
            elif row[0] == '⭐':
                return bet * 20
        return 0 


if __name__ == "__main__":
    starting_money = 100
    app = QApplication(sys.argv)
    slot_machine = SlotMachine()
    slot_machine.show()
    sys.exit(app.exec_())