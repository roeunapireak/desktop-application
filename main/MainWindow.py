
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QApplication
from instr import *
from TestWindow import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.connects()
        self.set_appear()

        self.show()

    def initUI(self):
        self.start_btn = QPushButton('Start', self)
        self.welcome_txt = QLabel(welcome_txt, self)
        self.instrunction_txt = QLabel(instrunction_txt, self)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.welcome_txt, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instrunction_txt, alignment=Qt.AlignLeft)  
        self.layout_line.addWidget(self.start_btn, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def connects(self):
        self.start_btn.clicked.connect(self.next_click)

    def next_click(self):
        self.test_window = TestWin()
        self.hide()

    def set_appear(self):
        self.setWindowTitle('Health')
        self.resize(window_widht, window_height)
        self.move(window_x, window_y)


app = QApplication([])
window = MainWin()

app.exec_()