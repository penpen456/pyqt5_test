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
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 100, 221, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_hour = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_hour.setFont(font)
        self.label_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hour.setObjectName("label_hour")
        self.horizontalLayout.addWidget(self.label_hour)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_minute = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_minute.setFont(font)
        self.label_minute.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minute.setObjectName("label_minute")
        self.horizontalLayout.addWidget(self.label_minute)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_second = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_second.setFont(font)
        self.label_second.setAlignment(QtCore.Qt.AlignCenter)
        self.label_second.setObjectName("label_second")
        self.horizontalLayout.addWidget(self.label_second)
        self.pushButton_back = QtWidgets.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_hour.setText(_translate("Form", "10"))
        self.label_2.setText(_translate("Form", ":"))
        self.label_minute.setText(_translate("Form", "10"))
        self.label_3.setText(_translate("Form", ":"))
        self.label_second.setText(_translate("Form", "10"))
        self.pushButton_back.setText(_translate("Form", "返回"))

