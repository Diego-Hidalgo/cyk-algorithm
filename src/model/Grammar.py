
class Grammar:
    """
    This class is used to represent a context independent grammar.
    The grammar is in Chomsky's normal form.
    """
    
    """
    The constructor takes two arguments.
    The first argument is a list. This list contains the states or variables available in the grammar. The first state found in this list will be taken as the initial state.
    The second argument is a list. This list contains the alphabet or terminal productions of the grammar.
    The productions are stored in the __productions variable. It's a dictionary where the key is a state of the grammar and the value is a list with the productions.
    """
    def __init__(self, *args):
        if len(args) != 2:
            raise RuntimeError("Invalid amount of arguments")
        self.__states = args[0]
        self.__alphabet = args[1]
        self.__productions = {}
        self.__initialize_variables()
    
    """
    This method is called in the constructor of the class. It's responsibility is to initialize the list that contains the productions for each state in the grammar.
    """
    def __initialize_variables(self):
        for v in self.__states:
            self.__productions[v] = []
    
    """
    This method defines the property getter for the __states variable.
    :return: the states defined in the grammar.
    """
    @property
    def states(self):
        return self.__states

    """
    This method defines the property getter for the __alphabet variable.
    :return: the alphabet defined in the grammar.
    """
    @property
    def alphabet(self):
        return self.__alphabet

    """
    This method defines the property getter for the __productions variable.
    :return: the productions defined in the grammar.
    """
    @property
    def productions(self):
        return self.__productions

    """
    A setter for the __states variable. Changes the value of the states defined to a new one.
    :param new_states: the new states for the grammar
    """
    @states.setter
    def states(self, new_states:list):
        self.__states = new_states

    """
    A setter for the __alphabet variable. Changes the value of the alphabet defined to a new one.
    :param new_alphabet: the new alphabet of the grammar
    """
    @alphabet.setter
    def alphabet(self, new_alphabet:list):
        self.__alphabet = new_alphabet

    """
    A setter for the __productions variable. Changes the value of the productions defined to a new one.
    :param new_productions: the new productions of the grammar
    """
    @productions.setter
    def productions(self, new_productions:dict):
        self.__productions = new_productions
    
    """
    Add a new production to a specified variable in the grammar.
    :param variable: must be an existent variable or state in the grammar. Specifies the variable that will contain the production.
    :param production: the production to add to the variable. Given that this class represents a grammar in Chomsky's normal form. the production must be a terminal or a binary production (A -> BC).
    """
    def add_production_to_variable(self, variable:str, production:str):
        if variable not in self.__productions:
            raise RuntimeError("La variable no existe en las variables definidas de la gramatica")
        if len(production) == 1 and production not in self.__alphabet:
            raise RuntimeError("La terminal especificada no existe en el alfabeto definido de la gramatica")
        if production not in self.__productions[variable]:
            self.__productions[variable] += [production]

