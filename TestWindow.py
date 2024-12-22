from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
        QPushButton, QApplication, QHBoxLayout, QGroupBox, 
        QRadioButton, QListWidget, QLineEdit)

from txt_and_var import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.sendresult_btn = QPushButton(sendresult_txt, self)

    def connects(self):
        pass

    def set_appear(self):
        pass
