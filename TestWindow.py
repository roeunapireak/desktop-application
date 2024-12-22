from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit,
        QPushButton, QApplication, QHBoxLayout, QGroupBox, 
        QRadioButton, QListWidget)

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
        self.starttest_btn_1 = QPushButton(starttest_txt_1, self)
        self.starttest_btn_2 = QPushButton(starttest_txt_2, self)
        self.starttest_btn_3 = QPushButton(starttest_txt_3, self)

        self.text_name = QLabel(name_txt)
        self.text_age = QLabel(age_txt)
        self.text_test1 = QLabel(test_txt_1)
        self.text_test2 = QLabel(test_txt_1)
        self.text_test3 = QLabel(test_txt_1)
        self.text_timer = QLabel(timer_txt)

        self.line_name = QLineEdit('Full name')
        self.line_age = QLineEdit('0')
        self.line_test_1 = QLineEdit('0')
        self.line_test_2 = QLineEdit('0')
        self.line_test_3 = QLineEdit('0')
        

    def connects(self):
        pass

    def set_appear(self):
        pass
