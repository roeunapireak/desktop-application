from PyQt5.QtWidgets import (
    QApplication, QWidget
)
app = QApplication([])

window = QWidget()

window.setWindowTitle('Desktop Applicatin')

window.show()
app.exec_()