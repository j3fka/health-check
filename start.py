from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
win = QWidget()
win.resize(600, 400)
win.setWindowTitle('')

win.show()
app.exec_()