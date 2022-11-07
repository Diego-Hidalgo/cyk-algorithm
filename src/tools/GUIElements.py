from PyQt5 import QtCore, QtGui, QtWidgets


def createLabel(parent: QtWidgets, name: str, text: str):
    label = QtWidgets.QLabel(parent)
    label.setObjectName(name)
    label.setText(text)
    return label


def createFont(size: int, bold: bool, weight: int, *args):
    font = QtGui.QFont()
    font.setPointSize(size)
    font.setBold(bold)
    font.setWeight(weight)
    return font


def createTextField(parent: QtWidgets, name: str):
    text = QtWidgets.QPlainTextEdit(parent)
    text.setObjectName(name)
    return text


def createButton(parent: QtWidgets, name: str):
    button = QtWidgets.QPushButton(parent)
    button.setObjectName(name)
    return button


def createFrame(parent, name: str, width: int, height: int, *args):
    frame = QtWidgets.QWidget(parent)
    frame.setObjectName(name)
    frame.resize(width, height)
    if len(args) > 0:
        frame.setMaximumSize(args[0][0], args[0][1])
        frame.setMinimumSize(args[1][0], args[1][1])
    else:
        frame.setMaximumSize(width, height)
        frame.setMinimumSize(width, height)
    return frame


def adjustMainWindow(frame, name: str, width: int, height: int, *args):
    frame.setObjectName(name)
    frame.resize(width, height)
    if len(args) > 0:
        frame.setMaximumSize(args[0][0], args[0][1])
        frame.setMinimumSize(args[1][0], args[1][1])
    else:
        frame.setMaximumSize(width, height)
        frame.setMinimumSize(width, height)


def createSizePolicy(own, horizontalPolicy, verticalPolicy, hStretch, vStretch):
    sizePolicy = QtWidgets.QSizePolicy(horizontalPolicy, verticalPolicy)
    sizePolicy.setHorizontalStretch(hStretch)  # 10 / 5
    sizePolicy.setVerticalStretch(vStretch)
    sizePolicy.setHeightForWidth(own.sizePolicy().hasHeightForWidth())
    return sizePolicy
