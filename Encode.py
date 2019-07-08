# GUI to Encode

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import App
import AnoWin


def to_show(text):
    dlg.go_back.clicked.connect(text)


def error():
    QMessageBox.information(None, "Invalid Input", "Enter Something")


def go_back():
    AnoWin.dlg2.hide()
    dlg.show()


def Run_Encode():
    app =App.Main()
    if dlg.input_01.text() is not "":
        encoded = app.to_encode(dlg.input_01.text())
        # print(str(dlg.input_01.text()))
        # print(encoded)
        sec_win = AnoWin
        sec_win.dlg2.show()
        dlg.input_01.setText(None)
        sec_win.Show_Encode(encoded)
        dlg.hide()
        AnoWin.app2_gui.exec()
    else:
        error()


app_gui = QtWidgets.QApplication([])
dlg = uic.loadUi("encode.ui")

dlg.input_01.setFocus()
dlg.input_01.returnPressed.connect(Run_Encode)
dlg.logic.clicked.connect(Run_Encode)
AnoWin.dlg2.pushButton.clicked.connect(go_back)
