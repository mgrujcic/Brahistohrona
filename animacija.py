from matplotlib.animation import FuncAnimation, TimedAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
import numpy as np
from matplotlib.lines import Line2D

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

fig, ax = 0, 0
xs, ys = [], []
ln, = 0,
#https://stackoverflow.com/questions/36665850/matplotlib-animation-inside-your-own-gui
#functional animation??
class CustomFigCanvas(FigureCanvas, TimedAnimation):

        def __init__(self):

            # The data
            self.n = np.linspace(0, 1000, 1001)
            self.y = 1.5 + np.sin(self.n/20)

            # The window
            self.fig = Figure(figsize=(5,5), dpi=100)
            ax1 = self.fig.subplots()

            # ax1 settings
            ax1.set_xlabel('time')
            ax1.set_ylabel('raw data')
            self.line1 = Line2D([], [], color='blue')
            ax1.add_line(self.line1)
            ax1.set_xlim([0, 5])
            ax1.set_ylim([0, 5])

            FigureCanvas.__init__(self, self.fig)
            TimedAnimation.__init__(self, self.fig, interval = 20, blit = True)


        def _draw_frame(self, framedata):
            i = framedata

            self.line1.set_data(self.n[ 0 : i ], self.y[ 0 : i ])
            self._drawn_artists = [self.line1]

        def new_frame_seq(self):
            return iter(range(self.n.size))

        def _init_draw(self):
            lines = [self.line1]
            for l in lines:
                l.set_data([], [])

        def zaustavi(self):
            self._stop()





def animiraj(x, y, g):
    kanvas = CustomFigCanvas()
    ax = kanvas.figure.subplots()
    #xs, ys =[], []
    #ln, = ax.plot([], [], 'ro')

    
    #ani = FuncAnimation(fig, azurirajAnimaciju, frames=np.linspace(0, 2*np.pi, 128),
    #                init_func=inicijalizujAnimaciju, blit=True)
    
    return kanvas