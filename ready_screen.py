# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ready_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets


def show_ready_window(window):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


class Ui_readyWindow(object):
    def __init__(self, Client):
        self.client = Client


    def setupUi(self, readyWindow):
        readyWindow.setObjectName("readyWindow")
        readyWindow.resize(800, 600)
        readyWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(readyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(40, 0, 721, 381))
        self.logo.setObjectName("logo")
        self.logo.setPixmap(QtGui.QPixmap(":/photos3/logo4.png"))
        self.ready_button = QtWidgets.QPushButton(self.centralwidget)
        self.ready_button.setGeometry(QtCore.QRect(150, 400, 211, 71))
        self.ready_button.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                        "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                        "")
        self.ready_button.setObjectName("ready_button")
        self.waiting_text = QtWidgets.QLabel(self.centralwidget)
        self.waiting_text.setGeometry(QtCore.QRect(140, 480, 481, 41))
        self.waiting_text.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                        "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                        "font-color: rgb(255, 255, 255)")
        self.waiting_text.setObjectName("waiting_text")
        self.waiting_text.hide()
        self.dot1 = QtWidgets.QLabel(self.centralwidget)
        self.dot1.setGeometry(QtCore.QRect(630, 480, 16, 41))
        self.dot1.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                "font-color: rgb(255, 255, 255)")
        self.dot1.setObjectName("dot1")
        self.dot1.hide()
        self.dot2 = QtWidgets.QLabel(self.centralwidget)
        self.dot2.setGeometry(QtCore.QRect(650, 480, 16, 41))
        self.dot2.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                "font-color: rgb(255, 255, 255)")
        self.dot2.setObjectName("dot2")
        self.dot2.hide()
        self.dot3 = QtWidgets.QLabel(self.centralwidget)
        self.dot3.setGeometry(QtCore.QRect(670, 480, 16, 41))
        self.dot3.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                "font-color: rgb(255, 255, 255)")
        self.dot3.setObjectName("dot3")
        self.dot3.hide()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 400, 261, 71))
        self.pushButton.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                      "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.hide()
        readyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(readyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        readyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(readyWindow)
        self.statusbar.setObjectName("statusbar")
        readyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(readyWindow)
        QtCore.QMetaObject.connectSlotsByName(readyWindow)
        self.check_for_button(readyWindow)

    def retranslateUi(self, readyWindow):
        _translate = QtCore.QCoreApplication.translate
        readyWindow.setWindowTitle(_translate("readyWindow", "MainWindow"))
        self.logo.setText(
            _translate("readyWindow", "<html><head/><body><p><img src=\":/photos2/logo3.png\"/></p></body></html>"))
        self.ready_button.setText(_translate("readyWindow", "ready-up"))
        self.waiting_text.setText(_translate("readyWindow",
                                             "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">waiting for other players</span></p></body></html>"))
        self.dot1.setText(_translate("readyWindow",
                                     "<html><head/><body><p><span style=\" color:#ffffff;\">.</span></p></body></html>"))
        self.dot2.setText(_translate("readyWindow",
                                     "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">.</span></p></body></html>"))
        self.dot3.setText(_translate("readyWindow",
                                     "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">.</span></p></body></html>"))
        self.pushButton.setText(_translate("readyWindow", "cancel ready"))

    def check_for_button(self, MainWindow):
        self.ready_button.clicked.connect(lambda: self.readypressed(MainWindow))
        self.pushButton.clicked.connect(lambda: self.cancelpressed(MainWindow))

    def readypressed(self, MainWindow):
        print("ready pressed")
        self.waiting_text.show()
        self.ready_button.hide()
        self.client.client_ready = True

    def cancelpressed(self, MainWindow):
        print("cancel pressed")
        self.ready_button.show()
        self.waiting_text.hide()
        self.dot1.hide()
        self.dot2.hide()
        self.dot3.hide()
        self.pushButton.hide()
        self.client.client_ready = False

    def loading_animation(self):
        while True:
            self.dot1.show()
            time.sleep(1)
            self.dot2.show()
            time.sleep(1)
            self.dot3.show()
            time.sleep(1)
            self.dot1.hide()
            self.dot2.hide()
            self.dot3.hide()
            time.sleep(1)

import photos2
