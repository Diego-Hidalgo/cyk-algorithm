from PyQt5 import QtCore, QtGui, QtWidgets
from src.tools.GUIElements import *
from src.gui.AbstractView import AbstractView

BOTTOM_FRAME_HEIGHT = 100
SPACE_BETWEEN_ELEMENTS = 10


def configFrame(frame, x, y):
    frame.setGeometry(QtCore.QRect(x, y, frame.width(), frame.height()))
    frame.setSizePolicy(createSizePolicy(frame, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed, 0, 0))


def createContainer(layout):
    container = QtWidgets.QWidget()
    container.resize(layout.width(), layout.height())
    return container


class AddGrammarView(AbstractView):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__(parent)
        self.leftFrame = None
        self.leftLayout: QtWidgets.QVBoxLayout
        self.rightFrame = None
        self.rightLayout: QtWidgets.QVBoxLayout()
        self.bottomFrame = None
        self.bottomLayout: QtWidgets.QHBoxLayout()
        self.__lastFieldAdded = []
        self.__quantityOfFields = 0
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
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setGeometry(QtCore.QRect(self.leftFrame.x(), self.leftFrame.y(), self.leftFrame.width(),
                                                 self.leftFrame.height()))
        self.leftLayout.setObjectName("leftContainer")
        self.__buildLeftFrameElements()

    def __buildRightFrame(self):
        self.rightFrame = createFrame(self.parent.centralWidget, "rightFrame", int(self.parent.width() / 2),
                                      self.parent.height() - BOTTOM_FRAME_HEIGHT)
        configFrame(self.rightFrame, self.leftFrame.width() + 1, 0)
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setGeometry(QtCore.QRect(self.rightFrame.x(), self.rightFrame.y(), self.rightFrame.width(),
                                                  self.rightFrame.height()))
        self.rightLayout.setObjectName("rightContainer")
        self.__buildRightFrameElements()

    def __buildBottomFrame(self):
        self.bottomFrame = createFrame(self.parent.centralWidget, "bottomFrame", self.parent.width(),
                                       BOTTOM_FRAME_HEIGHT)
        configFrame(self.bottomFrame, 0, self.leftFrame.height() + 1)
        self.bottomLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout.setGeometry(QtCore.QRect(self.bottomFrame.x(), self.bottomFrame.y(), self.bottomFrame.width(),
                                                   self.bottomFrame.height()))
        self.bottomLayout.setObjectName("bottomContainer")
        self.__buildBottomFrameElements()

    def __buildLeftFrameElements(self):
        widget = QtWidgets.QWidget()
        label = createLabel(("label" + str(self.__quantityOfFields)), "Ingresa una GIC", self.leftFrame.width(), 70)
        label.setGeometry(QtCore.QRect(0, 0, 100, 45))
        label.setFont(createFont(18, True, label.width()))
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.leftLayout.addWidget(label)
        widget.setLayout(self.leftLayout)
        self.leftFrame.setWidget(widget)

    def createVariableField(self):
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("Hbox" + str(self.__quantityOfFields))
        widget = QtWidgets.QWidget()
        widget.setObjectName("widget" + str(self.__quantityOfFields))
        variables = createTextField(("Variables" + str(self.__quantityOfFields)), 40, 25)
        terminals = createTextField(("Terminals" + str(self.__quantityOfFields)), self.leftFrame.width() - 150, 25)
        layout.addWidget(variables)
        layout.addWidget(terminals)
        widget.setLayout(layout)
        self.leftLayout.addWidget(widget)
        container.setLayout(self.leftLayout)
        self.leftFrame.setWidget(container)
        self.__quantityOfFields += 1

    def deleteVariableField(self):
        widgets = self.leftLayout.count()
        if widgets > 1:
            self.leftLayout.itemAt(widgets - 1).widget().deleteLater()

    def __buildRightFrameElements(self):
        label = createLabel("rightTittle", "Ingresa una producción", self.rightFrame.width(), 70)
        label.setGeometry(QtCore.QRect(self.rightFrame.x(), 0, self.rightFrame.width(), 70))
        label.setFont(createFont(18, True, label.width()))
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.rightLayout.addWidget(label)
        self.rightFrame.setLayout(self.rightLayout)

    def __buildBottomFrameElements(self):
        addBtn = createButton("addProduction", 145, 30)
        addBtn.setFont(createFont(10, True))
        addBtn.setText("Agregar producción")
        addBtn.clicked.connect(self.createVariableField)
        deleteBtn = createButton("deleteProduction", 145, 30)
        deleteBtn.setFont(createFont(10, True))
        deleteBtn.setText("Borrar campo")
        deleteBtn.clicked.connect(self.deleteVariableField)
        self.bottomLayout.addWidget(addBtn)
        self.bottomLayout.addWidget(deleteBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
