# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_2048.ui'
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
        MainWindow.resize(339, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2048 = QLabel(self.centralwidget)
        self.label_2048.setObjectName(u"label_2048")
        self.label_2048.setGeometry(QRect(240, 30, 81, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_2048.setFont(font)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(32, 198, 60, 60))
        self.lineEdit_5.setMinimumSize(QSize(60, 60))
        self.lineEdit_5.setMaximumSize(QSize(60, 60))
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(32, 264, 60, 60))
        self.lineEdit_9.setMinimumSize(QSize(60, 60))
        self.lineEdit_9.setMaximumSize(QSize(60, 60))
        self.lineEdit_13 = QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(32, 330, 60, 60))
        self.lineEdit_13.setMinimumSize(QSize(60, 60))
        self.lineEdit_13.setMaximumSize(QSize(60, 60))
        self.init = QPushButton(self.centralwidget)
        self.init.setObjectName(u"init")
        self.init.setGeometry(QRect(10, 30, 75, 30))
        self.score_label = QLabel(self.centralwidget)
        self.score_label.setObjectName(u"score_label")
        self.score_label.setGeometry(QRect(120, 10, 47, 13))
        self.score_label.setFont(font)
        self.lineEdit_score = QLineEdit(self.centralwidget)
        self.lineEdit_score.setObjectName(u"lineEdit_score")
        self.lineEdit_score.setGeometry(QRect(100, 30, 90, 30))
        self.left = QPushButton(self.centralwidget)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(11, 87, 75, 23))
        self.right = QPushButton(self.centralwidget)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(92, 87, 75, 23))
        self.down = QPushButton(self.centralwidget)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(173, 87, 75, 23))
        self.up = QPushButton(self.centralwidget)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(254, 87, 75, 23))
        self.lineEdit_15 = QLineEdit(self.centralwidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(168, 330, 60, 60))
        self.lineEdit_15.setMinimumSize(QSize(60, 60))
        self.lineEdit_15.setMaximumSize(QSize(60, 60))
        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(168, 264, 60, 60))
        self.lineEdit_11.setMinimumSize(QSize(60, 60))
        self.lineEdit_11.setMaximumSize(QSize(60, 60))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(168, 198, 60, 60))
        self.lineEdit_7.setMinimumSize(QSize(60, 60))
        self.lineEdit_7.setMaximumSize(QSize(60, 60))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(168, 132, 60, 60))
        self.lineEdit_3.setMinimumSize(QSize(60, 60))
        self.lineEdit_3.setMaximumSize(QSize(60, 60))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 132, 60, 60))
        self.lineEdit_2.setMinimumSize(QSize(60, 60))
        self.lineEdit_2.setMaximumSize(QSize(60, 60))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(100, 198, 60, 60))
        self.lineEdit_6.setMinimumSize(QSize(60, 60))
        self.lineEdit_6.setMaximumSize(QSize(60, 60))
        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(100, 264, 60, 60))
        self.lineEdit_10.setMinimumSize(QSize(60, 60))
        self.lineEdit_10.setMaximumSize(QSize(60, 60))
        self.lineEdit_14 = QLineEdit(self.centralwidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(100, 330, 60, 60))
        self.lineEdit_14.setMinimumSize(QSize(60, 60))
        self.lineEdit_14.setMaximumSize(QSize(60, 60))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(236, 132, 60, 60))
        self.lineEdit_4.setMinimumSize(QSize(60, 60))
        self.lineEdit_4.setMaximumSize(QSize(60, 60))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(236, 198, 60, 60))
        self.lineEdit_8.setMinimumSize(QSize(60, 60))
        self.lineEdit_8.setMaximumSize(QSize(60, 60))
        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(236, 264, 60, 60))
        self.lineEdit_12.setMinimumSize(QSize(60, 60))
        self.lineEdit_12.setMaximumSize(QSize(60, 60))
        self.lineEdit_16 = QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(236, 330, 60, 60))
        self.lineEdit_16.setMinimumSize(QSize(60, 60))
        self.lineEdit_16.setMaximumSize(QSize(60, 60))
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(32, 132, 60, 60))
        self.lineEdit_1.setMinimumSize(QSize(60, 60))
        self.lineEdit_1.setMaximumSize(QSize(60, 60))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2048.setText(QCoreApplication.translate("MainWindow", u"Game 2048", None))
        self.init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.score_label.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
    # retranslateUi

