from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic



def button_clicked():
    experiment.do_scan()


app = QApplication([])
win = QMainWindow()

uic.loadUi('/home/aquiles/Documents/ZZP/Delft/PythonForTheLab/main_window.ui', win)

def other_action():
    if win.start_button.text() == 'Start':
        win.start_button.setText('New Start')
    else:
        win.start_button.setText('Start')


win.start_button.clicked.connect(button_clicked)
win.stop_button.clicked.connect(button_clicked)
win.start_button.clicked.connect(other_action)


win.show()
app.exit(app.exec_())

