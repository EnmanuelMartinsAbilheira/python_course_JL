# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(883, 677)
        Dialog.setMinimumSize(QtCore.QSize(488, 375))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.txt_num1 = QtWidgets.QLineEdit(Dialog)
        self.txt_num1.setGeometry(QtCore.QRect(180, 20, 421, 81))
        self.txt_num1.setObjectName("txt_num1")
        self.Executar = QtWidgets.QPushButton(Dialog)
        self.Executar.setGeometry(QtCore.QRect(260, 260, 271, 71))
        self.Executar.setObjectName("Executar")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(100, 530, 661, 121))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.txt_num2 = QtWidgets.QLineEdit(Dialog)
        self.txt_num2.setGeometry(QtCore.QRect(180, 150, 421, 81))
        self.txt_num2.setObjectName("txt_num2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 380, 651, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 550, 151, 91))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 470, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Executar.setText(_translate("Dialog", "Executar"))
        self.label.setText(_translate("Dialog", "Peso"))
        self.label_2.setText(_translate("Dialog", "Altura"))
        self.label_4.setText(_translate("Dialog", "Peso inferior al normal Menos de 18.5 - Normal 18.5 – 24.9 "))
        self.label_3.setText(_translate("Dialog", "Peso superior al normal   25.0 – 29.9  Obesidad - Más de 30.0"))
