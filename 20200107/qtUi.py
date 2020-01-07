# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 661, 451))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(150, 500, 75, 23))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_last = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_last.setGeometry(QtCore.QRect(480, 500, 75, 23))
        self.pushButton_last.setObjectName("pushButton_last")
        self.pushButton_read = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_read.setGeometry(QtCore.QRect(310, 500, 75, 23))
        self.pushButton_read.setObjectName("pushButton_read")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_next.setText(_translate("MainWindow", "下一个"))
        self.pushButton_last.setText(_translate("MainWindow", "上一个"))
        self.pushButton_read.setText(_translate("MainWindow", "读取"))

