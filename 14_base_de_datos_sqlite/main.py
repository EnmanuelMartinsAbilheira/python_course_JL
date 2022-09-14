import sys
import sqlite3
import os

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,
)
from PyQt5.QtGui import  QStandardItem, QStandardItemModel
from PyQt5.uic import loadUi
from PyQt5 import QtCore


from teste import Ui_Dialog

class Database():
                   
    SQLiteDatabase = "SQLite.db"

    @staticmethod
    def querySQL(query):
        conn = sqlite3.connect(Database.SQLiteDatabase)
        c = conn.cursor()
        x = None
        try:
            x = c.execute(query)
            conn.commit()
        except Exception as e:
            print(e)
        return x
    
    @staticmethod
    def criar_tabela():
        Database.querySQL('''
            CREATE TABLE IF NOT EXISTS contacto (
                Id integer PRIMARY KEY AUTOINCREMENT,
                Nome text NOT NULL
            );
        ''') 

class Window(QMainWindow, Ui_Dialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        Database.criar_tabela()
        self.setupUi(self)
        self.connectSignalsSlots()
        self.Total.setText("0")
        self.Id_Seleccionado.setText("0")


    model = QStandardItemModel()

    def guardar_list_nomes(self):
        conn = sqlite3.connect('SQLite.db')
        curser= conn.cursor()
        curser.execute("SELECT Nome FROM contacto")
        hu= curser.fetchall()
        self.model = QStandardItemModel()
        for i in range(len(hu)):         
            dwd = QStandardItem(hu[i][0])
            dwd.setCheckable(True)
            self.model.appendRow(dwd)
            self.listView.setModel(self.model)
        
        
    
    def criar_pessoa_DB(self):
        Database.querySQL("INSERT INTO contacto(Nome) Values('" + str(self.textEdit.toPlainText()) + "')")
        
        self.model = QStandardItemModel()
        
        self.guardar_list_nomes()

    def eliminar_pessoa(self):
        
        mod = self.listView.model()

        if mod == None:
            mod = self.model
        
        toRem1 = []
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if it != None and it.checkState() == QtCore.Qt.Checked:
                toRem1.append(it)
        
        for x in toRem1:

            conn = sqlite3.connect('SQLite.db')
            curser= conn.cursor()
           
            curser.execute("SELECT id FROM contacto where Nome = '" + x.text() + "'")

            hu= curser.fetchall()
            for i in range(len(hu)): 
                id = hu[i][0]
                print("delete from contacto where id=" + str(id))
                curser.execute("delete from contacto where id=" + str(id))
                conn.commit()

            mod.removeRow(x.row())
        
        self.listView.setModel(mod)

        self.model = QStandardItemModel()

    def updateListCount(self):
        mod = self.listView.model()
    
        if mod != None:
            self.Total.setText(str(mod.rowCount()))
                           
    def Id_Seleccionado_func(self):
        
        mod = self.listView.model()
        index = self.listView.currentIndex().row()
        it =  mod.item(index)
        nome = it.text()

        #chamar base de dados 
        conn = sqlite3.connect('SQLite.db')
        curser= conn.cursor()
        curser.execute("SELECT id FROM contacto where Nome = '" + nome + "'")
        hu= curser.fetchall()
        for i in range(len(hu)): 
            id = hu[i][0]
            self.Id_Seleccionado.setText(str(id))
            self.lcdNumber_id.display((id))

    def pesquisar_pessoa(self):
        nome = self.textEdit.toPlainText()

        novoMod = QStandardItemModel()
        mod = self.listView.model()
        for r in range(mod.rowCount()):
            it = mod.item(r)
            if nome in it.text():
                dwd = QStandardItem(it.text())
                dwd.setCheckable(True)
                novoMod.appendRow(dwd)
        
        self.model = novoMod
        self.listView.setModel(self.model)
    
    def connectSignalsSlots(self):
        self.Executar.clicked.connect(self.btn_Executar_click)
        self.Criar_Nome.clicked.connect(self.btn_Criar_Nome_click)
        self.Eliminar.clicked.connect(self.btn_Eliminar_click)
        self.listView.clicked.connect(self.btn_Id_Seleccionado_click)
        self.Pesquisar.clicked.connect(self.btn_pesquisar_pessoa_click)
        self.textEdit.textChanged.connect(self.btn_pesquisar_pessoa_click)

    def btn_Executar_click(self):
        self.guardar_list_nomes()
        self.updateListCount()
    
    def btn_Criar_Nome_click(self):
        self.criar_pessoa_DB()
        self.updateListCount()

    def btn_Eliminar_click(self):
        self.eliminar_pessoa()
        self.updateListCount()

    def btn_Id_Seleccionado_click(self):
        self.Id_Seleccionado_func()

    def btn_pesquisar_pessoa_click(self):
        self.guardar_list_nomes()
        self.pesquisar_pessoa()
        self.updateListCount()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
