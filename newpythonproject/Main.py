# -*- coding: utf-8 -*-
#include <QColorDialog>

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

from Selectorcolor import Ui_MainWindow

class Selectorcolor(QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        super(Selectorcolor,self).__init__(parent)
        self.setupUi(self)
        self.centraFinestra()
        self.red = 0
        self.green = 0
        self.blue = 0
        QtCore.QObject.connect(self.paletButton, QtCore.SIGNAL("clicked()"), self.color)
        QtCore.QObject.connect(self.sButton, QtCore.SIGNAL("clicked()"), self.sortir)
        
    def color(self):
        rojo = int(self.numRed.text())
        verde = int(self.numGreen.text())
        azul = int(self.numBlue.text())
        auxcolor = QColor(rojo, verde, azul, 1)
        color = QtGui.QColorDialog.getColor(auxcolor,self)
        self.redSlider.setValue(color.red())
        self.greenSlider.setValue(color.green())
        self.blueSlider.setValue(color.blue())
        
        
    def sortir(self):
        app.quit()
        
    def centraFinestra(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def recalcula(self):
        self.lineColor.setText("#"+self.hex(self.redSlider.value())+(self.hex(self.greenSlider.value()))+(self.hex(self.blueSlider.value())))
        self.colorLabel.setStyleSheet("QLabel { background-color: rgb("+str(self.redSlider.value())+","+str(self.greenSlider.value())+","+str(self.blueSlider.value())+"); }")
        
    def hex(self, n):
        if n <= 1:
            return str(n)
        else:
            l = ""
            hexa = ""
            while n > 0:
                h = n % 16
                if h < 10:
                    l = str(h)
                elif h == 10:
                    l = "A"
                elif h == 11:
                    l = "B"    
                elif h == 12:
                    l = "C"
                elif h == 13:
                    l = "D"
                elif h == 14:
                    l = "E"
                elif h == 15:
                    l = "F"
                hexa = l + hexa
                n = n / 16
            return str(hexa)    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Selectorcolor()
    finestra.show()
    sys.exit(app.exec_())
