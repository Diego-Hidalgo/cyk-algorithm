from src.gui.MainWindow import *
from src.gui.AddGrammarView import *
from src.gui.ResultView import *


class GrammarController(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.addGrammarView = AddGrammarView(self)
        self.resultView = ResultView(self)
        self.setupUi(self)
        self.changeView(self.addGrammarView)

    def runCYKAlgorithmOnGrammar(self):
        print(self.addGrammarView.message)

