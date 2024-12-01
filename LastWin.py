from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from instr import *

class LastWin(QWidget):
    def __init__(self, age, result_1, result_2, result_3):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

        self.age = age
        self.result_1 = result_1
        self.result_2 = result_2
        self.result_3 = result_3
    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
    def initUI(self):
        pass
