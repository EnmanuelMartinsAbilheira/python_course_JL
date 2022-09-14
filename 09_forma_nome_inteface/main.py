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

    def procura_menor(self):
        v = [
            self.txt_num1.text(),
            self.txt_num2.text(),
            self.txt_num3.text(),
            self.txt_num4.text(),
            self.txt_num5.text()
        ]
        ret = {}

        for x in v:
            print(x)
            try:
                m = int(x)
                if "maior" not in ret:
                    ret["maior"] = m
                elif ret["maior"] < m:
                    ret["maior"] = m

                if "menor" not in ret:
                    ret["menor"] = m
                elif ret["menor"] > m:
                    ret["menor"] = m
            except:
                pass
        return ret

        
    def btn_Executar_click(self):
        k = self.procura_menor()
        if "maior" in k and "menor" in k:
            self.txt_resultado.setText("[" + str(k["menor"]) + ", " + str(k["maior"]) + "]")
        
        
    
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())