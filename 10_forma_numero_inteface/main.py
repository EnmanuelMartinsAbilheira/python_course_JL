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
        self.Executar.clicked.connect(self.btn_Executar_click)

    def iMC(self):
        p = float(self.txt_num1.text())
        a = float(self.txt_num2.text())
        imc = p / (a*a)
        return imc

            

    def btn_Executar_click(self):
        try:
            print(self.iMC)
            self.progressBar.setValue(self.iMC())
            print(type(self.lcdNumber))
            self.lcdNumber.display(self.iMC())
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())