# -*- coding: utf-8 -*-
# DevelOPS
# Invictuz Online
# Mark Anthony Pequeras - 2013
coreSEC = """
_________  ________ _____________________ _____________________________  
\_   ___ \ \_____  \\______   \_   _____//   _____/\_   _____/\_   ___ \ 
/    \  \/  /   |   \|       _/|    __)_ \_____  \  |    __)_ /    \  \/ 
\     \____/    |    \    |   \|        \/        \ |        \\     \____
 \______  /\_______  /____|_  /_______  /_______  //_______  / \______  /
        \/         \/       \/        \/        \/         \/         \/ 
"""
from Settings import settings
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread
import sys
import pyodbc as db
import plus
import setyellow
import wepyellow
import invictuzsockets
import subprocess


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mPequeras(object):
    def __init__(self):
        self.fullVault = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.con = db.connect('DRIVER={SQL SERVER};SERVER=25.69.176.139;DATABASE=MuOnline;UID=sa;PWD=mLnA4f2o82jX')
        # name[ROW] number [Column]
        # r1c
        self.first1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.first2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.first3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.first4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r2c
        self.second1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.second2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.second3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.second4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r3c
        self.third1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.third2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.third3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.third4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r4c
        self.fourth1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fourth2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fourth3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fourth4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r5c
        self.fifth1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fifth2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fifth3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.fifth4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r6c
        self.sixth1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.sixth2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.sixth3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.sixth4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        # r7c
        self.seventh1 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.seventh2 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.seventh3 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        self.seventh4 = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
    def setupUi(self, mPequeras):
        mPequeras.setObjectName(_fromUtf8("mPequeras"))
        mPequeras.resize(889, 705)
        mPequeras.setStyleSheet(_fromUtf8("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #333751);"))
        self.premiumItems = QtGui.QPushButton(mPequeras)
        self.premiumItems.setGeometry(QtCore.QRect(390, 120, 201, 51))
        self.premiumItems.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.premiumItems.setObjectName(_fromUtf8("premiumItems"))
        self.lineEdit_4 = QtGui.QLineEdit(mPequeras)
        self.lineEdit_4.setGeometry(QtCore.QRect(840, 120, 61, 20))
        self.lineEdit_4.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pkClear = QtGui.QPushButton(mPequeras)
        self.pkClear.setGeometry(QtCore.QRect(10, 120, 181, 51))
        self.pkClear.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.pkClear.setObjectName(_fromUtf8("pkClear"))
        self.fullGearMaker = QtGui.QPushButton(mPequeras)
        self.fullGearMaker.setGeometry(QtCore.QRect(200, 120, 181, 51))
        self.fullGearMaker.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.fullGearMaker.setObjectName(_fromUtf8("fullGearMaker"))
        self.connected = QtGui.QLabel(mPequeras)
        self.connected.setGeometry(QtCore.QRect(380, 680, 211, 20))
        self.connected.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: transparent;"))
        self.connected.setObjectName(_fromUtf8("connected"))
        self.comboBox = QtGui.QComboBox(mPequeras)
        self.comboBox.setGeometry(QtCore.QRect(620, 30, 251, 22))
        self.comboBox.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(156, 156, 156)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.lineEdit_2 = QtGui.QLineEdit(mPequeras)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 50, 191, 20))
        self.lineEdit_2.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.accountMaker = QtGui.QPushButton(mPequeras)
        self.accountMaker.setGeometry(QtCore.QRect(10, 60, 181, 51))
        self.accountMaker.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.accountMaker.setObjectName(_fromUtf8("accountMaker"))
        self.label_2 = QtGui.QLabel(mPequeras)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(600, 0, 291, 711))
        self.label_2.setStyleSheet(_fromUtf8("background:rgb(0, 85, 127)"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(mPequeras)
        self.label.setGeometry(QtCore.QRect(20, 0, 341, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(0, 85, 127)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mPequeras)
        self.label_3.setGeometry(QtCore.QRect(10, 680, 201, 16))
        self.label_3.setStyleSheet(_fromUtf8("background: none;\n"
"color: rgb(100, 100, 100);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.itemMaker = QtGui.QPushButton(mPequeras)
        self.itemMaker.setGeometry(QtCore.QRect(200, 60, 181, 51))
        self.itemMaker.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.itemMaker.setObjectName(_fromUtf8("itemMaker"))
        self.connectNow = QtGui.QPushButton(mPequeras)
        self.connectNow.setGeometry(QtCore.QRect(810, 50, 71, 41))
        self.connectNow.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 13px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.connectNow.setObjectName(_fromUtf8("connectNow"))
        self.serverPassword = QtGui.QLineEdit(mPequeras)
        self.serverPassword.setGeometry(QtCore.QRect(610, 70, 201, 21))
        self.serverPassword.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.serverPassword.setText(_fromUtf8(""))
        self.serverPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.serverPassword.setObjectName(_fromUtf8("serverPassword"))
        self.customQueries = QtGui.QPushButton(mPequeras)
        self.customQueries.setGeometry(QtCore.QRect(390, 60, 201, 51))
        self.customQueries.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.customQueries.setObjectName(_fromUtf8("customQueries"))
        self.serverServer = QtGui.QLineEdit(mPequeras)
        self.serverServer.setGeometry(QtCore.QRect(610, 10, 201, 21))
        self.serverServer.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.serverServer.setObjectName(_fromUtf8("serverServer"))
        self.serverPort = QtGui.QLineEdit(mPequeras)
        self.serverPort.setGeometry(QtCore.QRect(810, 10, 71, 21))
        self.serverPort.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.serverPort.setEchoMode(QtGui.QLineEdit.Normal)
        self.serverPort.setObjectName(_fromUtf8("serverPort"))
        self.connectionType = QtGui.QComboBox(mPequeras)
        self.connectionType.setGeometry(QtCore.QRect(610, 30, 261, 22))
        self.connectionType.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(156, 156, 156)"))
        self.connectionType.setObjectName(_fromUtf8("connectionType"))
        self.connectionType.addItem(_fromUtf8(""))
        self.connectionType.addItem(_fromUtf8(""))
        self.serverUsername = QtGui.QLineEdit(mPequeras)
        self.serverUsername.setGeometry(QtCore.QRect(610, 50, 201, 20))
        self.serverUsername.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.serverUsername.setText(_fromUtf8(""))
        self.serverUsername.setObjectName(_fromUtf8("serverUsername"))
        self.closenow = QtGui.QPushButton(mPequeras)
        self.closenow.setGeometry(QtCore.QRect(820, 670, 61, 31))
        self.closenow.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 13px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.closenow.setObjectName(_fromUtf8("closenow"))
        self.MarkPequerasfooter = QtGui.QLabel(mPequeras)
        self.MarkPequerasfooter.setGeometry(QtCore.QRect(10, 680, 299, 16))
        self.MarkPequerasfooter.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: rgb(107, 107, 107)"))
        self.MarkPequerasfooter.setObjectName(_fromUtf8("MarkPequerasfooter"))
        self.minimize = QtGui.QPushButton(mPequeras)
        self.minimize.setGeometry(QtCore.QRect(760, 670, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.minimize.setFont(font)
        self.minimize.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 19px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.minimize.setObjectName(_fromUtf8("minimize"))
        self.editCharacter = QtGui.QPushButton(mPequeras)
        self.editCharacter.setGeometry(QtCore.QRect(10, 180, 181, 51))
        self.editCharacter.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.editCharacter.setObjectName(_fromUtf8("editCharacter"))
        self.OptionsButton = QtGui.QPushButton(mPequeras)
        self.OptionsButton.setGeometry(QtCore.QRect(390, 180, 201, 51))
        self.OptionsButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.OptionsButton.setObjectName(_fromUtf8("OptionsButton"))
        self.CastleSiegeButton = QtGui.QPushButton(mPequeras)
        self.CastleSiegeButton.setGeometry(QtCore.QRect(200, 180, 181, 51))
        self.CastleSiegeButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.CastleSiegeButton.setObjectName(_fromUtf8("CastleSiegeButton"))
        self.MessageBox = QtGui.QTextEdit(mPequeras)
        self.MessageBox.setGeometry(QtCore.QRect(610, 170, 271, 381))
        self.MessageBox.setStyleSheet(_fromUtf8("border: none;\n"
"color: rgb(211, 211, 211);"))
        self.MessageBox.setObjectName(_fromUtf8("MessageBox"))
        self.label_5 = QtGui.QLabel(mPequeras)
        self.label_5.setGeometry(QtCore.QRect(830, 150, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("background: none;\n"
"color: rgb(180, 180, 180)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.saveCredentials = QtGui.QPushButton(mPequeras)
        self.saveCredentials.setGeometry(QtCore.QRect(610, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.saveCredentials.setFont(font)
        self.saveCredentials.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 9px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.saveCredentials.setObjectName(_fromUtf8("saveCredentials"))
        self.saveLogs = QtGui.QPushButton(mPequeras)
        self.saveLogs.setGeometry(QtCore.QRect(610, 670, 71, 31))
        self.saveLogs.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 13px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.saveLogs.setObjectName(_fromUtf8("saveLogs"))
        self.clearallLogs = QtGui.QPushButton(mPequeras)
        self.clearallLogs.setGeometry(QtCore.QRect(680, 670, 71, 31))
        self.clearallLogs.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"

"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 13px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.clearallLogs.setObjectName(_fromUtf8("clearallLogs"))
        self.progressBar = QtGui.QProgressBar(mPequeras)
        self.progressBar.setGeometry(QtCore.QRect(490, 20, 101, 21))
        self.progressBar.setStyleSheet(_fromUtf8(" QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
" }\n"
"\n"
" QProgressBar:chunk {\n"
"     background-color: #05B8CC;\n"
"     width: 20px;\n"
" }"))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setFormat(_fromUtf8("%p% Success"))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.background = QtGui.QLabel(mPequeras)
        self.background.setEnabled(False)
        self.background.setGeometry(QtCore.QRect(10, 240, 581, 431))
        self.background.setStyleSheet(_fromUtf8("background:rgb(0, 85, 127)"))
        self.background.setText(_fromUtf8(""))
        self.background.setObjectName(_fromUtf8("background"))
        self.ShowSwords = QtGui.QPushButton(mPequeras)
        self.ShowSwords.setGeometry(QtCore.QRect(310, 250, 81, 31))
        self.ShowSwords.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowSwords.setObjectName(_fromUtf8("ShowSwords"))
        self.ShowAxes = QtGui.QPushButton(mPequeras)
        self.ShowAxes.setGeometry(QtCore.QRect(310, 280, 81, 31))
        self.ShowAxes.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowAxes.setObjectName(_fromUtf8("ShowAxes"))
        self.ShowBows = QtGui.QPushButton(mPequeras)
        self.ShowBows.setGeometry(QtCore.QRect(310, 400, 81, 31))
        self.ShowBows.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowBows.setObjectName(_fromUtf8("ShowBows"))
        self.ShowSpears = QtGui.QPushButton(mPequeras)
        self.ShowSpears.setGeometry(QtCore.QRect(310, 370, 81, 31))
        self.ShowSpears.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowSpears.setObjectName(_fromUtf8("ShowSpears"))
        self.ShowMaces = QtGui.QPushButton(mPequeras)
        self.ShowMaces.setGeometry(QtCore.QRect(310, 310, 81, 31))
        self.ShowMaces.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowMaces.setObjectName(_fromUtf8("ShowMaces"))
        self.ShowScepters = QtGui.QPushButton(mPequeras)
        self.ShowScepters.setGeometry(QtCore.QRect(310, 340, 81, 31))
        self.ShowScepters.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowScepters.setObjectName(_fromUtf8("ShowScepters"))
        self.ShowCrossBows = QtGui.QPushButton(mPequeras)
        self.ShowCrossBows.setGeometry(QtCore.QRect(310, 430, 81, 31))
        self.ShowCrossBows.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowCrossBows.setObjectName(_fromUtf8("ShowCrossBows"))
        self.ShowStaffs = QtGui.QPushButton(mPequeras)
        self.ShowStaffs.setGeometry(QtCore.QRect(310, 460, 81, 31))
        self.ShowStaffs.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowStaffs.setObjectName(_fromUtf8("ShowStaffs"))
        self.ShowShields = QtGui.QPushButton(mPequeras)
        self.ShowShields.setGeometry(QtCore.QRect(310, 490, 81, 31))
        self.ShowShields.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowShields.setObjectName(_fromUtf8("ShowShields"))
        self.ShowHelms = QtGui.QPushButton(mPequeras)
        self.ShowHelms.setGeometry(QtCore.QRect(150, 280, 81, 31))
        self.ShowHelms.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowHelms.setObjectName(_fromUtf8("ShowHelms"))
        self.line = QtGui.QFrame(mPequeras)
        self.line.setGeometry(QtCore.QRect(394, 250, 21, 411))
        self.line.setStyleSheet(_fromUtf8("background: none;\n"
"color: grey;\n"
""))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.usernameBox = QtGui.QLineEdit(mPequeras)
        self.usernameBox.setGeometry(QtCore.QRect(20, 250, 281, 21))
        self.usernameBox.setStyleSheet(_fromUtf8("border: none;\n"
"background: rgb(132, 132, 132);\n"
"color: white;"))
        self.usernameBox.setObjectName(_fromUtf8("usernameBox"))




        self.checkBox = QtGui.QComboBox(mPequeras)
        self.checkBox.addItems(invictuzsockets.socket)
        self.checkBox.setGeometry(QtCore.QRect(420, 270, 161, 21))
        self.checkBox.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.checkBox_2 = QtGui.QComboBox(mPequeras)
        self.checkBox_2.addItems(invictuzsockets.socket)
        self.checkBox_2.setGeometry(QtCore.QRect(420, 290, 161, 21))
        self.checkBox_2.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))


        self.checkBox_3 = QtGui.QComboBox(mPequeras)
        self.checkBox_3.addItems(invictuzsockets.socket)
        self.checkBox_3.setGeometry(QtCore.QRect(420, 310, 161, 21))
        self.checkBox_3.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))


        self.checkBox_4 = QtGui.QComboBox(mPequeras)
        self.checkBox_4.addItems(invictuzsockets.socket)
        self.checkBox_4.setGeometry(QtCore.QRect(420, 330, 161, 21))
        self.checkBox_4.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))


        self.checkBox_6 = QtGui.QComboBox(mPequeras)
        self.checkBox_6.addItems(invictuzsockets.socket)
        self.checkBox_6.setGeometry(QtCore.QRect(420, 349, 161, 21))
        self.checkBox_6.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))

        self.checkBox_7 = QtGui.QComboBox(mPequeras)
        self.checkBox_7.addItems(invictuzsockets.socket)
        self.checkBox_7.setGeometry(QtCore.QRect(420, 370, 161, 21))
        self.checkBox_7.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);font:9px;"))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))


        self.itemoptionTitle = QtGui.QLabel(mPequeras)
        self.itemoptionTitle.setGeometry(QtCore.QRect(510, 400, 71, 20))
        self.itemoptionTitle.setStyleSheet(_fromUtf8("color: rgb(199, 199, 199);\n"
"background: transparent;"))
        self.itemoptionTitle.setObjectName(_fromUtf8("itemoptionTitle"))
        self.itemOption3 = QtGui.QCheckBox(mPequeras)
        self.itemOption3.setGeometry(QtCore.QRect(420, 460, 161, 21))
        self.itemOption3.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption3.setObjectName(_fromUtf8("itemOption3"))
        self.itemOption5 = QtGui.QCheckBox(mPequeras)
        self.itemOption5.setGeometry(QtCore.QRect(420, 499, 161, 21))
        self.itemOption5.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption5.setObjectName(_fromUtf8("itemOption5"))
        self.itemOption1 = QtGui.QCheckBox(mPequeras)
        self.itemOption1.setGeometry(QtCore.QRect(420, 420, 161, 21))
        self.itemOption1.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption1.setObjectName(_fromUtf8("itemOption1"))
        self.itemOption6 = QtGui.QCheckBox(mPequeras)
        self.itemOption6.setGeometry(QtCore.QRect(420, 520, 161, 21))
        self.itemOption6.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption6.setObjectName(_fromUtf8("itemOption6"))
        self.itemOption2 = QtGui.QCheckBox(mPequeras)
        self.itemOption2.setGeometry(QtCore.QRect(420, 440, 161, 21))
        self.itemOption2.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption2.setObjectName(_fromUtf8("itemOption2"))
        self.itemOption4 = QtGui.QCheckBox(mPequeras)
        self.itemOption4.setGeometry(QtCore.QRect(420, 480, 161, 21))
        self.itemOption4.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: rgb(62, 62, 62);"))
        self.itemOption4.setObjectName(_fromUtf8("itemOption4"))
        self.Serial = QtGui.QLabel(mPequeras)
        self.Serial.setGeometry(QtCore.QRect(380, 680, 211, 20))
        self.Serial.setStyleSheet(_fromUtf8("color: rgb(144, 144, 144);\n"
"background: transparent;"))
        self.Serial.setObjectName(_fromUtf8("Serial"))
        self.ExecuteALL = QtGui.QPushButton(mPequeras)
        self.ExecuteALL.setGeometry(QtCore.QRect(420, 550, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.ExecuteALL.setFont(font)
        self.ExecuteALL.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #FF9933;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #2980b9);\n"

"  border-radius: 1px;\n"



"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #2ea7f2;\n"
"  text-decoration: none;\n"
"}"))
        self.ExecuteALL.setObjectName(_fromUtf8("ExecuteALL"))
        self.ShowArmors = QtGui.QPushButton(mPequeras)
        self.ShowArmors.setGeometry(QtCore.QRect(150, 310, 81, 31))
        self.ShowArmors.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowArmors.setObjectName(_fromUtf8("ShowArmors"))
        self.ShowPants = QtGui.QPushButton(mPequeras)
        self.ShowPants.setGeometry(QtCore.QRect(150, 340, 81, 31))
        self.ShowPants.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowPants.setObjectName(_fromUtf8("ShowPants"))
        self.ShowGloves = QtGui.QPushButton(mPequeras)
        self.ShowGloves.setGeometry(QtCore.QRect(150, 370, 81, 31))
        self.ShowGloves.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowGloves.setObjectName(_fromUtf8("ShowGloves"))

        plist = list(plus.plus)
        self.Plus = QtGui.QListWidget(mPequeras)
        self.Plus.setGeometry(167,450,50,212)
        self.Plus.setObjectName(_fromUtf8("currentPlus"))
        self.Plus.addItems(plist)
        self.Plus.setStyleSheet('background: grey; color: white;')

        self.ShowBoots = QtGui.QPushButton(mPequeras)
        self.ShowBoots.setGeometry(QtCore.QRect(150, 400, 81, 31))
        self.ShowBoots.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowBoots.setObjectName(_fromUtf8("ShowBoots"))
        self.ShowWings = QtGui.QPushButton(mPequeras)
        self.ShowWings.setGeometry(QtCore.QRect(310, 520, 81, 31))
        self.ShowWings.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowWings.setObjectName(_fromUtf8("ShowWings"))
        self.ShowPets = QtGui.QPushButton(mPequeras)
        self.ShowPets.setGeometry(QtCore.QRect(310, 550, 81, 31))
        self.ShowPets.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowPets.setObjectName(_fromUtf8("ShowPets"))
        self.ShowRings = QtGui.QPushButton(mPequeras)
        self.ShowRings.setGeometry(QtCore.QRect(310, 580, 81, 31))
        self.ShowRings.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowRings.setObjectName(_fromUtf8("ShowRings"))
        self.ShowOrbs = QtGui.QPushButton(mPequeras)
        self.ShowOrbs.setGeometry(QtCore.QRect(310, 610, 81, 31))
        self.ShowOrbs.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowOrbs.setObjectName(_fromUtf8("ShowOrbs"))
        self.ShowScrolls = QtGui.QPushButton(mPequeras)
        self.ShowScrolls.setGeometry(QtCore.QRect(230, 280, 81, 31))
        self.ShowScrolls.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowScrolls.setObjectName(_fromUtf8("ShowScrolls"))
        self.ShowJewels = QtGui.QPushButton(mPequeras)
        self.ShowJewels.setGeometry(QtCore.QRect(230, 310, 81, 31))
        self.ShowJewels.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowJewels.setObjectName(_fromUtf8("ShowJewels"))
        self.ShowPotions = QtGui.QPushButton(mPequeras)
        self.ShowPotions.setGeometry(QtCore.QRect(230, 340, 81, 31))
        self.ShowPotions.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowPotions.setObjectName(_fromUtf8("ShowPotions"))
        self.ShowAmulets = QtGui.QPushButton(mPequeras)
        self.ShowAmulets.setGeometry(QtCore.QRect(230, 370, 81, 31))
        self.ShowAmulets.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowAmulets.setObjectName(_fromUtf8("ShowAmulets"))
        self.ShowEvents = QtGui.QPushButton(mPequeras)
        self.ShowEvents.setGeometry(QtCore.QRect(230, 400, 81, 31))
        self.ShowEvents.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowEvents.setObjectName(_fromUtf8("ShowEvents"))
        self.ShowQuests = QtGui.QPushButton(mPequeras)
        self.ShowQuests.setGeometry(QtCore.QRect(230, 430, 81, 31))
        self.ShowQuests.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowQuests.setObjectName(_fromUtf8("ShowQuests"))
        self.ShowBoxes = QtGui.QPushButton(mPequeras)
        self.ShowBoxes.setGeometry(QtCore.QRect(230, 460, 81, 31))
        self.ShowBoxes.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowBoxes.setObjectName(_fromUtf8("ShowBoxes"))
        self.ShowPetMix = QtGui.QPushButton(mPequeras)
        self.ShowPetMix.setGeometry(QtCore.QRect(230, 490, 81, 31))
        self.ShowPetMix.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowPetMix.setObjectName(_fromUtf8("ShowPetMix"))
        self.ShowCastleSiege = QtGui.QPushButton(mPequeras)
        self.ShowCastleSiege.setGeometry(QtCore.QRect(230, 520, 81, 31))
        self.ShowCastleSiege.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowCastleSiege.setObjectName(_fromUtf8("ShowCastleSiege"))
        self.ShowSpears_2 = QtGui.QPushButton(mPequeras)
        self.ShowSpears_2.setGeometry(QtCore.QRect(230, 550, 81, 31))
        self.ShowSpears_2.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowSpears_2.setObjectName(_fromUtf8("ShowSpears_2"))
        self.ShowNew = QtGui.QPushButton(mPequeras)
        self.ShowNew.setGeometry(QtCore.QRect(230, 580, 81, 31))
        self.ShowNew.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowNew.setObjectName(_fromUtf8("ShowNew"))
        self.ShowNone = QtGui.QPushButton(mPequeras)
        self.ShowNone.setGeometry(QtCore.QRect(230, 610, 81, 31))
        self.ShowNone.setStyleSheet(_fromUtf8("border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"background: rgb(104, 104, 104);\n"
"color: white;\n"
""))
        self.ShowNone.setObjectName(_fromUtf8("ShowNone"))
        self.label_6 = QtGui.QLabel(mPequeras)
        self.label_6.setGeometry(QtCore.QRect(170, 20, 71, 16))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 85, 127);\n"
"background: transparent;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.currentItem = QtGui.QListWidget(mPequeras)
        self.currentItem.setGeometry(QtCore.QRect(20, 288, 130, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.currentItem.setFont(font)
        self.currentItem.setStyleSheet(_fromUtf8("color: rgb(255, 150, 21);"))
        self.currentItem.setWordWrap(False)
        self.currentItem.setObjectName(_fromUtf8("currentItem"))

        self.invBg = QtGui.QLabel(mPequeras)
        self.invBg.setGeometry(QtCore.QRect(20, 465, 130, 205))


        self.drop = QtGui.QPlainTextEdit(mPequeras)
        self.drop.setGeometry(610,143,193,20)
        self.drop.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.drop.setStyleSheet('color: white;')
        self.retranslateUi(mPequeras)
        self.yellowsetL = QtGui.QLabel(mPequeras) # Label
        self.yellowsetL.setStyleSheet('color:grey; background: transparent')
        self.yellowsetL.setGeometry(610,553,270,20)
        self.yellowsetL.setText('Set Yellow Options')

        self.yellowwL = QtGui.QLabel(mPequeras) # Label
        self.yellowwL.setStyleSheet('color:grey; background: transparent')
        self.yellowwL.setGeometry(610,603,270,20)
        self.yellowwL.setText('Weapon Yellow Options')

        self.yellow = QtGui.QComboBox(mPequeras) # CBox
        self.yellow.setGeometry(610,573,270,20)
        yelloset = setyellow.set
        self.yellow.addItems(yelloset)
        self.yellow.setStyleSheet('color: white')

        self.wyello = QtGui.QComboBox(mPequeras)
        self.wyello.setStyleSheet('color: white')
        yellowwep = wepyellow.weapon
        self.wyello.addItems(yellowwep)
        self.wyello.setGeometry(610,622,270,20)
# is socket mode?
        self.isSocket = QtGui.QCheckBox(mPequeras)
        self.isSocket.setText('Enable Sockets')
        self.isSocket.setGeometry(QtCore.QRect(420, 250, 93, 20))
        self.isSocket.setStyleSheet('color: rgb(255, 17, 180); background: transparent;')
# is vault mode?
        self.isVaultmode = QtGui.QCheckBox(mPequeras)
        self.isVaultmode.setText('Enable Vault Mode')
        self.isVaultmode.setGeometry(QtCore.QRect(27, 558, 130, 205))
        self.isVaultmode.setStyleSheet('background: transparent; color: grey;')
### 1
        # inventory Buttons as SLOTS
        self.r1c1 = QtGui.QPushButton(mPequeras)
        self.r1c1.setGeometry(QtCore.QRect(20, 450, 33, 30))
        self.r1c1.setStyleSheet('background: grey; color: white;')

        self.r1c2 = QtGui.QPushButton(mPequeras)
        self.r1c2.setGeometry(QtCore.QRect(52, 450, 33, 30))
        self.r1c2.setStyleSheet('background: grey; color: white;')

        self.r1c3 = QtGui.QPushButton(mPequeras)
        self.r1c3.setGeometry(QtCore.QRect(84, 450, 34, 30))
        self.r1c3.setStyleSheet('background: grey; color: white;')

        self.r1c4 = QtGui.QPushButton(mPequeras)
        self.r1c4.setGeometry(QtCore.QRect(117, 450, 33, 30))
        self.r1c4.setStyleSheet('background: grey; color: white;')

### 2
        self.r2c1 = QtGui.QPushButton(mPequeras)
        self.r2c1.setGeometry(QtCore.QRect(20, 479, 33, 30))
        self.r2c1.setStyleSheet('background: grey; color: white;')

        self.r2c2 = QtGui.QPushButton(mPequeras)
        self.r2c2.setGeometry(QtCore.QRect(52, 479, 33, 30))
        self.r2c2.setStyleSheet('background: grey; color: white;')

        self.r2c3 = QtGui.QPushButton(mPequeras)
        self.r2c3.setGeometry(QtCore.QRect(84, 479, 34, 30))
        self.r2c3.setStyleSheet('background: grey; color: white;')

        self.r2c4 = QtGui.QPushButton(mPequeras)
        self.r2c4.setGeometry(QtCore.QRect(117, 479, 33, 30))
        self.r2c4.setStyleSheet('background: grey; color: white;')

### 3
        self.r3c1 = QtGui.QPushButton(mPequeras)
        self.r3c1.setGeometry(QtCore.QRect(20, 508, 33, 30))
        self.r3c1.setStyleSheet('background: grey; color: white;')

        self.r3c2 = QtGui.QPushButton(mPequeras)
        self.r3c2.setGeometry(QtCore.QRect(52, 508, 33, 30))
        self.r3c2.setStyleSheet('background: grey; color: white;')

        self.r3c3 = QtGui.QPushButton(mPequeras)
        self.r3c3.setGeometry(QtCore.QRect(84, 508, 34, 30))
        self.r3c3.setStyleSheet('background: grey; color: white;')

        self.r3c4 = QtGui.QPushButton(mPequeras)
        self.r3c4.setGeometry(QtCore.QRect(117, 508, 33, 30))
        self.r3c4.setStyleSheet('background: grey; color: white;')

### 4
        self.r4c1 = QtGui.QPushButton(mPequeras)
        self.r4c1.setGeometry(QtCore.QRect(20, 537, 33, 30))
        self.r4c1.setStyleSheet('background: grey; color: white;')

        self.r4c2 = QtGui.QPushButton(mPequeras)
        self.r4c2.setGeometry(QtCore.QRect(52, 537, 33, 30))
        self.r4c2.setStyleSheet('background: grey; color: white;')

        self.r4c3 = QtGui.QPushButton(mPequeras)
        self.r4c3.setGeometry(QtCore.QRect(84, 537, 34, 30))
        self.r4c3.setStyleSheet('background: grey; color: white;')

        self.r4c4 = QtGui.QPushButton(mPequeras)
        self.r4c4.setGeometry(QtCore.QRect(117, 537, 33, 30))
        self.r4c4.setStyleSheet('background: grey; color: white;')

### 5
        self.r5c1 = QtGui.QPushButton(mPequeras)
        self.r5c1.setGeometry(QtCore.QRect(20, 566, 33, 30))
        self.r5c1.setStyleSheet('background: grey; color: white;')

        self.r5c2 = QtGui.QPushButton(mPequeras)
        self.r5c2.setGeometry(QtCore.QRect(52, 566, 33, 30))
        self.r5c2.setStyleSheet('background: grey; color: white;')

        self.r5c3 = QtGui.QPushButton(mPequeras)
        self.r5c3.setGeometry(QtCore.QRect(84, 566, 34, 30))
        self.r5c3.setStyleSheet('background: grey; color: white;')

        self.r5c4 = QtGui.QPushButton(mPequeras)
        self.r5c4.setGeometry(QtCore.QRect(117, 566, 33, 30))
        self.r5c4.setStyleSheet('background: grey; color: white;')

### 6
        self.r6c1 = QtGui.QPushButton(mPequeras)
        self.r6c1.setGeometry(QtCore.QRect(20, 595, 33, 30))
        self.r6c1.setStyleSheet('background: grey; color: white;')

        self.r6c2 = QtGui.QPushButton(mPequeras)
        self.r6c2.setGeometry(QtCore.QRect(52, 595, 33, 30))
        self.r6c2.setStyleSheet('background: grey; color: white;')

        self.r6c3 = QtGui.QPushButton(mPequeras)
        self.r6c3.setGeometry(QtCore.QRect(84, 595, 34, 30))
        self.r6c3.setStyleSheet('background: grey; color: white;')

        self.r6c4 = QtGui.QPushButton(mPequeras)
        self.r6c4.setGeometry(QtCore.QRect(117, 595, 33, 30))
        self.r6c4.setStyleSheet('background: grey; color: white;')

### 7
        self.r7c1 = QtGui.QPushButton(mPequeras)
        self.r7c1.setGeometry(QtCore.QRect(20, 624, 33, 30))
        self.r7c1.setStyleSheet('background: grey; color: white;')

        self.r7c2 = QtGui.QPushButton(mPequeras)
        self.r7c2.setGeometry(QtCore.QRect(52, 624, 33, 30))
        self.r7c2.setStyleSheet('background: grey; color: white;')

        self.r7c3 = QtGui.QPushButton(mPequeras)
        self.r7c3.setGeometry(QtCore.QRect(84, 624, 34, 30))
        self.r7c3.setStyleSheet('background: grey; color: white;')

        self.r7c4 = QtGui.QPushButton(mPequeras)
        self.r7c4.setGeometry(QtCore.QRect(117, 624, 33, 30))
        self.r7c4.setStyleSheet('background: grey; color: white;')



        QtCore.QObject.connect(self.customQueries, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CustomQueries)
        QtCore.QObject.connect(self.CastleSiegeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CastleSiege)
        QtCore.QObject.connect(self.itemMaker, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ItemMaker)
        QtCore.QObject.connect(self.minimize, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Minimize)
        QtCore.QObject.connect(self.accountMaker, QtCore.SIGNAL(_fromUtf8("clicked()")), self.AccountMaker)
        QtCore.QObject.connect(self.OptionsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Options)
        QtCore.QObject.connect(self.pkClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.PKClear)
        QtCore.QObject.connect(self.ShowSwords, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showSwords)
        QtCore.QObject.connect(self.saveLogs, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveLogss)
        QtCore.QObject.connect(self.editCharacter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.EditCharacter)
        QtCore.QObject.connect(self.closenow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Close)
        QtCore.QObject.connect(self.ExecuteALL, QtCore.SIGNAL(_fromUtf8("clicked()")), self.executeCodes)
        QtCore.QObject.connect(self.saveCredentials, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveSettings)
        QtCore.QObject.connect(self.premiumItems, QtCore.SIGNAL(_fromUtf8("clicked()")), self.PremiumGearMaker)
        QtCore.QObject.connect(self.fullGearMaker, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FullGearMaker)
        QtCore.QObject.connect(self.ShowAxes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showAxes)
        QtCore.QObject.connect(self.connectNow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connectsNow)
        QtCore.QObject.connect(self.clearallLogs, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearLogs)
        QtCore.QObject.connect(self.ShowMaces, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showMaxes)
        QtCore.QObject.connect(self.ShowScepters, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showScepters)
        QtCore.QObject.connect(self.ShowSpears, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showSpear)
        QtCore.QObject.connect(self.ShowBows, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showBows)
        QtCore.QObject.connect(self.ShowCrossBows, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showCrossbows)
        QtCore.QObject.connect(self.ShowStaffs, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showStaffs)
        QtCore.QObject.connect(self.ShowShields, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showShields)
        QtCore.QObject.connect(self.ShowWings, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showWings)
        QtCore.QObject.connect(self.ShowPets, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showPets)
        QtCore.QObject.connect(self.ShowRings, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showRings)
        QtCore.QObject.connect(self.ShowOrbs, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showOrbs)
        QtCore.QObject.connect(self.ShowScrolls, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showScrolls)
        QtCore.QObject.connect(self.ShowJewels, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showJewels)
        QtCore.QObject.connect(self.ShowPotions, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showPotions)
        QtCore.QObject.connect(self.ShowAmulets, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showAmulets)
        QtCore.QObject.connect(self.ShowEvents, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showEvents)
        QtCore.QObject.connect(self.ShowQuests, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showQuest)
        QtCore.QObject.connect(self.ShowBoxes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showBoxes)
        QtCore.QObject.connect(self.ShowPetMix, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showPetmix)
        QtCore.QObject.connect(self.ShowCastleSiege, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showCastleSiege)
        QtCore.QObject.connect(self.ShowSpears_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showSpears)
        QtCore.QObject.connect(self.ShowNew, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showNew)
        QtCore.QObject.connect(self.ShowNone, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showNone)
        QtCore.QObject.connect(self.ShowHelms, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showHelms)
        QtCore.QObject.connect(self.ShowArmors, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showArmors)
        QtCore.QObject.connect(self.ShowPants, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showPants)
        QtCore.QObject.connect(self.ShowGloves, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showGloves)
        QtCore.QObject.connect(self.ShowBoots, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showBoots)

        ### Start Vault Sluts, i meant Slots
        # 1
        QtCore.QObject.connect(self.r1c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row1c1)
        QtCore.QObject.connect(self.r1c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row1c2)
        QtCore.QObject.connect(self.r1c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row1c3)
        QtCore.QObject.connect(self.r1c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row1c4)
        # 2
        QtCore.QObject.connect(self.r2c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row2c1)
        QtCore.QObject.connect(self.r2c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row2c2)
        QtCore.QObject.connect(self.r2c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row2c3)
        QtCore.QObject.connect(self.r2c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row2c4)
        # 3
        QtCore.QObject.connect(self.r3c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row3c1)
        QtCore.QObject.connect(self.r3c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row3c2)
        QtCore.QObject.connect(self.r3c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row3c3)
        QtCore.QObject.connect(self.r3c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row3c4)

        # 4
        QtCore.QObject.connect(self.r4c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row4c1)
        QtCore.QObject.connect(self.r4c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row4c2)
        QtCore.QObject.connect(self.r4c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row4c3)
        QtCore.QObject.connect(self.r4c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row4c4)

        # 5
        QtCore.QObject.connect(self.r5c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row5c1)
        QtCore.QObject.connect(self.r5c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row5c2)
        QtCore.QObject.connect(self.r5c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row5c3)
        QtCore.QObject.connect(self.r5c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row5c4)

        # 6
        QtCore.QObject.connect(self.r6c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row6c1)
        QtCore.QObject.connect(self.r6c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row6c2)
        QtCore.QObject.connect(self.r6c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row6c3)
        QtCore.QObject.connect(self.r6c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row6c4)

        # 7
        QtCore.QObject.connect(self.r7c1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row7c1)
        QtCore.QObject.connect(self.r7c2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row7c2)
        QtCore.QObject.connect(self.r7c3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row7c3)
        QtCore.QObject.connect(self.r7c4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.row7c4)

        QtCore.QMetaObject.connectSlotsByName(mPequeras)

    def retranslateUi(self, mPequeras):
        mPequeras.setWindowTitle(_translate("mPequeras", "iOnline Creator - Invictuz Online", None))
        mPequeras.setProperty("creditsString", _translate("mPequeras", "asdasdasdasd", None))
        self.Plus.setWindowTitle(_translate("mPequeras", "Plus Lists", None))
        self.premiumItems.setText(_translate("mPequeras", "Premium Items", None))
        self.lineEdit_4.setText(_translate("mPequeras", "1433", None))
        self.lineEdit_4.setPlaceholderText(_translate("mPequeras", "Port:", None))
        self.pkClear.setText(_translate("mPequeras", "PK Clear", None))
        self.fullGearMaker.setText(_translate("mPequeras", "Full Gear Maker", None))
        self.comboBox.setItemText(0, _translate("mPequeras", "Local Connection", None))
        self.comboBox.setItemText(1, _translate("mPequeras", "Remote Connection", None))
        self.lineEdit_2.setPlaceholderText(_translate("mPequeras", "Username:", None))
        self.accountMaker.setText(_translate("mPequeras", "Account Maker", None))
        self.label.setText(_translate("mPequeras", "iMaker", None))
        self.itemMaker.setText(_translate("mPequeras", "Item Maker", None))
        self.connectNow.setText(_translate("mPequeras", "GO", None))
        self.serverPassword.setPlaceholderText(_translate("mPequeras", "Password:", None))
        self.customQueries.setText(_translate("mPequeras", "Custom Queries", None))
        self.serverServer.setPlaceholderText(_translate("mPequeras", "Server:", None))
        self.serverPort.setText(_translate("mPequeras", "1433", None))
        self.serverPort.setPlaceholderText(_translate("mPequeras", "Port:", None))
        self.connectionType.setItemText(0, _translate("mPequeras", "Local Area Connection", None))
        self.connectionType.setItemText(1, _translate("mPequeras", "Remote Connection", None))
        self.serverUsername.setPlaceholderText(_translate("mPequeras", "Username:", None))
        self.closenow.setText(_translate("mPequeras", "✕", None))
        self.MarkPequerasfooter.setText(_translate("mPequeras", "iMaker © Mark Pequeras - CoreSEC Software Development", None))
        self.minimize.setText(_translate("mPequeras", "-", None))
        self.editCharacter.setText(_translate("mPequeras", "Edit Character", None))
        self.OptionsButton.setText(_translate("mPequeras", "Options", None))
        self.CastleSiegeButton.setText(_translate("mPequeras", "Castle Siege", None))
        self.MessageBox.setHtml(_translate("mPequeras", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("mPequeras", "Processes", None))
        self.saveCredentials.setText(_translate("mPequeras", "Save Credentials", None))
        self.saveLogs.setText(_translate("mPequeras", "Save", None))
        self.clearallLogs.setText(_translate("mPequeras", "Clear", None))
        self.ShowSwords.setText(_translate("mPequeras", "Swords", None))
        self.ShowAxes.setText(_translate("mPequeras", "Axes", None))
        self.ShowBows.setText(_translate("mPequeras", "Bows", None))
        self.ShowSpears.setText(_translate("mPequeras", "Spears", None))
        self.ShowMaces.setText(_translate("mPequeras", "Maces", None))
        self.ShowScepters.setText(_translate("mPequeras", "Scepters", None))
        self.ShowCrossBows.setText(_translate("mPequeras", "CrossBows", None))
        self.ShowStaffs.setText(_translate("mPequeras", "Staffs", None))
        self.ShowShields.setText(_translate("mPequeras", "Shields", None))
        self.ShowHelms.setText(_translate("mPequeras", "Helms", None))
        self.usernameBox.setPlaceholderText(_translate("mPequeras", "Username:", None))

        self.itemoptionTitle.setText(_translate("mPequeras", "Item\'s Options", None))
        self.itemOption3.setText(_translate("mPequeras", "Reflect Damage", None))
        self.itemOption5.setText(_translate("mPequeras", "Mana", None))
        self.itemOption1.setText(_translate("mPequeras", "Zen After Hunting", None))
        self.itemOption6.setText(_translate("mPequeras", "HP", None))
        self.itemOption2.setText(_translate("mPequeras", "Defense Success Rate", None))
        self.itemOption4.setText(_translate("mPequeras", "Reduce Damage", None))
        self.Serial.setText(_translate("mPequeras", "<html><head/><body><p>000014CA87A300000040000000000000</p></body></html>", None))
        self.ExecuteALL.setText(_translate("mPequeras", "Execute >>", None))
        self.ShowArmors.setText(_translate("mPequeras", "Armors", None))
        self.ShowPants.setText(_translate("mPequeras", "Pants", None))
        self.ShowGloves.setText(_translate("mPequeras", "Gloves", None))
        self.ShowBoots.setText(_translate("mPequeras", "Boots", None))
        self.ShowWings.setText(_translate("mPequeras", "Wings", None))
        self.ShowPets.setText(_translate("mPequeras", "Pets", None))
        self.ShowRings.setText(_translate("mPequeras", "Rings", None))
        self.ShowOrbs.setText(_translate("mPequeras", "Orbs", None))
        self.ShowScrolls.setText(_translate("mPequeras", "Scrolls", None))
        self.ShowJewels.setText(_translate("mPequeras", "Jewels", None))
        self.ShowPotions.setText(_translate("mPequeras", "Potions", None))
        self.ShowAmulets.setText(_translate("mPequeras", "Amulets", None))
        self.ShowEvents.setText(_translate("mPequeras", "Events", None))
        self.ShowQuests.setText(_translate("mPequeras", "Quests", None))
        self.ShowBoxes.setText(_translate("mPequeras", "Boxes", None))
        self.ShowPetMix.setText(_translate("mPequeras", "Pet Mix", None))
        self.ShowCastleSiege.setText(_translate("mPequeras", "Castle Siege", None))
        self.ShowSpears_2.setText(_translate("mPequeras", "Spears", None))
        self.ShowNew.setText(_translate("mPequeras", "New", None))
        self.ShowNone.setText(_translate("mPequeras", "None", None))
        self.label_6.setText(_translate("mPequeras", "Open-Source", None))
        config = settings # Lets Load Invictuz Settings
        if (config.AutoLoad == 1):
            self.serverServer.setText(str(config.Server))
            self.serverUsername.setText(str(config.User))
            self.serverPassword.setText(str(config.Password))
            if (config.Connection) == 1:
                self.connectionType.setCurrentIndex(1)
            else:
                self.connectionType.setCurrentIndex(0)
                # Configs Loaded ;)


    inUString = "<b><font color=\"red\">I Need Username!</font><b>"
    # Start Main functions

    def connectsNow(self):
        import time
        Authenticated = 0
        run = 0
       # multi / div * 24 # calculated vault slots
        #xx = QtGui.QDialog()
        #xx.setWindowTitle("Aliga")
        #xx.setMaximumSize(123,123)
        #xx.exec_()
        protocol = self.connectionType.currentIndex()
        if protocol == 1:   ## REMOTE
            if self.connected.text() != '1':
                server = self.serverServer.text() # ionline svr
                username = self.serverUsername.text() # ionline usr
                password = self.serverPassword.text() # ionline pwd
                self.query = None
                con = self.con
                cursor = con.cursor()
                executed = cursor.execute("select memb___id from MEMB_INFO")  # select memb___id from MEMB_INFO
                final = executed.fetchall()
                self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"green\">Successfully Remote Connected!</font><br/>")
                self.progressBar.setValue(100)
                time.sleep(2)
                self.progressBar.setValue(0)
                self.connected.setText('1')


            else:
                self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"orange\">Already Connected,This may Exhause your Engine!</font><br/>")


        #if (run > 0):
        #    self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"orange\">Already Connected,This may Exhause your Engine!</font><br/>")
        #    return False
        elif protocol == 0:               ## LOCAL
            if self.connected.text() != '1':
                server = self.serverServer.text() # ionline svr
                username = self.serverUsername.text() # ionline usr
                password = self.serverPassword.text() # ionline pwd
                self.query = None
                con = self.con
                cursor = con.cursor()
                executed = cursor.execute("select memb___id from MEMB_INFO")  # select memb___id from MEMB_INFO
                final = executed.fetchall()
                self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"green\">Successfully Connected Locally!</font><br/>")
                self.progressBar.setValue(100)
                time.sleep(2)
                self.progressBar.setValue(0)
                self.connected.setText('1')
                self.connectNow.setText('Connected')
                self.connectNow.setStyleSheet('background: green; color: white; font-size: 10px; ')
            else:
                self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"orange\">Already Connected,This may Stress your Engine!</font><br/>")

        else:
            self.MessageBox.clear(),self.MessageBox.insertHtml("<b><font color=\"green\">Error Occured, Please Check your Setting's Config!</font><br/>")
    def CustomQueries(self):

        dlg = QtGui.QDialog()
        button = QtGui.QPushButton(dlg)
        dlg.setMaximumHeight(500)
        dlg.setMaximumWidth(200)
        dlg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        button.setText('RUN')
        button.setStyleSheet('background: grey; color: white;')
        button.setGeometry(73,120,90,30)

        buttonc = QtGui.QPushButton(dlg)
        buttonc.setText('Close')
        buttonc.setStyleSheet('background: red; color: white;')
        buttonc.setGeometry(10,120,50,20)
        qbox = QtGui.QPlainTextEdit(dlg)
        qbox.setGeometry(3,20,160,100)

        output = QtGui.QPlainTextEdit(dlg)
        output.setGeometry(3,160,160,200)




        def closer():
            dlg.close()
        def runsql():
            try:
                quer = qbox.toPlainText()
                con = self.con
                cursor = con.cursor()
                execute = cursor.execute(str(quer))
                ex = execute.fetchall()
                output.clear(),output.insertPlainText('iCreator Output: \n\n' + str(ex))
            except:
                output.clear(),output.insertPlainText('Error, Please Check the Syntax or your connection!')
        QtCore.QObject.connect(buttonc, QtCore.SIGNAL(_fromUtf8("clicked()")), closer)
        QtCore.QObject.connect(button, QtCore.SIGNAL(_fromUtf8("clicked()")), runsql)







        dlg.exec_()
    def CastleSiege(self):
        queryx = "select memb_guid from MEMB__INFO"

    def Minimize(self):
        mPequeras.showMinimized()
    def ItemMaker(self):
        pass
    def AccountMaker(self):
        pass
    def Options(self):
        pass
    def PKClear(self):
        pass
    def showSwords(self):
        from swords import sword
        self.Serial.clear(), self.Serial.setText('Swords -3@31Uf941sfQ')
        helmx = list(sword)
        self.currentItem.clear()
        self.currentItem.addItems(helmx)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Swords Loaded Successfully!</b><br>')

    def saveLogss(self):
        pass
    def EditCharacter(self):
        editDlg = QtGui.QDialog()
        usrbox = QtGui.QPlainTextEdit(editDlg)   # USR Box
        usrbox.setGeometry(QtCore.QRect(80,67, 130,20))

        usrbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        text3 = QtGui.QPlainTextEdit(editDlg)   # Log Box
        text3.setGeometry(QtCore.QRect(350,50, 130,220))
        text3.setDisabled(1)
        global text
        text = QtGui.QPlainTextEdit(editDlg)   # Username
        text.setGeometry(QtCore.QRect(120,30, 100,20))
        text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        def clearAll():
            text3.clear()
            usrbox.clear()
            pwbox.clear()
            emailbox.clear()
        def saveMe():
            pass
        def close():

            editDlg.close()


        def button3x():
            query = """
                SELECT
                [memb___id],
                  [memb__pwd],
                  [mail_addr],
                  [fpas_ques],
                  [fpas_answ],
                  [job__code],
                  [appl_days],
                  [modi_days],
                  [out__days],
                  [true_days],
                  [mail_chek],
                  [bloc_code],
                  [ctl1_code],
                  [vip_free],
                  [country],
                  [gender],
                  [SecretQuestion],
                  [SecretAnswer],
                  [SCFIsVip],
                  [SCFVipMoney],
                  [SCFVipDays],
                  [SCFWareVipCount],
                  [SCFLuckyCoins],
                  [SMSPoints],
                  [confirmed],
                  [activation_id],
                  [votes],
                  [Admin],
                  [bank_zen],
                  [bank_pcpoints],
                  [Skype],
                  [vip],
                  [Expired],
                  [SCFExtWarehouse],
                  [WCoin],
                  [WCoinP],
                  [GoblinCoin],
                  [MuItemShopList],
                  [MuItemShopGiftList],
                  [MuItemShopGiftMsg],
                  [GoldChannelTime]
                  FROM MEMB_INFO WHERE memb___id='iOnlineHash'
                    """

            try:
                toEx = open('Settings/db.sql','w+')
                toEx.write(str(query))
                toEx.close()
                toExx = open('Settings/db.sql','r+')
                queries = toExx.read()
                currentusr = text.toPlainText()
                xxx = queries.replace('iOnlineHash', str(currentusr));
                toExx.truncate()
                toExx.close() # close file

                con = self.con
                cursor = con.cursor()
                execute = cursor.execute(xxx)
                out = execute.fetchall()

                for rows in out:
                    row = rows,
                    text3.insertPlainText('Account \"'+str(currentusr)+'\" Informations Loaded Successfully')#str(row))

                usrbox.clear(),usrbox.insertPlainText(str(rows[0]))  # Username
                pwbox.clear(),pwbox.insertPlainText(str(rows[1]))  #Raw Password
                emailbox.clear(),emailbox.insertPlainText(str(rows[2])) # Email
                sabox.clear(),sabox.insertPlainText(str(rows[17])) # Secret A
                svipbox.clear(),svipbox.insertPlainText(str(rows[20])) #vip days
                joinbox.clear(),joinbox.insertPlainText(str(rows[6]))  # joined date
                wcoin.clear(),wcoin.insertPlainText(str(rows[34]))  #wcoins
                wcoinP.clear(),wcoinP.insertPlainText(str(rows[35]))
                gcoinP.clear(),gcoinP.insertPlainText(str(rows[36]))

            except:
                currentusr = usrbox.toPlainText()
                #xxx = queries.replace('iOnlineHash', str(currentusr));
                text3.insertPlainText('Oppps! An error Occured!')


        editDlg.setWindowTitle('Edit Character')
        editDlg.setFixedWidth(500)
        editDlg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        usern = QtGui.QLabel(editDlg) # Username from DB
        usern.setText('Username: ')
        usern.setGeometry(20,70,100,12)
        sa = QtGui.QLabel(editDlg)
        sa.setText('Secret: ')
        sa.setGeometry(38,140,100,12)

        wcoinl = QtGui.QLabel(editDlg)
        wcoinl.setText('WCoins: ')
        wcoinl.setGeometry(26,245,100,12)
        wcoin = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        wcoin.setGeometry(QtCore.QRect(80,240, 50,20))
        wcoin.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        wcoinl2 = QtGui.QLabel(editDlg)
        wcoinl2.setText('WCoinsP: ')
        wcoinl2.setGeometry(26,270,100,12)
        wcoinP = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        wcoinP.setGeometry(QtCore.QRect(80,265, 50,20))
        wcoinP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        gcoinl2 = QtGui.QLabel(editDlg)
        gcoinl2.setText('GPoints: ')
        gcoinl2.setGeometry(26,295,100,12)
        gcoinP = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        gcoinP.setGeometry(QtCore.QRect(80,290, 50,20))
        gcoinP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        sabox = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        sabox.setGeometry(QtCore.QRect(80,137, 130,20))
        sabox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        isvip = QtGui.QLabel(editDlg)
        isvip.setText('VIP Days: ')
        isvip.setGeometry(26,163,100,12)
        svipbox = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        svipbox.setGeometry(QtCore.QRect(80,160, 130,20))
        svipbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        joined = QtGui.QLabel(editDlg)
        joined.setText('Joind Date: ')
        joined.setGeometry(18,187,100,12)
        joinbox = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        joinbox.setGeometry(QtCore.QRect(80,183, 130,20))
        joinbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        pwbox = QtGui.QPlainTextEdit(editDlg)   # PWd Box
        pwbox.setGeometry(QtCore.QRect(80,90, 130,20))
        pwbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        emailbox = QtGui.QPlainTextEdit(editDlg)   # Email Box
        emailbox.setGeometry(QtCore.QRect(80,113, 130,20))
        emailbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        pwd = QtGui.QLabel(editDlg) # Password Label
        pwd.setText('Password: ')
        pwd.setGeometry(22,95,100,12)
        em = QtGui.QLabel(editDlg) # Email from DB
        em.setText('Email: ')
        em.setGeometry(44,117,100,12)
        label = QtGui.QLabel(editDlg)
        label.setText('Search Username: ')
        label.setGeometry(20,35,100,12)
        button3 = QtGui.QPushButton(editDlg)  # Search Username
        button3.setText('Search Now')
        button3.setGeometry(220,30,90,20)
        button3.setStyleSheet('background: grey; color: white;')
        button = QtGui.QPushButton(editDlg)  # Close Button
        button.setText('Close')
        button.setGeometry(QtCore.QRect(400, 0, 81, 31))
        button2 = QtGui.QPushButton(editDlg)   # Save Button
        button2.setText('Save!')
        button2.setGeometry(QtCore.QRect(400, 340, 100, 50))
        button2.setStyleSheet('background: green; color: white;')
        button.setStyleSheet('background: blue; color: white;')
        title = QtGui.QLabel(editDlg)
        title.setText('iOnline Manage Accounts Panel')
        title.setGeometry(187, 350, 220, 50)
        button4 = QtGui.QPushButton(editDlg)   # Save Button
        button4.setText('Clear All')
        button4.setGeometry(QtCore.QRect(30, 350, 81, 31))
        button4.setStyleSheet('background: green; color: white;')
        QtCore.QObject.connect(button, QtCore.SIGNAL(_fromUtf8("clicked()")), close)
        QtCore.QObject.connect(button3, QtCore.SIGNAL(_fromUtf8("clicked()")), button3x)
        QtCore.QObject.connect(button2, QtCore.SIGNAL(_fromUtf8("clicked()")), saveMe)
        QtCore.QObject.connect(button4, QtCore.SIGNAL(_fromUtf8("clicked()")), clearAll)
        editDlg.setFixedHeight(400)
        editDlg.exec_()


    def Close(self):  # Close Window
        sys.exit(0),mPequeras.close()


    def executeCodes(self):
        import random
        try:
            import armors
            import boots
            import gloves
            import helms
            import pants
            import plus
            import swords
        except ImportError:
            self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
        #  14 00 FF 00 3A605E 00 8310
        # 1 . 4 - 1-Item type  4 - item (kb sowrd)
        # 00 - item level / luck / skill
        # 3A605E  - serial (must be unique or else dupe)
        # 00 - item ex option -64 FO
        # 8310 - i dont know hahaha -markie
        resultbox = self.MessageBox
        l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
        plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
        vspace = 'FFFFFFFFFFFFFFFFFFFF'
        slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
#Variables Start
        itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
        itemQuer.truncate()
        username = self.usernameBox.text()
        cuplus = self.Plus.currentItem()
        curitem = self.currentItem.currentItem()
        item = curitem.text()
        theplus = cuplus.text()
        itemType = None
        itemNum = None
        theQuery = None
        iOp1 = 0 #Zen after Huntung
        iOp2 = 0 #DSR
        iOp3 = 0 #ref
        iOp4 = 0 #DD
        iOp5 = 0 #mana
        iOp6 = 0 #hp
#Variables End
        isWeapon = 0
        if self.itemOption1.isChecked() == 1:
            iOp1 = 1
        if self.itemOption2.isChecked() == 1:
            iOp2 = 2
        if self.itemOption3.isChecked() == 1:
            iOp3 = 4
        if self.itemOption4.isChecked() == 1:
            iOp4 = 8
        if self.itemOption5.isChecked() == 1:
            iOp5 = 16
        if self.itemOption6.isChecked() == 1:
            iOp6 = 32

        Chosen = self.Serial.text()
        if 'Armors' in Chosen:
            itemNum = armors.ArmorList.index(item)
            itemType = 8
            itemPlus = theplus
        elif 'Helms' in Chosen:
            itemNum = helms.helmList.index(item)
            itemType = 7
            itemPlus = theplus
        elif 'Pants' in Chosen:
            itemNum = pants.PantsList.index(item)
            itemType = 9
            itemPlus = theplus
        elif 'Gloves' in Chosen:
            itemNum = gloves.GlovesList.index(item)
            itemType = 10
            itemPlus = theplus
        elif 'Boots' in Chosen:
            itemNum = boots.BootsList.index(item)
            itemType = 11
            itemPlus = theplus

        elif 'Swords' in Chosen:
            itemNum = swords.sword.index(item)
            itemType = 0
            itemPlus = theplus
            isWeapon = 1 # Enable Weapon Option
        else:
            print "Error!"




        usr = self.usernameBox.text()
        serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
        serialchar = random.choice("abcdefghigklmnop")
        serial3nums = random.randint(100, 999)
        serialchar2 = random.choice("abcdefghigklmnop")
        generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
        #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
        #generated = '0x0A00FF00002FB2000570000000000000'
        serialize = open('Settings/serialize.sql','w')
        serialize.truncate()
        serialize.write(str(generatedSerial))
        serialize.close()
        oserial = open('Settings/serialize.sql', 'r+')
        rserial = oserial.read()
        try:
            toHex = hex(int(itemNum))
        except:
            tHex = '0x00'

        setJoh = 'None'
        setJohPlus = 'None'
        syellow = self.yellow.currentText()
#'None',
#'Damage Increase',
#'Max AG',
#'Max HP',
#'HP Auto Rate',
#'MN Auto Rate',
#'Damage Success Rate',
#'Damage - Rate +',
#'SD Rate + ',
        if syellow == 'None':
            setJoh = '00'
        elif syellow == 'Damage Increase':
            setJoh = '01'
            setJohPlus = 'D0'
        elif syellow == 'Max AG':
            setJoh = '02'
            setJohPlus = 'D0'
        elif syellow == 'Max HP':
            setJoh = '03'
            setJohPlus = 'D0'
        elif syellow == 'HP Auto Rate':
            setJoh = '04'
            setJohPlus = 'D0'
        elif syellow == 'MN Auto Rate':
            setJoh = '05'
            setJohPlus = 'D0'
        elif syellow == 'Damage Success Rate':
            setJoh = '06'
            setJohPlus = 'D0'
        elif syellow == 'Damage - Rate +':
            setJoh = '07'
            setJohPlus = 'D0'
        elif syellow == 'SD Rate +':
            setJoh = '08'
            setJohPlus = 'D0'
########################################################################################################################
#                     SEPERATED OPTIONS FOR WEAPONS YA KNOW :P
########################################################################################################################




########################################################################################################################
        iNum = toHex.replace('0x','').upper()
        tHex = hex(int(itemType))
        print tHex
        sHex = tHex.replace('0x','').upper()
        exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
        hxOpt = hex(int(exOpt))
        hxsOpt = hxOpt.replace('0x','').upper()
        hxPlus = '00'
        if itemPlus == '1':
            hxPlus = '8F'   # Done
        elif itemPlus == '2':
            hxPlus = '97'   # Done
        elif itemPlus == '3':
            hxPlus = '9F'   # Done
        elif itemPlus == '4':
            hxPlus = 'A7'   # Done
        elif itemPlus == '5':
            hxPlus = 'AF'   # Done
        elif itemPlus == '6':
            hxPlus = 'B7'
        elif itemPlus == '7':
            hxPlus = 'BF'
        elif itemPlus == '8':
            hxPlus = 'C7'
        elif itemPlus == '9':
            hxPlus = 'CF'
        elif itemPlus == '10':
            hxPlus = 'D7'
        elif itemPlus == '11':
            hxPlus = 'DF'
        elif itemPlus == '12':
            hxPlus = 'E7'
        elif itemPlus == '13':
            hxPlus = 'EF'
        elif itemPlus == '14':
            hxPlus = 'F7'
        elif itemPlus == '15':
            hxPlus = 'FF'
        # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

        # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

        isSocketEnabled = self.isSocket.isChecked()

        sockValues = {
        'NO SOCKET' : '00',
        '[Fire]IncreaseSkillAttackPower' : 'C9',
        '[Fire]IncreaseAttackSpeed' : 'CA',
        '[Fire]IncreaseMaximumDamageskill' : 'CB',
        '[Fire]IncreaseMinimumDamageskill' : 'CC',
        '[Fire]DamageSkillPower' : 'CD',
        '[Fire]DecreaseAGuse' : 'CE',
        '[Water]IncreaseDefenseSRate' : 'D3',
        '[Water]IncreaseDefense' : 'D4',
        '[Water]IncreaseDefenseShield' : 'D5',
        '[Water]DamageReduction' : 'D6',
        '[Water]DamageReflection' : 'D7',
        '[Ice]MonsterDieGetLife' : 'D9',
        '[Ice]MonsterDieGetMana' : 'DA',
        '[Ice]IncreaseSkillAttackPower' : 'DB',
        '[Ice]IncreaseAttackSRate' : 'DC',
        '[Ice]IncreaseDurability' : 'DD',
        '[Wind]IncreaseLifeRecovery' : 'DE',
        '[Wind]IncreaseMaximumLife' : 'DF',
        '[Wind]IncreaseMaximumMana' : 'E0',
        '[Wind]IncreaseManaAutoRecovery' : 'E1',
        '[Wind]IncreaseMaximumAG' : 'E2',
        '[Wind]IncreaseAGAmount' : 'E3',
        '[Lightning]IncreaseExcellentDamage' : 'E6',
        '[Lightning]IncreaseExcellentDamageII' : 'E7',
        '[Lightning]IncreaseCriticalDamage' : 'E8',
        '[Lightning]IncreaseCriticalDamageII' : 'E9',
        '[Earth]IncreaseStamina' : 'ED',
        '[  EMPTY SLOT  ]' : 'FF',
        }
        firstSlot = self.checkBox.currentText() #first
        secondSlot = self.checkBox_2.currentText() #second
        thirdSlot = self.checkBox_3.currentText() #third
        fourthSlot = self.checkBox_4.currentText() #fourth
        fifthSlot = self.checkBox_6.currentText() #fifth
        SixthSlot = self.checkBox_7.currentText() #sixth nigga
            # lets some smarter algorithm
        s1 = sockValues[str(firstSlot)]
        s2 = sockValues[str(secondSlot)]
        s3 = sockValues[str(thirdSlot)]
        s4 = sockValues[str(fourthSlot)]
        s5 = sockValues[str(fifthSlot)]
        s6 = sockValues[str(SixthSlot)]
        VaultEnabled = self.isVaultmode.isChecked()
        backupVarVault = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

        fullVault = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
        #if isSocketEnabled == 1: # if enable sockets
            # compatible for invictuzPytech hex > binary > dec
        #    toWrite = '0x{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))

        if VaultEnabled == 1:
            # lets write slots by slots
# [ROW/COLUMN]
# 1 [ROW/COLUM]
            one1 = self.first1
            one2 = self.first2
            one3 = self.first3
            one4 = self.first4
# 2 [ROW/COLUM]
            two1 = self.second1
            two2 = self.second2
            two3 = self.second3
            two4 = self.second4
# 3 [ROW/COLUM]
            three1 = self.third1
            three2 = self.third2
            three3 = self.third3
            three4 = self.third4
# 4 [ROW/COLUM]
            four1 = self.fourth1
            four2 = self.fourth2
            four3 = self.fourth3
            four4 = self.fourth4
# 5 [ROW/COLUM]
            five1 = self.fifth1
            five2 = self.fifth2
            five3 = self.fifth3
            five4 = self.fifth4
# 6 [ROW/COLUM]
            six1 = self.sixth1
            six2 = self.sixth2
            six3 = self.sixth3
            six4 = self.sixth4
# 7 [ROW/COLUM]
            seven1 = self.seventh1
            seven2 = self.seventh2
            seven3 = self.seventh3
            seven4 = self.seventh4
            mxa = 'F'
            multiF = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
            mui = mxa * 644
            #toWrite = '0x{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            toWrite = '0x{a}{BOX}{b}{BOX}{c}{BOX}{d}{BOX}{e}{BOX}{f}{BOX}{g}{BOX}{h}{BOX}{i}{BOX}{j}{BOX}{k}{BOX}{l}{BOX}{m}{BOX}{n}{BOX}{o}{BOX}{p}{BOX}{q}{BOX}{r}{BOX}{s}{BOX}{t}{BOX}{u}{BOX}{v}{BOX}{w}{BOX}{x}{BOX}{y}{BOX}{z}{BOX}{aa}{BOX}{bb}{BOX}{mxu}'.format(a=one1,b=one2,c=one3,d=one4,e=two1,f=two2,g=two3,h=two4,i=three1,j=three2,k=three3,l=three4,m=four1,n=four2,o=four3,p=four4,q=five1,r=five2,s=five3,t=five4,u=six1,v=six2,w=six3,x=six4,y=seven1,z=seven2,aa=seven3,bb=seven4,BOX=multiF,mxu=mui)

        else:
            toWrite = '0x{itemn}{hxpl}FF00000000{xop}00{itemt}{joh}D0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),joh=str(setJoh),fv=str(backupVarVault))


        toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
        serialize.close()

        Q = "UPDATE warehouse SET Items=ITMS WHERE (AccountID='"+str(usr)+"')"
        oserial.close()
        toEx = open('Settings/item.sql','w+')
        toEx.write(str(Q))
        toEx.close()
        # Next
        toExx = open('Settings/item.sql','r+')
        queries = toExx.read()
        xxx = queries.replace('ITMS', str(toWrite))
        self.drop.setPlainText(str(toDrop))
        toExx.truncate()
        toExx.close() # close file
        con = self.con
        cursor = con.cursor()
        execute = cursor.execute(xxx)
        self.con.commit()

        self.MessageBox.insertHtml("<center>-----------------<br><b>Item: "+ str(toWrite) +"</b></br>------------------</center>")

    def PremiumGearMaker(self):
        pass
    def saveSettings(self):
        pass
    def FullGearMaker(self):
        pass
    def showAxes(self):
        pass
    def clearLogs(self):
        self.MessageBox.clear()

    def showMaxes(self):
        pass
    def showSpears(self):
        pass
    def showBoxes(self):
        pass
    def showQuest(self):
        pass
    def showRings(self):
        pass
    def showAmulets(self):
        pass
    def showPets(self):
        pass
    def showNone(self):
        pass
    def showNew(self):
        pass
    def showScepters(self):
        pass
    def showShields(self):
        pass
    def showCrossbows(self):
        pass
    def showJewels(self):
        pass
    def showPetmix(self):
        pass
    def showScrolls(self):
        pass
    def showOrbs(self):
        pass

    def showStaffs(self):
        pass
    def showWings(self):
        pass
    def showBows(self):
        pass
    def showSpear(self):
        pass
    def showPotions(self):
        pass
    def showEvents(self):
        pass
    def showHelms(self):   # HELMS
        import helms
        self.Serial.clear(), self.Serial.setText('Helms -34@1ifQ41sfQ')
        helmx = list(helms.helmList)
        self.currentItem.clear()
        self.currentItem.addItems(helmx)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Helms Loaded Successfully!</b><br>')

    def showArmors(self):  # ARMORS
        import armors
        self.Serial.clear(), self.Serial.setText('Armors -1@31sfQ4x1Zf1')
        armor = armors.ArmorList
        self.currentItem.clear()
        self.currentItem.addItems(armor)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Armors Loaded Successfully!</b><br>')

    def showPants(self):   # PANTS
        import pants
        self.Serial.clear(), self.Serial.setText('Pants -1@31sfQs21sfQ')
        pant = pants.PantsList
        self.currentItem.clear()
        self.currentItem.addItems(pant)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Pants Loaded Successfully!</b><br>')

    def showGloves(self):  # GLOVES
        import gloves
        self.Serial.clear(), self.Serial.setText('Gloves -1@31ZhQ41sfQ')
        glove = gloves.GlovesList
        self.currentItem.clear()
        self.currentItem.addItems(glove)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Gloves Loaded Successfully!</b><br>')

    def showBoots(self):   # BOOTS
        self.Serial.clear(), self.Serial.setText('Boots -1@31sfQ41sfQ')
        import boots
        boot = boots.BootsList
        self.currentItem.clear()
        self.currentItem.addItems(boot)
        self.MessageBox.clear(),self.MessageBox.insertHtml('<b>Boots Loaded Successfully!</b><br>')


    def showPetMix(self):  # Show Pet Items
        pass
    
    def showCastleSiege(self): # Show Castle Siege Items
        pass




#######################################################################################################################
    ######################################## VAULT FUNCTIONS BELOW ######################################################
    #######################################################################################################################
    ########################################################################################################################
#############################################################################################################################

############# VAULT FUNCTIONS STARTS HERE ###################
    # 1

    def row1c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.first1 = mainVar
            print self.first1


            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################

            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r1c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r1c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')






    def row1c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.first2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r1c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r1c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')



    def row1c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.first3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r1c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r1c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row1c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.first4 = mainVar


            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r1c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r1c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')


    # 2
    def row2c1(self):

        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.second1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r2c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r2c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row2c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.second2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r2c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r2c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row2c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.second3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r2c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r2c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row2c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.second4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r2c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r2c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    # 3
    def row3c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.third1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r3c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r3c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
    def row3c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.third2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r3c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r3c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row3c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.third3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r3c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r3c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
    def row3c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.third4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r3c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r3c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
     # 4
    def row4c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fourth1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r4c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r4c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row4c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fourth2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r4c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r4c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row4c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fourth3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r4c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r4c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row4c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fourth4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r4c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r4c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')

    # 5
    def row5c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fifth1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r5c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r5c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')

    def row5c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fifth2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r5c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r5c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row5c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fifth3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r5c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r5c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row5c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.fifth4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r5c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r5c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')

    # 6
    def row6c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.sixth1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r6c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r6c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row6c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.sixth2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r6c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r6c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row6c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.sixth3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r6c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r6c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row6c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.sixth4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r6c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r6c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    # 7
    def row7c1(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.seventh1 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r7c1.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r7c1.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row7c2(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.seventh2 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r7c2.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r7c2.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
    def row7c3(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.seventh3 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r7c3.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r7c3.setText(theString),message.insertPlainText(str(theString)+' Added\n')
    def row7c4(self):
        message = self.MessageBox
        enabled = self.isVaultmode.isChecked()
        if enabled == 1:
            ################################## STARTS ###################################
            import random
            try:
                import armors
                import boots
                import gloves
                import helms
                import pants
                import plus
                import swords
            except ImportError:
                self.MessageBox.clear(),self.MessageBox.insertPlainText('There\'s Something wrong with the Item\'s List!')
            #  14 00 FF 00 3A605E 00 8310
            # 1 . 4 - 1-Item type  4 - item (kb sowrd)
            # 00 - item level / luck / skill
            # 3A605E  - serial (must be unique or else dupe)
            # 00 - item ex option -64 FO
            # 8310 - i dont know hahaha -markie
            resultbox = self.MessageBox
            l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15 = '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
            plusLists = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,]
            vspace = 'FFFFFFFFFFFFFFFFFFFF'
            slots = vspace * 120# Blank Slots of Vault Converted to binary afterwards.
    #Variables Start
            itemQuer = open('Settings/item.sql','r+') # write no replace / dont forget to close this mark.
            itemQuer.truncate()
            username = self.usernameBox.text()
            cuplus = self.Plus.currentItem()
            curitem = self.currentItem.currentItem()
            item = curitem.text()
            theplus = cuplus.text()
            itemType = None
            itemNum = None
            theQuery = None
            iOp1 = 0 #Zen after Huntung
            iOp2 = 0 #DSR
            iOp3 = 0 #ref
            iOp4 = 0 #DD
            iOp5 = 0 #mana
            iOp6 = 0 #hp
    #Variables End
            isWeapon = 0
            if self.itemOption1.isChecked() == 1:
                iOp1 = 1
            if self.itemOption2.isChecked() == 1:
                iOp2 = 2
            if self.itemOption3.isChecked() == 1:
                iOp3 = 4
            if self.itemOption4.isChecked() == 1:
                iOp4 = 8
            if self.itemOption5.isChecked() == 1:
                iOp5 = 16
            if self.itemOption6.isChecked() == 1:
                iOp6 = 32

            Chosen = self.Serial.text()
            if 'Armors' in Chosen:
                itemNum = armors.ArmorList.index(item)
                itemType = 8
                itemPlus = theplus
            elif 'Helms' in Chosen:
                itemNum = helms.helmList.index(item)
                itemType = 7
                itemPlus = theplus
            elif 'Pants' in Chosen:
                itemNum = pants.PantsList.index(item)
                itemType = 9
                itemPlus = theplus
            elif 'Gloves' in Chosen:
                itemNum = gloves.GlovesList.index(item)
                itemType = 10
                itemPlus = theplus
            elif 'Boots' in Chosen:
                itemNum = boots.BootsList.index(item)
                itemType = 11
                itemPlus = theplus

            elif 'Swords' in Chosen:
                itemNum = swords.sword.index(item)
                itemType = 0
                itemPlus = theplus
                isWeapon = 1 # Enable Weapon Option
            else:
                print "Error!"




            usr = self.usernameBox.text()
            serialnum = random.randrange(9)  # UPDATE warehouse SET items=0x7DDCFF00000000FF4076FFFFFFFFFFFFFFFFFFFF5
            serialchar = random.choice("abcdefghigklmnop")
            serial3nums = random.randint(100, 999)
            serialchar2 = random.choice("abcdefghigklmnop")
            generatedSerial = str(serialchar).upper()  + str(serialchar2).upper() + str(serialnum) + str(serialchar).upper() + str(serial3nums) + str(serialchar2).upper()
            #generated = str(itemType)+str(itemNum)+str(itemPlus)+str(generatedSerial)+'8310'+str(vspace)
            #generated = '0x0A00FF00002FB2000570000000000000'
            serialize = open('Settings/serialize.sql','w')
            serialize.truncate()
            serialize.write(str(generatedSerial))
            serialize.close()
            oserial = open('Settings/serialize.sql', 'r+')
            rserial = oserial.read()
            try:
                toHex = hex(int(itemNum))
            except:
                tHex = '0x00'

            setJoh = 'None'
            setJohPlus = 'None'
            syellow = self.yellow.currentText()
    #'None',
    #'Damage Increase',
    #'Max AG',
    #'Max HP',
    #'HP Auto Rate',
    #'MN Auto Rate',
    #'Damage Success Rate',
    #'Damage - Rate +',
    #'SD Rate + ',
            if syellow == 'None':
                setJoh = '00'
            elif syellow == 'Damage Increase':
                setJoh = '01'
                setJohPlus = 'D0'
            elif syellow == 'Max AG':
                setJoh = '02'
                setJohPlus = 'D0'
            elif syellow == 'Max HP':
                setJoh = '03'
                setJohPlus = 'D0'
            elif syellow == 'HP Auto Rate':
                setJoh = '04'
                setJohPlus = 'D0'
            elif syellow == 'MN Auto Rate':
                setJoh = '05'
                setJohPlus = 'D0'
            elif syellow == 'Damage Success Rate':
                setJoh = '06'
                setJohPlus = 'D0'
            elif syellow == 'Damage - Rate +':
                setJoh = '07'
                setJohPlus = 'D0'
            elif syellow == 'SD Rate +':
                setJoh = '08'
                setJohPlus = 'D0'

            iNum = toHex.replace('0x','').upper()
            tHex = hex(int(itemType))
            sHex = tHex.replace('0x','').upper()
            exOpt = iOp1 + iOp2 + iOp3 + iOp4 + iOp5 + iOp6
            hxOpt = hex(int(exOpt))
            hxsOpt = hxOpt.replace('0x','').upper()
            hxPlus = '00'
            if itemPlus == '1':
                hxPlus = '8F'   # Done
            elif itemPlus == '2':
                hxPlus = '97'   # Done
            elif itemPlus == '3':
                hxPlus = '9F'   # Done
            elif itemPlus == '4':
                hxPlus = 'A7'   # Done
            elif itemPlus == '5':
                hxPlus = 'AF'   # Done
            elif itemPlus == '6':
                hxPlus = 'B7'
            elif itemPlus == '7':
                hxPlus = 'BF'
            elif itemPlus == '8':
                hxPlus = 'C7'
            elif itemPlus == '9':
                hxPlus = 'CF'
            elif itemPlus == '10':
                hxPlus = 'D7'
            elif itemPlus == '11':
                hxPlus = 'DF'
            elif itemPlus == '12':
                hxPlus = 'E7'
            elif itemPlus == '13':
                hxPlus = 'EF'
            elif itemPlus == '14':
                hxPlus = 'F7'
            elif itemPlus == '15':
                hxPlus = 'FF'
            # 0x{itemn}7FFF00000000{xop}00{itemt}000000000000

            # 0x{itemn}{hxpl}FF00000000{xop}00{itemt}0000000000000

            isSocketEnabled = self.isSocket.isChecked()

            sockValues = {
            'NO SOCKET' : '00',
            '[Fire]IncreaseSkillAttackPower' : 'C9',
            '[Fire]IncreaseAttackSpeed' : 'CA',
            '[Fire]IncreaseMaximumDamageskill' : 'CB',
            '[Fire]IncreaseMinimumDamageskill' : 'CC',
            '[Fire]DamageSkillPower' : 'CD',
            '[Fire]DecreaseAGuse' : 'CE',
            '[Water]IncreaseDefenseSRate' : 'D3',
            '[Water]IncreaseDefense' : 'D4',
            '[Water]IncreaseDefenseShield' : 'D5',
            '[Water]DamageReduction' : 'D6',
            '[Water]DamageReflection' : 'D7',
            '[Ice]MonsterDieGetLife' : 'D9',
            '[Ice]MonsterDieGetMana' : 'DA',
            '[Ice]IncreaseSkillAttackPower' : 'DB',
            '[Ice]IncreaseAttackSRate' : 'DC',
            '[Ice]IncreaseDurability' : 'DD',
            '[Wind]IncreaseLifeRecovery' : 'DE',
            '[Wind]IncreaseMaximumLife' : 'DF',
            '[Wind]IncreaseMaximumMana' : 'E0',
            '[Wind]IncreaseManaAutoRecovery' : 'E1',
            '[Wind]IncreaseMaximumAG' : 'E2',
            '[Wind]IncreaseAGAmount' : 'E3',
            '[Lightning]IncreaseExcellentDamage' : 'E6',
            '[Lightning]IncreaseExcellentDamageII' : 'E7',
            '[Lightning]IncreaseCriticalDamage' : 'E8',
            '[Lightning]IncreaseCriticalDamageII' : 'E9',
            '[Earth]IncreaseStamina' : 'ED',
            '[  EMPTY SLOT  ]' : 'FF',
            }
            firstSlot = self.checkBox.currentText() #first
            secondSlot = self.checkBox_2.currentText() #second
            thirdSlot = self.checkBox_3.currentText() #third
            fourthSlot = self.checkBox_4.currentText() #fourth
            fifthSlot = self.checkBox_6.currentText() #fifth
            SixthSlot = self.checkBox_7.currentText() #sixth nigga
                # lets some smarter algorithm
            s1 = sockValues[str(firstSlot)]
            s2 = sockValues[str(secondSlot)]
            s3 = sockValues[str(thirdSlot)]
            s4 = sockValues[str(fourthSlot)]
            s5 = sockValues[str(fifthSlot)]
            s6 = sockValues[str(SixthSlot)]
            mainVar = '{itemn}{hxpl}FF00000000{xop}00{itemt}000{is1}{is2}{is3}{is4}{is5}'.format(itemn=str(iNum),hxpl=str(hxPlus),xop=str(hxsOpt),itemt=str(sHex),is1=str(s1),is2=str(s2),is3=str(s3),is4=str(s4),is5=str(s5))
            self.seventh4 = mainVar



            toDrop = '/drop {itemTypes} {itemNums} {itemPluses} {skill} {luck} {exeop}'.format(itemTypes=itemType,itemNums=itemNum,itemPluses=itemPlus,skill='1',luck='1',exeop='32')
            serialize.close()
################################## FUNCTION END ###################################
            theBox = self.currentItem.currentItem()
            theString = theBox.text()
            self.r7c4.setStyleSheet('background: orange;font: 7px;color: black;')
            self.r7c4.setText(theString),message.insertPlainText(str(theString)+' Added\n')
        else:
            message.insertPlainText('You are not in Vault Mode!\n')
mark = 'mark'
if mark == "mark": # Disable if wrong signature
    import sys
    import win32api
    app = QtGui.QApplication(sys.argv)
    mPequeras = QtGui.QWidget()
    mPequeras.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = Ui_mPequeras()
    ui.setupUi(mPequeras)
    mPequeras.show()
    sys.exit(app.exec_())

