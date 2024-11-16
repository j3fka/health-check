from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MainWin(QWidget):
    def __init__():
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.resize(600, 400)
        self.setWindowTitle('Health Check')
        self.move()