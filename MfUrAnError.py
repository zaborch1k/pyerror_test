from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from text import *

class ThirdScreen(QWidget):
    def __init__(self, ans):
        super().__init__()
        self.ans = ans
        self.set_win()
        self.initUI()
        self.show()

    def set_win(self):
        self.setWindowTitle("Вывод🤠")
        self.resize(600,500)

    def initUI(self):
        self.ans1=QLabel("Мы выяснили что у вас есть несколько проблем:")
        self.res=QLabel(self.counter())
        self.ans2=QLabel("Шизофрения, депрессия, умственная отсталось")
        

        self.lay=QVBoxLayout()
        self.lay.addWidget(self.ans1)
        self.lay.addWidget(self.res)
        self.lay.addWidget(self.ans2)

        self.setLayout(self.lay) 

    def counter(self):
        ans = [self.ans.count(1), self.ans.count(2), self.ans.count(3), self.ans.count(4)]
        num = max(ans)
        
        if ans.count(num) < 1:
            a = ans_list[num-1]
        else:
            a = ans_list[-1]
        return a
        

        



if __name__ == '__main__':
    app=QApplication([])
    my_app=ThirdScreen()
    app.exec() 
