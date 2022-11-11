from src.gui.MainWindow import *
from src.gui.AddGrammarView import *
from src.gui.ResultView import *
from src.model.Grammar import *
from src.model.CYK import *


class GrammarController(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.addGrammarView = AddGrammarView(self)
        self.resultView = ResultView(self)
        self.setupUi(self)
        self.changeView(self.addGrammarView)

    def runCYKAlgorithmOnGrammar(self):
        cyk = CYK(self.__setGrammar())
        response = cyk.grammar_produces_string(self.addGrammarView.string)

    def __setGrammar(self):
        grammar = Grammar(self.addGrammarView.variables, self.addGrammarView.terminals)
        productions = self.addGrammarView.productions
        for variable in grammar.states:
            p = productions[variable].split("|")
            for production in p:
                try:
                    grammar.add_production(variable, production)
                except:
                    print("a")
