import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,
)
from PyQt5.QtGui import  QStandardItem, QStandardItemModel
from PyQt5.uic import loadUi
from PyQt5 import QtCore


from teste import Ui_Dialog

class Window(QMainWindow, Ui_Dialog):
    model = QStandardItemModel()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def guardar_list_nomes(self):
        print(self.textEdit.toPlainText())
        dwd = QStandardItem(self.textEdit.toPlainText())
        dwd.setCheckable(True)
        self.model.appendRow(dwd)
        self.listView.setModel(self.model)
    
    
    def apagar_list_nomes(self):
        mod = self.listView.model()
        toRem = []
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                toRem.append(it.row())
                

        for x in toRem:
            mod.removeRow(x)

    def connectSignalsSlots(self):
        self.Executar.clicked.connect(self.btn_Executar_click)
        self.Delete.clicked.connect(self.btn_Apagar_Click)
    
    def btn_Executar_click(self):
        self.guardar_list_nomes()

    def btn_Apagar_Click(self):
        self.apagar_list_nomes()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())