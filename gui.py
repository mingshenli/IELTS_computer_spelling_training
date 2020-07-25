# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\program\python\IELS_computer_training/gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check = QtWidgets.QTextBrowser(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(370, 420, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 220, 91, 21))
        self.label_2.setObjectName("label_2")
        self.Dic = QtWidgets.QPushButton(self.centralwidget)
        self.Dic.setGeometry(QtCore.QRect(120, 450, 141, 71))
        self.Dic.setIconSize(QtCore.QSize(50, 50))
        self.Dic.setObjectName("Dic")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(470, 610, 141, 61))
        self.Next.setObjectName("Next")
        self.Sayagain = QtWidgets.QPushButton(self.centralwidget)
        self.Sayagain.setGeometry(QtCore.QRect(130, 530, 111, 61))
        self.Sayagain.setObjectName("Sayagain")
        self.Key = QtWidgets.QTextEdit(self.centralwidget)
        self.Key.setGeometry(QtCore.QRect(110, 40, 851, 171))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.Key.setFont(font)
        self.Key.setObjectName("Key")
        self.Input = QtWidgets.QTextEdit(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(110, 240, 861, 161))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.Input.setFont(font)
        self.Input.setObjectName("Input")
        self.Checkanswer = QtWidgets.QPushButton(self.centralwidget)
        self.Checkanswer.setGeometry(QtCore.QRect(470, 530, 141, 71))
        self.Checkanswer.setObjectName("Checkanswer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 26))
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
        self.label.setText(_translate("MainWindow", "keys"))
        self.label_2.setText(_translate("MainWindow", "your answer"))
        self.Dic.setText(_translate("MainWindow", "choose dic"))
        self.Next.setText(_translate("MainWindow", "next"))
        self.Sayagain.setText(_translate("MainWindow", "say again"))
        self.Checkanswer.setText(_translate("MainWindow", "check answer"))

