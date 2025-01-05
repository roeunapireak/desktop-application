
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        self.exp = exp