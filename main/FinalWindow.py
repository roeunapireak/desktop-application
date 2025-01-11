
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        self.exp = exp

        self.set_appear()
        self.initUI()

        self.show()

    def set_appear(self):
        self.setWindowTitle('Result')
        self.resize(window_widht, window_height)
        self.move(window_x, window_y)
    
    def initUI(self):
        self.work_text = QLabel('Cardiac performance: ' + '0')
        self.index_text = QLabel('Roufier Index: ' + '0')

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)

