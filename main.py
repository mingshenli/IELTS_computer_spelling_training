# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:06:30 2020

@author: 18926
"""

from gui_import import Main_control_window
import os
import time as t
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QMessageBox
import sys,copy,re
from PyQt5.QtCore import Qt, QThread,pyqtSignal, QTimer
#from translator import translator


import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class mainprogram(Main_control_window):
    def __init__(self):
        super().__init__()
        self.p=0
        self.length=0
        self.alreadknow=0
        self.valist=[]
        self.checklist=[]
        self.Dic.clicked.connect(self.choosedic)
        self.Sayagain.clicked.connect(self.sayagain)
        self.Next.clicked.connect(self.nextva)
        self.Checkanswer.clicked.connect(self.compare)
    def nextva(self):
#        self.Input.clear()
        self.Input.setText('')
        
        cursor=self.Input.textCursor()
#        cursor.movePosition(QTextCursor.End) 
        self.Input.setTextCursor(cursor)
        
        self.p=(self.p+1)%(self.length)
        cir=0
        
        while self.checklist[self.p]==1:
             self.p=(self.p+1)%(self.length)
#             print(self.p)
             cir=cir+1
             if cir>self.length:
                 self.check.setText('finish')
                 engine.say('finish')
                 engine.runAndWait()
                 return
#        self.Showen.setText(self.valist[self.p])
        engine.say(self.valist[self.p])
        engine.runAndWait()
        
    def compare(self):
        inp=self.Input.toPlainText()
        if inp==self.valist[self.p]:
            self.check.setText('correct')
            self.checklist[self.p]=1
            engine.say('correct')
            engine.runAndWait()
            t.sleep(1)
            self.nextva()#直接调用光标就不会出来
        else:
            self.check.setText('wrong')
            self.Key.setText(self.valist[self.p])
            engine.say('wrong')
            engine.runAndWait()
            
        
    def choosedic(self):
        self.p=0
        self.length=0
        self.alreadknow=0
        self.checklist=[]
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "valib",
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        try:
            f=open(fileName,"r",encoding="UTF-8-sig")
            i=f.read()
            f.close()
#            print(i)
        except Exception as e:
            print(str(e))
            
            return
        i=i.split('\n')
        rei=[]
      
        for ind in range(0,len(i)):
            if i[ind] != '':
                s=str.strip(i[ind])
                rei.append(s.lower())
                self.checklist.append(0)
            else:
                break
        self.valist=rei
        print(self.valist)
        self.length=len(self.valist)
        engine.say(self.valist[self.p])
        engine.runAndWait()
        
    def sayagain(self):
        engine.say(self.valist[self.p])
        engine.runAndWait()
        
    def keyPressEvent(self,event):
#        print(str(event.key()))
        if event.key()==Qt.Key_Alt:
#            print(str(event.key()))
            self.nextva()
#        if event.key()==Qt.Key_:
#            self.compare()
        if event.key()==Qt.Key_Control:
            self.compare()
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a = mainprogram()
    a.show()
    sys.exit(app.exec_()) 