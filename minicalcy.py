# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minicalcy.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(170, 90, 113, 22))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.t2.setObjectName("t2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionCube = QtWidgets.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.actionSqrRoot = QtWidgets.QAction(MainWindow)
        self.actionSqrRoot.setObjectName("actionSqrRoot")
        self.actionCubeRoot = QtWidgets.QAction(MainWindow)
        self.actionCubeRoot.setObjectName("actionCubeRoot")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSquare)
        self.menuFile.addAction(self.actionCube)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSqrRoot)
        self.menuFile.addAction(self.actionCubeRoot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number:"))
        self.label_2.setText(_translate("MainWindow", "Result:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionCube.setText(_translate("MainWindow", "Cube"))
        self.actionSqrRoot.setText(_translate("MainWindow", "SqrRoot"))
        self.actionCubeRoot.setText(_translate("MainWindow", "CubeRoot"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
    def menufunction(self, action):
        txt= (action.text())
        no=int(self.t1.text())
        print (txt, no)
        if txt =='Square':
            self.t2.setText(str(no*no))
        if txt =='Cube':
            self.t2.setText(str(no*no*no))
        if txt =='SqrRoot':
            self.t2.setText(str(math.sqrt(no)))
        if txt=='CubeRoot':
            self.t2.setText(str(math.pow(no,1/3)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
