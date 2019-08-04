# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\first_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 456)
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 401, 311))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 401, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.get_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.get_btn.setObjectName("get_btn")
        self.horizontalLayout.addWidget(self.get_btn)
        self.close_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.get_btn.setText(_translate("Form", "get"))
        self.close_btn.setText(_translate("Form", "close"))

