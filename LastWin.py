from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *
from matan import *


class LastWin(QWidget):
    def __init__(self, age, result_1, result_2, result_3):
        self.age = age
        self.result_1 = result_1
        self.result_2 = result_2
        self.result_3 = result_3

        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
    def initUI(self):
        index_r, be = compare(self.result_1, self.result_2, self.result_3, self.age)
        self.v_layout = QVBoxLayout()
        self.index = QLabel(f'Индекс Руфье: {index_r}')
        self.preferably = QLabel(f'Работоспособность сердца: {be}')

        self.v_layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.v_layout.addWidget(self.preferably, alignment = Qt.AlignCenter)
        self.setLayout(self.v_layout)



