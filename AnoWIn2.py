# To show output of Decoded Text

from PyQt5 import QtWidgets, uic
app2_gui = QtWidgets.QApplication([])
dlg2 = uic.loadUi("Anowin2.ui")


def Show_Encode(text):
    dlg2.show_me.setText(text)
