from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from SecondWin import SecondWin

class MainWin(QWidget):
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
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.btn_txt_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_hello)
        self.layout.addWidget(self.txt_instruction)
        self.layout.addWidget(self.btn_txt_next)
        self.setLayout(self.layout)
    def connects(self):
        self.btn_txt_next.clicked.connect(self.nextwin)
    def nextwin(self):
        self.hide()
        self.sw = SecondWin()
        


app = QApplication([])
mw = MainWin()
app.exec_()