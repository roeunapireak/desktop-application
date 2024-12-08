from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QHBoxLayout, # Herizontal layout
    QVBoxLayout, # vertical layout 
    QRadioButton, 
    QMessageBox
)


app = QApplication([])

window = QWidget()

window.setWindowTitle('Desktop Applicatin')
window.resize(400, 200)
window.move(900, 70)

question = QLabel('what programming langauge do you learn?')
# winner = QLabel('?')
gen_bottun = QPushButton('Generate')

answer_1 = QRadioButton('C+++')
answer_2 = QRadioButton('Python')
answer_3 = QRadioButton('Java')
answer_4 = QRadioButton('Java script')


main_v_line = QVBoxLayout()

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()
h_line_4 = QHBoxLayout()
h_line_5 = QHBoxLayout()

h_line_1.addWidget(question, alignment=Qt.AlignCenter)
# h_line_2.addWidget(winner, alignment=Qt.AlignCenter)
h_line_3.addWidget(gen_bottun, alignment=Qt.AlignCenter)

h_line_4.addWidget(answer_1, alignment=Qt.AlignCenter)
h_line_4.addWidget(answer_2, alignment=Qt.AlignCenter)
h_line_5.addWidget(answer_3, alignment=Qt.AlignCenter)
h_line_5.addWidget(answer_4, alignment=Qt.AlignCenter)


main_v_line.addLayout(h_line_1)
# main_v_line.addLayout(h_line_2)
main_v_line.addLayout(h_line_4)
main_v_line.addLayout(h_line_5)
main_v_line.addLayout(h_line_3)

window.setLayout(main_v_line)


def show_winner():
    print('function is call.')

gen_bottun.clicked.connect(show_winner)

window.show()
app.exec_()