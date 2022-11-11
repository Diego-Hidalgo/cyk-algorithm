from src.gui.MainWindow import *
from src.gui.AddGrammarView import *
from src.gui.ResultView import *
from src.model.Grammar import *
from src.model.CYK import *
from src.error.error import *


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
        if response:
            self.addGrammarView.showResponse("Si pertenece a la gramatica")
        else:
            self.addGrammarView.showResponse("No pertenece a la gramatica")

    def __setGrammar(self):
        grammar = Grammar(self.addGrammarView.variables, self.addGrammarView.terminals)
        states = grammar.states
        productions = self.addGrammarView.productions
        for variable in range(len(grammar.states)):
            p = productions[variable].split("|")
            for production in p:
                try:
                    grammar.add_production(states[variable], production)
                except CustomRuntimeError as e:
                    self.addGrammarView.showResponse(e)
        return grammar
