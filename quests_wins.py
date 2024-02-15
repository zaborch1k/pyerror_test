# window of first quest

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtGui import QIcon

from text import *


class Win(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def show_me(self, wins):
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
        self.rbutt2 = QRadioButton(text)
        self.rbutt3 = QRadioButton(text)
        self.rbutt4= QRadioButton(text)
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
        #win = self.wins[0]
        #self.hide()
        #self.next_screen = win
        print('*next*')


if __name__ == '__main__':
    app = QApplication([])

    win = Win('gfhfghfghhfhg')
    win.show_me('hhhhhh')

    app.exec()


'''
label1 = QLabel('text1')
v_line = QVBoxLayout()

v_line.addWidget(label1, alignment=Qt.AlignLeft)
v_line.addWidget(rbutt1, 3, alignment=Qt.AlignLeft)
v_line.addWidget(rbutt2, alignment=Qt.AlignLeft)
v_line.addWidget(rbutt3, alignment=Qt.AlignLeft)
v_line.addWidget(rbutt4, alignment=Qt.AlignLeft)

v_line.addWidget(button, alignment=Qt.AlignCenter)


button.clicked.connect(next_quest)
my_win.setLayout(v_line)


my_win.show()
app.exec_()
'''