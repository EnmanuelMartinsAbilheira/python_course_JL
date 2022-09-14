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
    model2 = QStandardItemModel()
    toUpdate = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.label.setText("0")
        self.label_2.setText("0")

    def guardar_list_nomes(self):
        if self.toUpdate != None:
            self.toUpdate.setText(self.textEdit.toPlainText())
            self.textEdit.setText('')
            self.toUpdate = None
            return

        print(self.textEdit.toPlainText())
        dwd = QStandardItem(self.textEdit.toPlainText())
        dwd.setCheckable(True)
        self.model.appendRow(dwd)
        self.listView.setModel(self.model)
        
    
    
    def btn_der(self):
        mod = self.listView.model()
        if mod == None:
            return
        toRem = []
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                toRem.append(it)
                
        for x in toRem:
            k = x.text()
            mod.removeRow(x.row())
            self.listView.setModel(mod)
            mod2 = self.listView_2.model()
            if mod2 == None:
                mod2 = self.model2
            dwd = QStandardItem(k)
            dwd.setCheckable(True)
            mod2.appendRow(dwd)
            self.listView_2.setModel(mod2)


    def btn_izq(self):
        mod2 = self.listView_2.model()
        if mod2 == None:
            return
        toRem = []
        for r in range(mod2.rowCount()):
            it = mod2.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                toRem.append(it)
                
                
        for x in toRem:
            k = x.text()
            mod2.removeRow(x.row())
            self.listView_2.setModel(mod2)
            mod = self.listView.model()
            if mod == None:
                mod = self.model
            dwd = QStandardItem(k)
            dwd.setCheckable(True)
            mod.appendRow(dwd)
            self.listView.setModel(mod)


    
    def btn_delete(self):
        mod = self.listView.model()
        mod2 = self.listView_2.model()

        if self.toUpdate != None:
            self.textEdit.setText('')
            self.toUpdate = None
            return

        if mod == None:
            mod = self.model
        if mod2 == None:
            mod2 = self.model2

        toRem1 = []
        toRem2 = []
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                toRem1.append(it)

        for x in toRem1:
            mod.removeRow(x.row())

        self.listView.setModel(mod)

        for d in range (mod2.rowCount()):
            it = mod2.item(d)
            if it != None and it .checkState() == QtCore.Qt.Checked:
                toRem2.append(it)
        for x in toRem2:
            mod2.removeRow(x.row())    
        
        self.listView_2.setModel(mod2)


    def btn_editar_text(self):
        mod = self.listView.model()
        mod2 = self.listView_2.model()
                       
        self.textEdit.setText('')
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                self.textEdit.setText(it.text())
                self.toUpdate = it
                return
                
        for d in range (mod2.rowCount()):
            it = mod2.item(d)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                self.textEdit.setText(it.text())
                self.toUpdate = it 
                return


    def updateListCount(self):
        mod = self.listView.model()
        mod2 = self.listView_2.model()
        
        if mod != None:
            self.label.setText(str(mod.rowCount()))
        if mod2 != None:
            self.label_2.setText(str(mod2.rowCount()))

    def connectSignalsSlots(self):
        self.Executar.clicked.connect(self.btn_Executar_click)
        self.Executar_der.clicked.connect(self.btn_Der_Click)
        self.Executar_izq.clicked.connect(self.btn_Izq_Click)
        self.Delete.clicked.connect(self.btn_Delete)
        self.Editar.clicked.connect(self.btn_Editar)
    
    def btn_Executar_click(self):
        self.guardar_list_nomes()
        self.updateListCount()

    def btn_Der_Click(self):
        self.btn_der()
        self.updateListCount()

    def btn_Izq_Click(self):
        self.btn_izq()
        self.updateListCount()
    
    def btn_Delete(self):
        self.btn_delete()
        self.updateListCount()

    def btn_Editar(self):
        self.btn_editar_text()
        self.updateListCount()
                       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
