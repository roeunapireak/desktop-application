
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.connects()
        self.set_appear()

        self.show()

    def set_appear(self):
        self.setWindowTitle('Health')
        self.resize(window_widht, window_height)
        self.move(window_x, window_y)

    def initUI(self):
        self.sendresult_btn = QPushButton(sendresult_txt, self)
        self.start_test_1_btn = QPushButton(start_test_1, self)
        self.start_test_2_btn = QPushButton(start_test_2, self)
        self.start_test_3_btn = QPushButton(start_test_3, self)

        self.name_txt = QLabel(name_txt, self)
        self.age_txt = QLabel(age_txt, self)
        self.timer_txt = QLabel(timer_txt, self)
        self.test_txt_1 = QLabel(test_txt_1, self)
        self.test_txt_2 = QLabel(test_txt_2, self)
        self.test_txt_3 = QLabel(test_txt_3, self)

        self.name_line = QLineEdit(hint_test_name)
        self.hint_test_age = QLineEdit(hint_test_age)
        self.hint_test_1 = QLineEdit(hint_test_1)
        self.hint_test_2 = QLineEdit(hint_test_2)
        self.hint_test_3 = QLineEdit(hint_test_3)

        self.l_v_line = QVBoxLayout()
        self.r_v_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.r_v_line.addWidget(self.timer_txt, alignment=Qt.AlignCenter)
        self.l_v_line.addWidget(self.name_txt, alignment=Qt.AlignLeft)
        self.l_v_line.addWidget(self.name_line, alignment=Qt.AlignLeft)
        
        ##
        self.h_line.addLayout(self.l_v_line)
        self.setLayout(self.h_line)
        

