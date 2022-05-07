from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

brojTacaka = 1000

def napraviVebView():
    noviWebView = QWebView()
    noviWebView.setUrl(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo("site/index.html").absoluteFilePath()))
    noviWebView.setObjectName("webView")
    return noviWebView

def vremeZaDuz(x1, y1, x2, y2, g):
    x = x2-x1
    y = y2-y1

    put = np.sqrt(x**2 + y**2)
    sinusUgla = x/put
    ubrzanje = g*sinusUgla
    vreme = np.sqrt(2*put/ubrzanje)

    return vreme

def vrednostiDuz(x, y, g):
    k = y/x
    xs = np.linspace(0, x, brojTacaka)
    ys = (k) * xs #koeficijent
    vreme = 0

    for i in range(0, brojTacaka-1):
        vreme = vreme + vremeZaDuz(xs[i], ys[i], xs[i+1], ys[i+1], g)

    return xs, ys, vreme

#krug cija je tangenta u (0,0) y osa
def vrednostiKrug(x, y, g):
    r = (x**2+y**2) / (2*x)
    xs = np.linspace(0, x, brojTacaka)
    ys = np.sqrt(r**2 - (r-xs)**2)
    vreme = 0

    for i in range(0, brojTacaka-1):
        vreme = vreme + vremeZaDuz(xs[i], ys[i], xs[i+1], ys[i+1], g)

    return xs, ys, vreme

def nacrtajSve(x, y, g):
    kanvas = FigureCanvas(Figure(figsize=(5, 3)))
    ax = kanvas.figure.subplots()

    xsDuz, ysDuz, tDuz = vrednostiDuz(x, y, g)
    ax.plot(xsDuz, ysDuz, label = 'Prava: {:.5f} s'.format(tDuz))

    xsKrug, ysKrug, tKrug = vrednostiKrug(x, y, g)
    ax.plot(xsKrug, ysKrug, label = 'Krug: {:.5f} s'.format(tKrug))

    ax.set_aspect('equal')
    ax.legend()
    ax.invert_yaxis()

    return kanvas
