from matplotlib.animation import FuncAnimation, TimedAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import numpy as np
from matplotlib.patches import Circle


from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import akcije

fig, ax = 0, 0
xs, ys = [], []
ln, = 0,

class CustomFigCanvas(FigureCanvas, TimedAnimation):

        def __init__(self, x, y, g):
            self.g = g
            self.x = x
            self.y = y

            self.fig = Figure(figsize=(5,5))
            ax1 = self.fig.subplots()

            self.circleRadius = (x+y)*0.01

            self.tackaDuz = Circle((0,0), self.circleRadius, color='blue')
            self.tackaKrug = Circle((0,0), self.circleRadius, color='red')
            self.tackaCikloida = Circle((0,0), self.circleRadius, color='green')

            ax1.add_patch(self.tackaDuz)
            ax1.add_patch(self.tackaKrug)
            ax1.add_patch(self.tackaCikloida)

            self.xsDuz, self.ysDuz, self.tDuz = akcije.vrednostiDuz(x, y, g)
            ax1.plot(self.xsDuz, self.ysDuz, label = 'Prava: {:.5f} s'.format(self.tDuz[-1]), color='blue')

            self.xsKrug, self.ysKrug, self.tKrug = akcije.vrednostiKrug(x, y, g)
            ax1.plot(self.xsKrug, self.ysKrug, label = 'Krug: {:.5f} s'.format(self.tKrug[-1]), color='red')

            self.xsCikloida, self.ysCikloida, self.tCikloida = akcije.vrednostiCikloida(x, y, g)
            ax1.plot(self.xsCikloida, self.ysCikloida, label = 'Cikloida: {:.5f} s'.format(self.tCikloida[-1]), color='green')

            ax1.invert_yaxis()
            ax1.set_aspect('equal')

            self.tInterval = 20
            self.idxDuz = 0
            self.idxKrug = 0
            self.idxCikloida = 0
            self.tAnimacije = int((self.tDuz[-1]+1)*1000/self.tInterval)

            FigureCanvas.__init__(self, self.fig)
            TimedAnimation.__init__(self, self.fig, interval = self.tInterval, blit = False)


        def _draw_frame(self, framedata):
            i = framedata

            if i == 0:
                self.idxDuz = 0
                self.idxKrug = 0
                self.idxCikloida = 0

            t = i*self.tInterval/1000

            while self.idxDuz+1 < akcije.brojTacaka and self.tDuz[self.idxDuz+1] <= t:
                self.idxDuz = self.idxDuz + 1

            while self.idxKrug+1 < akcije.brojTacaka and self.tKrug[self.idxKrug+1] <= t:
                self.idxKrug = self.idxKrug + 1

            while self.idxCikloida+1 < akcije.brojTacaka and self.tCikloida[self.idxCikloida+1] <= t:
                self.idxCikloida = self.idxCikloida + 1

            self.tackaDuz.set(center=(self.xsDuz[self.idxDuz], self.ysDuz[self.idxDuz]))
            self.tackaKrug.set(center=(self.xsKrug[self.idxKrug], self.ysKrug[self.idxKrug]))
            self.tackaCikloida.set(center=(self.xsCikloida[self.idxCikloida], self.ysCikloida[self.idxCikloida]))

            self._drawn_artists = [self.tackaDuz, self.tackaKrug, self.tackaCikloida]

        def new_frame_seq(self):
            return iter(range(self.tAnimacije))

        def _init_draw(self):
            pass

        def zaustavi(self):
            self._stop()





def animiraj(x, y, g):
    kanvas = CustomFigCanvas(x, y, g)

    return kanvas
