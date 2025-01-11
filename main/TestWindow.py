
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from instr import *
from FinalWindow import FinalWin

class Experiment():
   def __init__(self, age, test1, test2, test3):
       self.age = age
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3

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
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
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
        self.l_v_line.addWidget(self.age_txt, alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.hint_test_age, alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.test_txt_1 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.start_test_1_btn , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.hint_test_1 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.test_txt_2 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.start_test_2_btn , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.hint_test_2 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.test_txt_3 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.start_test_3_btn , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.hint_test_3 , alignment = Qt.AlignLeft)
        self.l_v_line.addWidget(self.sendresult_btn , alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_v_line)
        self.h_line.addLayout(self.r_v_line)
        self.setLayout(self.h_line)
        
    def click_next(self):
        self.hide()
        self.exp = Experiment(age=int(self.hint_test_age.text()), 
                              test1=self.hint_test_1.text(), 
                              test2=self.hint_test_2.text(), 
                              test3=self.hint_test_3.text())
        self.final_result = FinalWin(exp=self.exp)

    def time_test(self):
        global time
        time = QTime(0, 0, 15) # https://doc.qt.io/qtforpython-5/PySide2/QtCore/QTime.html#
        self.timer = QTimer() # https://doc.qt.io/qtforpython-5/PySide2/QtCore/QTimer.html
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1) # https://doc.qt.io/qtforpython-5/PySide2/QtCore/QTime.html#PySide2.QtCore.PySide2.QtCore.QTime.addSecs
        self.timer_txt.setText(time.toString("hh:mm:ss"))
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500) #one squat in 1.5 seconds

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss")[6:8]) #[6:8] convert from "hh:mm:ss" to be "ss"
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_txt.setStyleSheet("color: rgb(0,255,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timer_txt.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer_txt.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def connects(self):
        self.sendresult_btn.clicked.connect(self.click_next)
        self.start_test_1_btn.clicked.connect(self.time_test)
        self.start_test_2_btn.clicked.connect(self.timer_sits)
        self.start_test_3_btn.clicked.connect(self.timer_final)