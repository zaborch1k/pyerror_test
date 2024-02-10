from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
class ThirdScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.show()
        self.initUI()
    def set_win(self):
        self.setWindowTitle("Вывод🤠")
        self.resize(600,500)
    def initUI(self):
        self.ans1=QLabel("Мы выяснили что у вас есть несколько проблем:")
        self.ans2=QLabel("Шизофрения, депрессия, умственная отсталось")
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.ans1)
        self.lay.addWidget(self.ans2)
        self.setLayout(self.lay) 
app=QApplication([])
my_app=ThirdScreen()
app.exec() 
