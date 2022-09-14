import sys
import time
from _thread import *

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from teste import Ui_Dialog

class Window(QMainWindow, Ui_Dialog):
    
    loading_speed = 1
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.Executar.clicked.connect(self.btn_Executar_click)
        self.horizontalSlider.valueChanged.connect(self.bar_loading_speed)

    def loading_bar_forever(self):
        count = 0
        while True:
            time.sleep(1/self.loading_speed)
            self.progressBar.setValue(count)
            print(count)
            if count == 101:
                count = 0
            count += 1
            
    def bar_loading_speed(self):
        if self.horizontalSlider.value() <= 0:
            self.loading_speed = 0
        elif self.horizontalSlider.value() >= 100:   
            self.loading_speed = 100
        else:
            self.loading_speed = self.horizontalSlider.value()
        pass

    def btn_Executar_click(self):
        try:
            start_new_thread(self.loading_bar_forever, ())
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())