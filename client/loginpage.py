#!/usr/bin/python
# first page is a login and register page
import sys
from PyQt4 import QtGui
import socket
from time import ctime
import cocos
import pygame
from pygame.locals import *
from hall import *


HOST = 'localhost'
PORT = 6666

class LoginPage(QtGui.QWidget):
    
    def __init__(self, sock=None, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(363,144,640,480)
        self.setWindowTitle("Welcome the The HSS world")
        
        name_label = QtGui.QLabel('Name:')
        password_label = QtGui.QLabel('password')
        
        self.name_edit = QtGui.QLineEdit()
        self.password_edit = QtGui.QLineEdit()
        
        self.login_btn = QtGui.QPushButton('Login')
        self.reg_btn = QtGui.QPushButton('Register')
        
        grid = QtGui.QGridLayout()
        
        grid.addWidget(name_label,     1, 0)
        grid.addWidget(self.name_edit, 1, 1)       
        
        grid.addWidget(password_label,     2, 0)
        grid.addWidget(self.password_edit, 2, 1)
        
        grid.addWidget(self.login_btn,  3, 0 )
        grid.addWidget(self.reg_btn,    3, 1)
        
        self.setLayout(grid)
        
        self.login_btn.clicked.connect(self.login)
        self.reg_btn.clicked.connect(self.register)
        
        ### some sock
        self.sock = sock
        
        self.Exit = True
        
    def login_ok(self):
        print "login_ok"
        self.Exit = False
        self.close()
    def login_error(self,error_msg):
        QtGui.QMessageBox.question(self, '', error_msg) 
        print "login error"
        
    def login(self):
        reg_msg = u"login" + u"@"  + unicode(self.name_edit.text()) + u"@" + unicode(self.password_edit.text())
        print reg_msg
        self.sock.send(reg_msg)
        data = self.sock.recv(1024)
        
        print "wtf",unicode(data)
        
        if unicode(data) == u'ok':
            self.login_ok()
        
        else: 
            self.login_error(unicode(data))
        
    def reg_ok(self):
        reg_msg_box = QtGui.QMessageBox.question(self, '', "Sir, your registration is OK!", QtGui.QMessageBox.Ok)
        if reg_msg_box == QtGui.QMessageBox.Yes:
            print "yeah, reg is ok"
    def reg_error(self,msg):
        QtGui.QMessageBox.question(self, '', msg)  
        print "reg error" 
    def register(self):
        reg_msg = u"register" + u"@"  + unicode(self.name_edit.text()) + u"@" + unicode(self.password_edit.text())
        self.sock.send(reg_msg)
        data = self.sock.recv(1024)
        if unicode(data) == u'ok':
            self.reg_ok()
        
        else: 
            self.reg_error(unicode(data))
    
    def closeEvent(self, event):
        if self.Exit == False:
            event.accept()
        else:
            reply = QtGui.QMessageBox.question(self,'',
                                            "Are you sure you wanna quit?", QtGui.QMessageBox.Yes,
                                            QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

## connect server sock
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    app = QtGui.QApplication(sys.argv)
    lp = LoginPage(sock)
    lp.show()
    app.exec_()

    eHall = Hall(sock)
    eHall.run()
