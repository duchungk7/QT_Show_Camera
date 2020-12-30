# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myShowCamera.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonCamera = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCamera.setGeometry(QtCore.QRect(20, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonCamera.setFont(font)
        self.buttonCamera.setObjectName("buttonCamera")
        self.LabelFrame = QtWidgets.QLabel(self.centralwidget)
        self.LabelFrame.setGeometry(QtCore.QRect(20, 70, 640, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelFrame.setFont(font)
        self.LabelFrame.setAutoFillBackground(True)
        self.LabelFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.LabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LabelFrame.setLineWidth(1)
        self.LabelFrame.setMidLineWidth(1)
        self.LabelFrame.setText("")
        self.LabelFrame.setObjectName("LabelFrame")
        self.buttonCapture = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCapture.setGeometry(QtCore.QRect(200, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonCapture.setFont(font)
        self.buttonCapture.setObjectName("buttonCapture")
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setGeometry(QtCore.QRect(20, 560, 641, 21))
        self.labelInfo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TUL AOI SYSTEM"))
        self.buttonCamera.setText(_translate("MainWindow", "Camera"))
        self.buttonCapture.setText(_translate("MainWindow", "Capture Screen Shot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
