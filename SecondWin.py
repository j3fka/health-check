from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from instr import *
from LastWin import LastWin

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

        self.timer = QLabel('0:00:15')

        self.v_layout_1 = QVBoxLayout()
        self.v_layout_2 = QVBoxLayout()
        self.h_layout_1 = QHBoxLayout()

        self.v_layout_1.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hintname, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hintage, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_starttest1, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hinttest1, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_test2, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_starttest2, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hinttest2, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_starttest3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hinttest3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_sendresults, alignment=Qt.AlignLeft)

        self.v_layout_2.addWidget(self.timer, alignment=Qt.AlignCenter)

        self.h_layout_1.addLayout(self.v_layout_1)
        self.h_layout_1.addLayout(self.v_layout_2)
    

        self.setLayout(self.h_layout_1)
        
    def connects(self):
        self.txt_sendresults.clicked.connect(self.nextwin)
    def nextwin(self):
        self.hide()
        self.lw = LastWin()

