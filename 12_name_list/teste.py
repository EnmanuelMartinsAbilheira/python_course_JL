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
        Dialog.resize(701, 555)
        Dialog.setMinimumSize(QtCore.QSize(488, 375))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.Executar = QtWidgets.QPushButton(Dialog)
        self.Executar.setGeometry(QtCore.QRect(180, 130, 181, 71))
        self.Executar.setObjectName("Executar")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(90, 220, 551, 291))
        self.listView.setObjectName("listView")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 501, 61))
        self.textEdit.setObjectName("textEdit")
        self.Delete = QtWidgets.QPushButton(Dialog)
        self.Delete.setGeometry(QtCore.QRect(380, 130, 181, 71))
        self.Delete.setObjectName("Delete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Executar.setText(_translate("Dialog", "Executar"))
        self.Delete.setText(_translate("Dialog", "Delete"))
