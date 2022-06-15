# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 483)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LeftUp = QPushButton(self.centralwidget)
        self.LeftUp.setObjectName(u"LeftUp")
        self.LeftUp.setGeometry(QRect(30, 30, 131, 51))
        self.RightUp = QPushButton(self.centralwidget)
        self.RightUp.setObjectName(u"RightUp")
        self.RightUp.setGeometry(QRect(210, 30, 131, 51))
        self.Center = QPushButton(self.centralwidget)
        self.Center.setObjectName(u"Center")
        self.Center.setGeometry(QRect(30, 90, 311, 51))
        self.LeftDown = QPushButton(self.centralwidget)
        self.LeftDown.setObjectName(u"LeftDown")
        self.LeftDown.setGeometry(QRect(30, 150, 131, 51))
        self.RightDown = QPushButton(self.centralwidget)
        self.RightDown.setObjectName(u"RightDown")
        self.RightDown.setGeometry(QRect(210, 150, 131, 51))
        self.GetData = QPushButton(self.centralwidget)
        self.GetData.setObjectName(u"GetData")
        self.GetData.setGeometry(QRect(40, 210, 301, 51))
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(50, 290, 111, 101))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(373, 30, 251, 361))
        self.HexLable = QComboBox(self.centralwidget)
        self.HexLable.addItem("")
        self.HexLable.setObjectName(u"HexLable")
        self.HexLable.setGeometry(QRect(220, 290, 121, 22))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(220, 330, 121, 61))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 410, 601, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 702, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LeftUp.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.RightUp.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.Center.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.LeftDown.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u043d\u0438\u0437", None))
        self.RightDown.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u043d\u0438\u0437", None))
        self.GetData.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.HexLable.setItemText(0, QCoreApplication.translate("MainWindow", u"Hex", None))

    # retranslateUi

