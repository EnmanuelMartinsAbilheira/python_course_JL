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
        Dialog.resize(696, 703)
        Dialog.setMinimumSize(QtCore.QSize(488, 375))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.txt_num1 = QtWidgets.QLineEdit(Dialog)
        self.txt_num1.setGeometry(QtCore.QRect(20, 30, 671, 81))
        self.txt_num1.setObjectName("txt_num1")
        self.txt_num2 = QtWidgets.QLineEdit(Dialog)
        self.txt_num2.setGeometry(QtCore.QRect(20, 120, 671, 81))
        self.txt_num2.setObjectName("txt_num2")
        self.txt_resultado = QtWidgets.QLineEdit(Dialog)
        self.txt_resultado.setGeometry(QtCore.QRect(340, 560, 331, 91))
        self.txt_resultado.setObjectName("txt_resultado")
        self.Executar = QtWidgets.QPushButton(Dialog)
        self.Executar.setGeometry(QtCore.QRect(20, 570, 271, 71))
        self.Executar.setObjectName("Executar")
        self.txt_num3 = QtWidgets.QLineEdit(Dialog)
        self.txt_num3.setGeometry(QtCore.QRect(20, 210, 671, 81))
        self.txt_num3.setObjectName("txt_num3")
        self.txt_num4 = QtWidgets.QLineEdit(Dialog)
        self.txt_num4.setGeometry(QtCore.QRect(20, 300, 671, 81))
        self.txt_num4.setObjectName("txt_num4")
        self.txt_num5 = QtWidgets.QLineEdit(Dialog)
        self.txt_num5.setGeometry(QtCore.QRect(20, 390, 671, 81))
        self.txt_num5.setObjectName("txt_num5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Executar.setText(_translate("Dialog", "Executar"))
