import projekat, akcije

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
from PyQt5 import sip
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

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
        noviWebView = QWebView()
        noviWebView.setUrl(QtCore.QUrl("https://alas.matf.bg.ac.rs/~mi20015/index.html"))
        noviWebView.setObjectName("webView")
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

''' stara funkcija
def dodajGrafik(frame):
    print(str(frame.layout()))
    
    layout = QtWidgets.QVBoxLayout(frame)

    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    layout.addWidget(NavigationToolbar(static_canvas, frame))
    layout.addWidget(static_canvas)

    _static_ax = static_canvas.figure.subplots()
    t = np.linspace(0, 10, 501)
    _static_ax.plot(t, np.tan(t), ".")
'''

def odabirAkcije():
    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    
    _static_ax = static_canvas.figure.subplots()
    t = np.linspace(0, 10, 501)


    if ui.comboBox.currentText() == "Grafik":
        _static_ax.plot(t, np.tan(t), ".")
        ui.addCanvas(static_canvas)
    elif ui.comboBox.currentText() == "Animacija":
        _static_ax.plot(t, np.cos(t), ".")
        ui.addCanvas(static_canvas)
    else:
        ui.addWebPage()

    
    


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = newMainWindow()
ui.setupUi(MainWindow)
MainWindow.setFixedSize(700, 700)
MainWindow.show()


ui.pushButton.clicked.connect(odabirAkcije)
#dodajGrafik(ui.frame)
sys.exit(app.exec_())


