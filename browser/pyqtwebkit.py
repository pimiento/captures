#!/usr/bin/env python2
"""
********************* VerySimpleWebBrowser ************************

    This is a Very Simple Web Browser implemented over Qt and QtWebKit.

    author: Juan Manuel Garcia <jmg.utn@gmail.com>

*******************************************************************
"""

import os
import sys
import base64
from camera import take_picture
from PyQt4 import QtCore, QtGui, QtWebKit

class IFace(QtCore.QObject):
    @QtCore.pyqtSlot(result=str)
    def takePhoto(self):
        return base64.b64encode(take_picture())

class Browser(QtGui.QMainWindow):

    def __init__(self):
        """
            Initialize the browser GUI and connect the events
        """

        QtGui.QMainWindow.__init__(self)
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.iface = IFace(self)
        self.html.page().mainFrame().addToJavaScriptWindowObject(
            "iface", self.iface)

        self.url = "http://localhost:8000"
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())
