from PyQt5 import QtCore, QtGui, QtWidgets
from src.tools.GUIElements import *
from src.gui.AbstractView import AbstractView

BOTTOM_FRAME_HEIGHT = 100


def configFrame(frame, x, y):
    frame.setGeometry(QtCore.QRect(x, y, frame.width(), frame.height()))
    frame.setSizePolicy(createSizePolicy(frame, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed, 0, 0))


class AddGrammarView(AbstractView):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__(parent)
        self.leftFrame = None
        self.leftLayout = None
        self.rightFrame = None
        self.rightLayout = None
        self.bottomFrame = None
        self.bottomLayout = None
        self.variablesFields = []

    def setupView(self):
        self.__buildLeftFrame()
        self.__buildRightFrame()
        self.__buildBottomFrame()

    def changeView(self, view):
        centralWidget = QtWidgets.QWidget(self.parent)
        self.parent.centralWidget().setObjectName("centralWidget")
        self.parent.setCentralWidget(centralWidget)
        QtCore.QMetaObject.connectSlotsByName(self.parent)

    def __buildLeftFrame(self):
        self.leftFrame = createScrollArea(self.parent.centralWidget, "leftFrame", int(self.parent.width() / 2),
                                          self.parent.height() - BOTTOM_FRAME_HEIGHT)
        configFrame(self.leftFrame, 0, 0)
        self.leftFrame.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.leftFrame.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftFrame.setStyleSheet("background-color: yellow;")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setGeometry(QtCore.QRect(self.leftFrame.x(), self.leftFrame.y(), self.leftFrame.width(),
                                                 self.leftFrame.height()))
        self.__buildLeftFrameElements()

    def __buildRightFrame(self):
        self.rightFrame = createFrame(self.parent.centralWidget, "rightFrame", int(self.parent.width() / 2),
                                      self.parent.height() - BOTTOM_FRAME_HEIGHT)
        configFrame(self.rightFrame, self.leftFrame.width() + 1, 0)
        self.rightFrame.setStyleSheet("background-color: blue;")
        self.__buildRightFrameElements()

    def __buildBottomFrame(self):
        self.bottomFrame = createFrame(self.parent.centralWidget, "bottomFrame", self.parent.width(),
                                       BOTTOM_FRAME_HEIGHT)
        configFrame(self.bottomFrame, 0, self.leftFrame.height() + 1)
        self.bottomFrame.setStyleSheet("background-color: red;")
        self.__buildBottomFrameElements()

    def __buildLeftFrameElements(self):
        widget = QtWidgets.QWidget()
        button = createButton("boton", 70, 20)
        button.setGeometry(QtCore.QRect(330, 0, button.width(), button.height()))
        button.setFont(createFont(11, False, 75))
        button.setText("Pulsar")
        button.clicked.connect(self.createVariableField)
        QtCore.QMetaObject.connectSlotsByName(self.leftLayout)
        self.leftLayout.addWidget(button)
        widget.setLayout(self.leftLayout)
        self.leftFrame.setWidget(widget)

    def createVariableField(self):
        widget = QtWidgets.QWidget()
        label = createLabel("Hola", 40, 30)
        label.setFont(createFont(10, False, 30))
        label.setGeometry(QtCore.QRect(60, 50, 30, 20))
        self.leftLayout.addWidget(label)
        widget.setLayout(self.leftLayout)
        self.leftFrame.setWidget(widget)

    def __buildRightFrameElements(self):
        pass

    def __buildBottomFrameElements(self):
        pass

