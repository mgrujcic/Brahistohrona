from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from scipy.optimize import fsolve

brojTacaka = 1000

def napraviVebView(path):
    noviWebView = QWebView()
    noviWebView.setUrl(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath()))
    noviWebView.setObjectName("webView")
    return noviWebView

def resiKvadratnuJednacinu(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    if x1 > 0:
        return x1
    return x2

def vremeZaDuz(x1, y1, x2, y2, g):
    x = x2-x1
    y = y2-y1

    put = np.sqrt(x**2 + y**2)
    kosinusUgla = y/put
    ubrzanje = g*kosinusUgla
    v = np.sqrt(2*g*y1)

    if abs(ubrzanje) > 1e-8:
        vreme = resiKvadratnuJednacinu(0.5*ubrzanje, v, -put)
    else:
        vreme = put/v
    return vreme

def vremeZaKrivu(xs, ys, g):
    vremena = [0]

    for i in range(0, brojTacaka-1):
        vremena.append(vremena[-1] + vremeZaDuz(xs[i], ys[i], xs[i+1], ys[i+1], g))

    return vremena

def vrednostiDuz(x, y, g):
    k = y/x
    xs = np.linspace(0, x, brojTacaka)
    ys = (k) * xs #koeficijent
    #print(vremeZaDuz(0, 0, x, y, g))
    vreme = vremeZaKrivu(xs, ys, g)

    return xs, ys, vreme

#krug cija je tangenta u (0,0) y osa
def vrednostiKrug(x, y, g):
    r = (x**2+y**2) / (2*x)

    kosinusUgla = ((-r)*(x-r))/(r**2)
    ugao = np.arccos(kosinusUgla)

    uglovi = np.linspace(0, ugao, brojTacaka)
    xs = r-r*np.cos(uglovi)
    ys = r*np.sin(uglovi)
    vreme = vremeZaKrivu(xs, ys, g)

    return xs, ys, vreme

def vrednostiCikloida(x, y, g):

    parametarKraj = fsolve(lambda t: y/x - (1-np.cos(t))/(t-np.sin(t)), np.pi*(2*x/(x+y)))[0]

    R = y/(1 - np.cos(parametarKraj))

    params = np.linspace(0, parametarKraj, brojTacaka)
    xs = R*(params - np.sin(params))
    ys = R*(1 - np.cos(params))

    vreme = vremeZaKrivu(xs, ys, g)
    return xs, ys, vreme


def nacrtajSve(x, y, g):
    kanvas = FigureCanvas(Figure(figsize=(5, 3)))
    ax = kanvas.figure.subplots()

    xsDuz, ysDuz, tDuz = vrednostiDuz(x, y, g)
    ax.plot(xsDuz, ysDuz, label = 'Prava: {:.5f} s'.format(tDuz[-1]), color='blue')

    xsKrug, ysKrug, tKrug = vrednostiKrug(x, y, g)
    ax.plot(xsKrug, ysKrug, label = 'Krug: {:.5f} s'.format(tKrug[-1]), color='red')

    xsCikloida, ysCikloida, tCikloida = vrednostiCikloida(x, y, g)
    ax.plot(xsCikloida, ysCikloida, label = 'Cikloida: {:.5f} s'.format(tCikloida[-1]), color='green')

    ax.set_aspect('equal')
    ax.legend()
    ax.invert_yaxis()

    return kanvas
