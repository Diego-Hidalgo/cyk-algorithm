
class Grammar:

    def __init__(self, *args):
        if len(args) != 2:
            raise RuntimeError("Invalid amount of arguments")
        self.__states = args[0]
        self.__alphabet = args[1]
        self.__productions = {}
        self.__initialize_variables()

    def __initialize_variables(self):
        for v in self.__states:
            self.__productions[v] = []

    @property
    def states(self):
        return self.__states

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def productions(self):
        return self.__productions

    @states.setter
    def states(self, new_states:list):
        self.__states = new_states

    @alphabet.setter
    def alphabet(self, new_alphabet:list):
        self.__alphabet = new_alphabet

    @productions.setter
    def productions(self, new_productions:dict):
        self.__productions = new_productions

    def add_production_to_variable(self, variable:str, production:str):
        if production.islower() and production not in self.__alphabet:
            raise RuntimeError("The specified variable does not exist in this grammar")
        if len(production) == 1 and not production.islower():
            raise RuntimeError("Production must be a terminal or a binary production")
        if len(production) == 2 and not production.isupper():
            raise RuntimeError("Production must be a terminal or a binary production")
        if variable in self.__productions:
            if production not in self.__productions[variable]:
                self.__productions[variable] += [production]

