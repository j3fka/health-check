from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
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
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
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
        self.v_layout_1.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_starttest3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hinttest2, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_hinttest3, alignment=Qt.AlignLeft)
        self.v_layout_1.addWidget(self.txt_sendresults, alignment=Qt.AlignCenter)

        self.v_layout_2.addWidget(self.timer, alignment=Qt.AlignCenter)
        self.timer.hide()

        self.h_layout_1.addLayout(self.v_layout_1)
        self.h_layout_1.addLayout(self.v_layout_2)
    

        self.setLayout(self.h_layout_1)

    def test_1(self):
        self.timer.show()
        global time
        time = QTime(0, 0, 15)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: black')
        self.timer_for_test_1 = QTimer()
        self.timer_for_test_1.timeout.connect(self.tick_1)
        self.timer_for_test_1.start(1000)

    def tick_1(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer_for_test_1.stop()

    def test_2(self):
        self.timer.show()
        global time
        time = QTime(0, 0, 30)
        self.timer.setText(time.toString('hh:mm:ss')[-2:])
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: black')
        self.timer_for_test_2 = QTimer()
        self.timer_for_test_2.timeout.connect(self.tick_2)
        self.timer_for_test_2.start(1500)
    
    def tick_2(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss')[-2:])
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer_for_test_2.stop()

    def test_3(self):
        self.timer.show()
        global time
        time = QTime(0, 1, 0)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: green')
        self.timer_for_test_3 = QTimer()
        self.timer_for_test_3.timeout.connect(self.tick_3)
        self.timer_for_test_3.start(1000)

    def tick_3(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss')[-2:] == '15':
            self.timer.setStyleSheet('color: green')
        if time.toString('hh:mm:ss')[-2:] == '45':
            self.timer.setStyleSheet('color: black')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer_for_test_3.stop()
    

    def connects(self):
        self.txt_sendresults.clicked.connect(self.nextwin)
        self.txt_starttest1.clicked.connect(self.test_1)
        self.txt_starttest2.clicked.connect(self.test_2)
        self.txt_starttest3.clicked.connect(self.test_3)
    def nextwin(self):
        self.hide()
        self.lw = LastWin(self.txt_hintage.text(), self.txt_hinttest1.text(), self.txt_hinttest2.text(), self.txt_hinttest3.text())
