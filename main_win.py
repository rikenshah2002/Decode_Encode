# Main Window
# It allows user to select what operation they want to do.

from PyQt5 import QtWidgets, uic
import Encode
import Decode

app_gui = QtWidgets.QApplication([])

win_first = uic.loadUi("Main_win.ui")
win_first.show()


def Encoder():

    Encode.dlg.show()
    Encode.app_gui.exec()
    win_first.hide()


def Decode1():
    Decode.dlg.show()
    Decode.app_gui.exec()
    win_first.hide()


def get_back():
    Encode.dlg.hide()
    win_first.show()


def get1_back():
    Decode.dlg.hide()
    win_first.show()


win_first.Encode.clicked.connect(Encoder)

win_first.Decode.clicked.connect(Decode1)

Encode.dlg.go_back.clicked.connect(get_back)

Decode.dlg.go_back.clicked.connect(get1_back)

app_gui.exec()
