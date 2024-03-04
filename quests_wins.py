# questions' windows

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon

from MfUrAnError import ThirdScreen

from text import *


class Win(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def show_me(self, wins, ans):
        self.ans = ans
        self.wins = wins
        self.set_win()
        self.initUI()
        self.connects()
        self.show()
    
    def set_win(self):
        self.setWindowTitle(f"{self.name}")
        self.resize(600,500)

    def initUI(self):
        text = 'dffffffffffffffffg'
        self.greetings = QLabel(q1)
        self.next = QPushButton("")

        self.rbutt1 = QRadioButton(text)
        self.rbutt1.setChecked(True)
        self.rbutt2 = QRadioButton(text)
        self.rbutt3 = QRadioButton(text)
        self.rbutt4= QRadioButton(text)

        self.rbuttgroup = QButtonGroup()
        self.rbuttgroup.addButton(self.rbutt1, id = 1)
        self.rbuttgroup.addButton(self.rbutt2, id = 2)
        self.rbuttgroup.addButton(self.rbutt3, id = 3)
        self.rbuttgroup.addButton(self.rbutt4, id = 4)

        self.next_butt = QPushButton('Ответить')

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.rbutt1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt4, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.next_butt, alignment=Qt.AlignLeft)

        self.setLayout(self.lay)

    def connects(self):
        self.next_butt.clicked.connect(self.to_next)

    def to_next(self):
        if not self.ans:
            self.ans = list()
        
        self.ans.append(self.rbuttgroup.checkedId())
        self.close()

        if not len(self.wins) <1:
            self.next_screen = self.wins[0]
            del self.wins[0]
            self.next_screen.show_me(self.wins, self.ans)
        else:
            self.win = ThirdScreen(self.ans)
        
    

if __name__ == '__main__':
    app = QApplication([])

    win = Win('gfhfghfghhfhg')
    win.show_me('hhhhhh')

    app.exec()
