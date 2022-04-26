import projekat, akcije

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import numpy as np
from PyQt5 import sip

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class newMainWindow(projekat.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        
    def addCanvas(self, static_canvas):
        self.deleteLayout(self.frame.layout())
        layout = QtWidgets.QVBoxLayout(self.frame)

        layout.addWidget(NavigationToolbar(static_canvas, self.frame))
        layout.addWidget(static_canvas)

    def addWebPage(self):
        self.deleteLayout(self.frame.layout())
        layout = QtWidgets.QVBoxLayout(self.frame)
        noviWebView = akcije.napraviVebView()
        layout.addWidget(noviWebView)



    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)

    def ucitajVrednosti(self, MainWindow):
        try:
            x = float(self.unosX.text())
            y = float(self.unosY.text())
            g = float(self.unosG.text())
            if x<=0 or y<=0 or g<=0:
                raise Exception
        except:
            poruka = QMessageBox(MainWindow)
            poruka.setText("X, Y, g moraju biti pozitivni realni brojevi")
            poruka.show()
            return (-1, -1, -1)
        
        return x,y,g

def odabirAkcije():

    if ui.comboBox.currentText() == "Istorija":
        ui.addWebPage()
    else:
        kanvas = None
        x, y, g = ui.ucitajVrednosti(MainWindow)
        if x == -1:
            return

        if ui.comboBox.currentText() == "Animacija":
            pass
        else:
            kanvas = akcije.nacrtajSve(x, y, g)

        ui.addCanvas(kanvas)
    


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = newMainWindow()
ui.setupUi(MainWindow)
MainWindow.setFixedSize(700, 700)
MainWindow.show()


ui.pushButton.clicked.connect(odabirAkcije)
#dodajGrafik(ui.frame)
sys.exit(app.exec_())


