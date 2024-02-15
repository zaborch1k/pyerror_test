# window of first quest

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtGui import QIcon

from text import *


class Quest(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.set_win()
        self.initUI()
        self.connects()
        self.show()

    def set_win(self):
        self.setWindowTitle(f"{self.name}")
        self.resize(600,500)

    def initUI(self):
        self.greetings = QLabel(q1)
        self.next = QPushButton("")

        self.rbutt1 = QRadioButton(text)
        self.rbutt2 = QRadioButton(text)
        self.rbutt3 = QRadioButton(text)
        self.rbutt4= QRadioButton(text)
        self.button = QPushButton('Ответить')

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.rbutt1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.rbutt4, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button, alignment=Qt.AlignLeft)

        self

        self.setLayout(self.lay)


    def connects(self):
        self.next.clicked.connect(self.to_second)

    def to_second(self, win):
        self.hide()
        self.next_screen = win

app = QApplication([])
app.exec()

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