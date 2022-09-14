import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from teste import Ui_Dialog

class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.btn_div.clicked.connect(self.btn_dividir_click)
        self.btn_mult.clicked.connect(self.btn_multiplicar_click)
        self.btn_sum.clicked.connect(self.btn_somar_click)
        self.btn_sub.clicked.connect(self.btn_subtrair_click)


    def btn_subtrair_click(self):
        try:
            self.txt_resultado.setText(str(int(self.txt_num1.text()) - int(self.txt_num2.text())))
        except:
            self.txt_resultado.setText("0")
    
    def btn_somar_click(self):
        try:
            self.txt_resultado.setText(str(int(self.txt_num1.text()) + int(self.txt_num2.text())))
        except:
            self.txt_resultado.setText("0")
    
    def btn_multiplicar_click(self):
        try:
            self.txt_resultado.setText(str(int(self.txt_num1.text()) * int(self.txt_num2.text())))
        except:
            self.txt_resultado.setText("0")

    def btn_dividir_click(self): 
        try:
            self.txt_resultado.setText(str(int(self.txt_num1.text()) / int(self.txt_num2.text())))
        except:
            self.txt_resultado.setText("0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())