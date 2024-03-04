# main file
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class MainScreen(QWidget):
    def __init__(self, wins):
        super().__init__()
        self.wins = wins
        self.set_win()
        self.show()
        self.initUI()
        self.connects()

    def set_win(self):
        self.setWindowTitle("Тест Pyфхехйъ")
        self.resize(600,500)

    def initUI(self):
        self.greetings=QLabel("Тест \"Какая ты ошибка из Python\"")
        self.desc=QLabel("Приветствую Вас, товарищи разработчики! Вы считаете свою жизнь ошибкой?\nЭтот тест именно для Вас! Пройдя его, вы узнаете, какой именно ошибкой вы являетесь!")
        
        self.next_butt=QPushButton("Начать Тест")

        self.lay=QVBoxLayout()

        self.lay.addWidget(self.greetings)
        self.lay.addWidget(self.desc)
        self.lay.addWidget(self.next_butt)

        self.setLayout(self.lay)

    def connects(self):
        self.next_butt.clicked.connect(self.moveupoo)

    def moveupoo(self):
        self.win = self.wins[0]
        self.close()
        self.go_next()
        del self.wins[0]
        
    def go_next(self):
        self.win.show_me(self.wins, None)


app=QApplication([])

from quests_wins import Win
wins = [Win('1'), Win('2'), Win('3'), Win('4')]

main_win = MainScreen(wins)
app.exec()
