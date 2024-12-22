from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QApplication)

from txt_and_var import *
from TestWindow import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.next_click()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.start_btn = QPushButton(start_txt, self)
        self.welcome_txt = QLabel(welcome_txt)
        self.instruction_txt = QLabel(instruction_txt)
        
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.welcome_txt, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction_txt, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.start_txt, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    def next_click(self):
        self.test_window = TestWin()
        self.hide()

    def connects(self):
        self.start_btn.clicked.connect(self.next_click)
    
    def set_appear(self):
        self.setWindowTitle('Health')
        self.resize(window_width, window_height)
        self.move(window_x, window_y)


app = QApplication([])
main_window = MainWin()
app.exec_()
