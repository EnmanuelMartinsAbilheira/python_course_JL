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
        Dialog.resize(701, 592)
        Dialog.setMinimumSize(QtCore.QSize(488, 375))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.Executar = QtWidgets.QPushButton(Dialog)
        self.Executar.setGeometry(QtCore.QRect(80, 130, 181, 71))
        self.Executar.setObjectName("Executar")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(40, 220, 261, 291))
        self.listView.setObjectName("listView")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 501, 61))
        self.textEdit.setObjectName("textEdit")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(410, 220, 261, 291))
        self.listView_2.setObjectName("listView_2")
        self.Executar_izq = QtWidgets.QPushButton(Dialog)
        self.Executar_izq.setGeometry(QtCore.QRect(320, 270, 81, 71))
        self.Executar_izq.setObjectName("Executar_izq")
        self.Executar_der = QtWidgets.QPushButton(Dialog)
        self.Executar_der.setGeometry(QtCore.QRect(320, 360, 81, 71))
        self.Executar_der.setObjectName("Executar_der")
        self.Delete = QtWidgets.QPushButton(Dialog)
        self.Delete.setGeometry(QtCore.QRect(270, 130, 181, 71))
        self.Delete.setObjectName("Delete")
        self.Editar = QtWidgets.QPushButton(Dialog)
        self.Editar.setGeometry(QtCore.QRect(460, 130, 181, 71))
        self.Editar.setObjectName("Editar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 520, 91, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 520, 81, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Executar.setText(_translate("Dialog", "Executar"))
        self.Executar_izq.setText(_translate("Dialog", "<"))
        self.Executar_der.setText(_translate("Dialog", ">"))
        self.Delete.setText(_translate("Dialog", "Delete"))
        self.Editar.setText(_translate("Dialog", "Editar"))
        self.label.setText(_translate("Dialog", "N_izq"))
        self.label_2.setText(_translate("Dialog", "N_der"))
