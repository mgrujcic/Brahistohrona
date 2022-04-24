from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings


def napraviVebView():
    noviWebView = QWebView()
    noviWebView.setUrl(QtCore.QUrl("https://alas.matf.bg.ac.rs/~mi20015/index.html"))
    noviWebView.setObjectName("webView")

