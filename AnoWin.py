# To show output of Encoded Text

from PyQt5 import QtWidgets, uic
app2_gui = QtWidgets.QApplication([])
dlg2 = uic.loadUi("AnoWindow.ui")


def Show_Encode(text):
    dlg2.show_me.setText(text)
