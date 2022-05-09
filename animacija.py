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
#https://stackoverflow.com/questions/36665850/matplotlib-animation-inside-your-own-gui
#functional animation??
class CustomFigCanvas(FigureCanvas, TimedAnimation):

        def __init__(self, x, y, g):
            self.g = g
            self.x = x
            self.y = y

            self.fig = Figure(figsize=(5,5))
            ax1 = self.fig.subplots()

            # The data
            self.xsDuz, self.ysDuz, self.tDuz = akcije.vrednostiDuz(x, y, g)
            ax1.plot(self.xsDuz, self.ysDuz, label = 'Prava: {:.5f} s'.format(self.tDuz))

            self.xsKrug, self.ysKrug, self.tKrug = akcije.vrednostiKrug(x, y, g)
            ax1.plot(self.xsKrug, self.ysKrug, label = 'Krug: {:.5f} s'.format(self.tKrug))

            self.xsCikloida, self.ysCikloida, self.tCikloida = akcije.vrednostiCikloida(x, y, g)
            ax1.plot(self.xsCikloida, self.ysCikloida, label = 'Cikloida: {:.5f} s'.format(self.tCikloida))


            self.n = np.linspace(0, 1000, 1001)

            ax1.set_xlabel('time')
            ax1.set_ylabel('raw data')
            self.tackaDuz = Circle((0,0), 0, color='blue')
            self.tackaKrug = Circle((0,0), 0, color='red')
            self.tackaCikloida = Circle((0,0), 0, color='green')
            ax1.add_artist(self.tackaDuz)
            ax1.add_artist(self.tackaKrug)
            ax1.add_artist(self.tackaCikloida)
            #ax1.set_xlim([0, 1000])
            #ax1.set_ylim([0, 4])
            ax1.invert_yaxis()
            ax1.set_aspect('equal')

            FigureCanvas.__init__(self, self.fig)
            TimedAnimation.__init__(self, self.fig, interval = 20, blit = True)


        def _draw_frame(self, framedata):
            i = framedata

            self.tackaDuz.set(center=(self.xsDuz[i], self.ysDuz[i]))
            self.tackaKrug.set(center=(self.xsKrug[i], self.ysKrug[i]))
            self.tackaCikloida.set(center=(self.xsCikloida[i], self.ysCikloida[i]))

            self._drawn_artists = [self.tackaDuz, self.tackaKrug, self.tackaCikloida]

        def new_frame_seq(self):
            return iter(range(akcije.brojTacaka))

        def _init_draw(self):
            self.tackaDuz.set(radius=0.5)
            self.tackaKrug.set(radius=0.5)
            self.tackaCikloida.set(radius=0.5)

            #lines = [self.line1]
            #for l in lines:
            #    l.set_data([], [])
            pass

        def zaustavi(self):
            self._stop()





def animiraj(x, y, g):
    kanvas = CustomFigCanvas(x, y, g)

    return kanvas
