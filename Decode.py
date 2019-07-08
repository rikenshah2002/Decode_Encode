# GUI to Decode

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import App
import AnoWIn2


def error1():
    QMessageBox.information(None, "Empty Input", "Enter Something")


def error2():
    QMessageBox.information(None, "Invalid Input", "Input valid sentence/word")


def go_back():
    AnoWIn2.dlg2.hide()
    dlg.show()


def Run_Decode():

    app = App.Main()
    try:
        if dlg.logic.text() is not "":
            encoded = app.to_decode(dlg.logic.text())
            # print(encoded)
            sec_win = AnoWIn2
            sec_win.dlg2.show()
            dlg.logic.setText(None)
            sec_win.Show_Encode(encoded)
            dlg.hide()
            AnoWIn2.app2_gui.exec()
        else:
            error1()
    except Exception:
        error2()


app_gui = QtWidgets.QApplication([])
dlg = uic.loadUi("decode.ui")

dlg.logic.setFocus()
dlg.logic.returnPressed.connect(Run_Decode)
dlg.decode_it.clicked.connect(Run_Decode)


AnoWIn2.dlg2.pushButton.clicked.connect(go_back)
