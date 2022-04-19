import projekat
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure



def dodajGrafik(frame):
    layout = QtWidgets.QVBoxLayout(frame)

    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    layout.addWidget(NavigationToolbar(static_canvas, frame))
    layout.addWidget(static_canvas)

    _static_ax = static_canvas.figure.subplots()
    t = np.linspace(0, 10, 501)
    _static_ax.plot(t, np.tan(t), ".")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = projekat.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setFixedSize(700, 700)
MainWindow.show()


dodajGrafik(ui.frame)
sys.exit(app.exec_())


