# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\display.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label_display = QtWidgets.QLabel(Form)
        self.label_display.setGeometry(QtCore.QRect(30, 100, 331, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_display.setFont(font)
        self.label_display.setText("")
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

