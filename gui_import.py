# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:05:39 2020

@author: 18926
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
class Main_control_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_control_window, self).__init__(parent)
        self.setupUi(self)  