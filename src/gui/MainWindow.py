import time

from PyQt5 import QtCore, QtGui, QtWidgets
from src.tools.GUIElements import *
from src.gui.AddGrammarView import *
from src.gui.ResultView import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 510
BOTTOM_FRAME_HEIGHT = 100


def configFrame(frame, x, y):
    frame.setGeometry(QtCore.QRect(x, y, frame.width(), frame.height()))
    frame.setSizePolicy(createSizePolicy(frame, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed, 0, 0))


class MainWindow(object):

    def __init__(self):
        self.centralWidget = None
        self.window = None

    def setupUi(self, window):
        self.window = window
        adjustMainWindow(window, "window", WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralWidget = QtWidgets.QWidget(window)
        self.centralWidget.setObjectName("centralWidget")
        window.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(window)

    def changeView(self, view):
        self.centralWidget = QtWidgets.QWidget(self.window)
        self.centralWidget.setObjectName("centralWidget")
        view.setupView()
        self.window.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.window)
