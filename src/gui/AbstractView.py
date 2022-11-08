import abc
from PyQt5 import QtWidgets


class AbstractView:
    def __init__(self,  parent: QtWidgets.QMainWindow):
        self.__parent = parent

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, newParent):
        self.__parent = newParent

    @abc.abstractmethod
    def setupView(self):
        pass

    @abc.abstractmethod
    def changeView(self, view):
        pass
