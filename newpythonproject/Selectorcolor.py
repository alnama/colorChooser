# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Nov 17 20:08:11 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 250)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.greenSlider = QtGui.QSlider(self.centralWidget)
        self.greenSlider.setGeometry(QtCore.QRect(140, 90, 231, 29))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName(_fromUtf8("greenSlider"))
        self.blueSlider = QtGui.QSlider(self.centralWidget)
        self.blueSlider.setGeometry(QtCore.QRect(140, 150, 231, 29))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName(_fromUtf8("blueSlider"))
        self.redSlider = QtGui.QSlider(self.centralWidget)
        self.redSlider.setGeometry(QtCore.QRect(140, 30, 231, 29))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName(_fromUtf8("redSlider"))
        self.paletButton = QtGui.QPushButton(self.centralWidget)
        self.paletButton.setGeometry(QtCore.QRect(10, 210, 331, 28))
        self.paletButton.setStyleSheet(_fromUtf8("background-color: rgb(128, 152, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.paletButton.setObjectName(_fromUtf8("paletButton"))
        self.sButton = QtGui.QPushButton(self.centralWidget)
        self.sButton.setGeometry(QtCore.QRect(360, 210, 102, 28))
        self.sButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 162, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.sButton.setObjectName(_fromUtf8("sButton"))
        self.redLabel = QtGui.QLabel(self.centralWidget)
        self.redLabel.setGeometry(QtCore.QRect(390, 30, 69, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.redLabel.setFont(font)
        self.redLabel.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.redLabel.setObjectName(_fromUtf8("redLabel"))
        self.greenLabel = QtGui.QLabel(self.centralWidget)
        self.greenLabel.setGeometry(QtCore.QRect(390, 90, 69, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.greenLabel.setFont(font)
        self.greenLabel.setStyleSheet(_fromUtf8("color: rgb(5, 255, 0);"))
        self.greenLabel.setObjectName(_fromUtf8("greenLabel"))
        self.blueLabel = QtGui.QLabel(self.centralWidget)
        self.blueLabel.setGeometry(QtCore.QRect(390, 150, 69, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.blueLabel.setFont(font)
        self.blueLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.blueLabel.setObjectName(_fromUtf8("blueLabel"))
        self.lineColor = QtGui.QLineEdit(self.centralWidget)
        self.lineColor.setGeometry(QtCore.QRect(10, 150, 113, 28))
        self.lineColor.setReadOnly(True)
        self.lineColor.setObjectName(_fromUtf8("lineColor"))
        self.numRed = QtGui.QLabel(self.centralWidget)
        self.numRed.setGeometry(QtCore.QRect(450, 30, 69, 18))
        self.numRed.setObjectName(_fromUtf8("numRed"))
        self.numGreen = QtGui.QLabel(self.centralWidget)
        self.numGreen.setGeometry(QtCore.QRect(450, 90, 69, 18))
        self.numGreen.setObjectName(_fromUtf8("numGreen"))
        self.numBlue = QtGui.QLabel(self.centralWidget)
        self.numBlue.setGeometry(QtCore.QRect(450, 150, 69, 18))
        self.numBlue.setObjectName(_fromUtf8("numBlue"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(20, 190, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.colorLabel = QtGui.QLabel(self.centralWidget)
        self.colorLabel.setGeometry(QtCore.QRect(10, 30, 111, 101))
        self.colorLabel.setAutoFillBackground(False)
        self.colorLabel.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;"))
        self.colorLabel.setText(_fromUtf8(""))
        self.colorLabel.setTextFormat(QtCore.Qt.AutoText)
        self.colorLabel.setObjectName(_fromUtf8("colorLabel"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.redSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.numRed.setNum)
        QtCore.QObject.connect(self.greenSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.numGreen.setNum)
        QtCore.QObject.connect(self.blueSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.numBlue.setNum)
        QtCore.QObject.connect(self.blueSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.recalcula)
        QtCore.QObject.connect(self.greenSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.recalcula)
        QtCore.QObject.connect(self.redSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.recalcula)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Selector de colors (by NavasPutoAmo)", None))
        self.paletButton.setText(_translate("MainWindow", "Paleta de colors", None))
        self.sButton.setText(_translate("MainWindow", "Sortir", None))
        self.redLabel.setText(_translate("MainWindow", "RED", None))
        self.greenLabel.setText(_translate("MainWindow", "GREEN", None))
        self.blueLabel.setText(_translate("MainWindow", "BLUE", None))
        self.numRed.setText(_translate("MainWindow", "0", None))
        self.numGreen.setText(_translate("MainWindow", "0", None))
        self.numBlue.setText(_translate("MainWindow", "0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

