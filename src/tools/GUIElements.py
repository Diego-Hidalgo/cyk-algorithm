from PyQt5 import QtCore, QtGui, QtWidgets


def createLabel(text: str, width: int, height: int, *args):
    label = QtWidgets.QLabel()
    # label.setObjectName(name)
    label.setText(text)
    label.resize(width, height)
    if len(args) > 0:
        label.setMaximumSize(args[0][0], args[0][1])
        label.setMinimumSize(args[1][0], args[1][1])
    else:
        label.setMaximumSize(width, height)
        label.setMinimumSize(width, height)
    return label


def createFont(size: int, bold: bool, weight: int, *args):
    font = QtGui.QFont()
    font.setPointSize(size)
    font.setBold(bold)
    font.setWeight(weight)
    return font


def createTextField(name: str, width: int, height: int, *args):
    text = QtWidgets.QPlainTextEdit()
    text.setObjectName(name)
    text.resize(width, height)
    if len(args) > 0:
        text.setMaximumSize(args[0][0], args[0][1])
        text.setMinimumSize(args[1][0], args[1][1])
    else:
        text.setMaximumSize(width, height)
        text.setMinimumSize(width, height)
    return text


def createButton(name: str,  width: int, height: int, *args):
    button = QtWidgets.QPushButton()
    button.setObjectName(name)
    button.resize(width, height)
    if len(args) > 0:
        button.setMaximumSize(args[0][0], args[0][1])
        button.setMinimumSize(args[1][0], args[1][1])
    else:
        button.setMaximumSize(width, height)
        button.setMinimumSize(width, height)
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


def createScrollArea(parent, name: str, width: int, height: int, *args):
    area = QtWidgets.QScrollArea(parent)
    area.setObjectName(name)
    area.resize(width, height)
    if len(args) > 0:
        area.setMaximumSize(args[0][0], args[0][1])
        area.setMinimumSize(args[1][0], args[1][1])
    else:
        area.setMaximumSize(width, height)
        area.setMinimumSize(width, height)
    return area


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
