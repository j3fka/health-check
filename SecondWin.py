from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_name = QLabel(txt_name)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.txt_hintage = QLineEdit(txt_hintage)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest3 = QLabel(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.txt_name)
        self.layout.addWidget(self.txt_hintname)
        self.layout.addWidget(self.txt_age)
        self.layout.addWidget(self.txt_hintage)
        self.layout.addWidget(self.txt_test1)
        self.layout.addWidget(self.txt_starttest1)
        self.layout.addWidget(self.txt_hinttest1)
        self.layout.addWidget(self.txt_test2)
        self.layout.addWidget(self.txt_starttest2)
        self.layout.addWidget(self.txt_hinttest2)
        self.layout.addWidget(self.txt_test3)
        self.layout.addWidget(self.txt_starttest3)
        self.layout.addWidget(self.txt_hinttest3)
        self.layout.addWidget(self.txt_sendresults)
    

        self.setLayout(self.layout)
        
    def connects(self):
        pass

