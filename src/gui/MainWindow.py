import time

from PyQt5 import QtCore, QtGui, QtWidgets
from src.tools.GUIElements import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 510
BOTTOM_FRAME_HEIGHT = 100


def configFrame(frame, x, y):
    frame.setGeometry(QtCore.QRect(x, y, frame.width(), frame.height()))
    frame.setSizePolicy(createSizePolicy(frame, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed, 0, 0))


class MainWindow(object):

    def __init__(self):
        self.centralWidget = None
        self.leftFrame = None
        self.rightFrame = None
        self.bottomFrame = None
        self.MainWindow = None
        self.button = None

    def setupUi(self, window):
        self.MainWindow = window
        adjustMainWindow(window, "window", WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralWidget = QtWidgets.QWidget(window)
        self.centralWidget.setObjectName("centralWidget")
        self.leftFrame = createFrame(self.centralWidget, "leftFrame", int(WINDOW_WIDTH / 2),
                                     WINDOW_HEIGHT - BOTTOM_FRAME_HEIGHT)
        configFrame(self.leftFrame, 0, 0)
        self.leftFrame.setStyleSheet("background-color: yellow;")
        self.rightFrame = createFrame(self.centralWidget, "rightFrame", int(WINDOW_WIDTH / 2),
                                      WINDOW_HEIGHT - BOTTOM_FRAME_HEIGHT)
        configFrame(self.rightFrame, self.leftFrame.width() + 1, 0)
        self.rightFrame.setStyleSheet("background-color: blue;")
        self.bottomFrame = createFrame(self.centralWidget, "bottomFrame", WINDOW_WIDTH, BOTTOM_FRAME_HEIGHT)
        configFrame(self.bottomFrame, 0, self.leftFrame.height() + 1)
        self.bottomFrame.setStyleSheet("background-color: red;")
        self.button = createButton(self.centralWidget, "boton")
        self.button.setGeometry(QtCore.QRect(self.leftFrame.width() + 1, 0, 70, 20))
        self.button.setFont(createFont(11, False, 75))
        self.button.setText("Pulsar")
        QtCore.QMetaObject.connectSlotsByName(self.centralWidget)
        window.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(window)
        self.button.clicked.connect(self.even)

    def even(self):
        self.centralWidget = QtWidgets.QWidget(self.MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
