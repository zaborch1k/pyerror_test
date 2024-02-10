from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.show()
        self.initUI()
        self.connects()
    def set_win(self):
        self.setWindowTitle("Тест Руфхехйъ")
        self.resize(600,500)
    def initUI(self):
        self.greetings=QLabel("Тест \"Какая ты ошибка из Python\"")
        self.desc=QLabel("Приветствую Вас, товарищи разработчики! Вы считаете свою жизнь ошибкой? Этот тест именно для Вас! Пройдя его, вы узнаете, какой именно ошибкой вы являетесь!")
        self.next=QPushButton("Начать Тест")
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.greetings)
        self.lay.addWidget(self.desc)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)
    def connects(self):
        self.next.clicked.connect(self.moveupoo)
    def moveupoo(self):
        self.hide()
        self.nxt_screen=SecondScreen()
app=QApplication([])
my_app=FirstScreen()
app.exec() 
