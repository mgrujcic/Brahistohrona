from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

brojTacaka = 1000

def napraviVebView():
    noviWebView = QWebView()
    noviWebView.setUrl(QtCore.QUrl("https://alas.matf.bg.ac.rs/~mi20015/index.html"))
    noviWebView.setObjectName("webView")
    return noviWebView

def vrednostiDuz(x, y, g):

    k = y/x
    xs = np.linspace(0, x, brojTacaka)
    ys = (k) * xs #koeficijent

    put = np.sqrt(x**2 + y**2)
    sinusUgla = x/put
    ubrzanje = g*sinusUgla
    vreme = np.sqrt(2*put/ubrzanje)

    return xs, ys, vreme

#krug cija je tangenta u (0,0) y osa


def vrednostiKrug(x, y, g):
    r = (x**2+y**2) / (2*x)


def nacrtajSve(x, y, g):
    
    kanvas = FigureCanvas(Figure(figsize=(5, 3)))
    
    ax = kanvas.figure.subplots()

    xsDuz, ysDuz, tDuz = vrednostiDuz(x, y, g)
    ax.plot(xsDuz, ysDuz, label = 'Prava: {:.5f} s'.format(tDuz))

    
    ax.legend()
    ax.invert_yaxis()



    return kanvas





