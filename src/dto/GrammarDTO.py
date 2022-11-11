class GrammarDTO:
    def __init__(self, variables: [], terminals: []):
        self.__variables = variables
        self.__terminals = terminals

    @property
    def variables(self):
        return self.__variables

    @property
    def terminals(self):
        return self.__terminals

    @variables.setter
    def variables(self, newVariables: []):
        self.__variables = newVariables

    @terminals.setter
    def terminals(self, newTerminals: []):
        self.__terminals = newTerminals

    def __str__(self):
        return str(self.__variables) + '\n' + str(self.__terminals)
