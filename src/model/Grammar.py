
class Grammar:
    """
    This class is used to represent a context independent grammar.
    The grammar is in Chomsky's normal form.
    """
    
    def __init__(self, *args):
        """
        The constructor takes two arguments.
        The first argument is a list. This list contains the states or variables available in the grammar. The first state found in this list will be taken as the initial state.
        The second argument is a list. This list contains the alphabet or terminal productions of the grammar.
        The productions are stored in the __productions variable. It's a dictionary where the key is a state of the grammar and the value is a list with the productions.
        """
        if len(args) != 2:
            raise RuntimeError("Invalid amount of arguments")
        self.__states = args[0]
        self.__alphabet = args[1]
        self.__productions = {}
        self.__initial_state = args[0][0]
        self.__initialize_variables()
    
    def __initialize_variables(self):
        """
        This method initializes the list that contains the productions for each state in the grammar.
        """
        for v in self.__states:
            self.__productions[v] = []
    
    @property
    def states(self):
        """
        This method defines the property getter for the __states variable.
        :return: the states defined in the grammar.
        """
        return self.__states

    @property
    def alphabet(self):
        """
        This method defines the property getter for the __alphabet variable.
        :return: the alphabet defined in the grammar.
        """
        return self.__alphabet

    @property
    def productions(self):
        """
        This method defines the property getter for the __productions variable.
        :return: the productions defined in the grammar.
        """
        return self.__productions

    @property
    def initial_state(self):
        """
        This method defines the property getter for the __initial_state variable.
        :return: the initial state defined in the grammar.
        """
        return self.__initial_state

    @states.setter
    def states(self, new_states:list):
        """
        A setter for the __states variable. Changes the value of the states defined to a new one.
        :param new_states: the new states for the grammar
        """
        self.__states = new_states

    @alphabet.setter
    def alphabet(self, new_alphabet:list):
        """
        A setter for the __alphabet variable. Changes the value of the alphabet defined to a new one.
        :param new_alphabet: the new alphabet of the grammar
        """
        self.__alphabet = new_alphabet

    @productions.setter
    def productions(self, new_productions:dict):
        """
        A setter for the __productions variable. Changes the value of the productions defined to a new one.
        :param new_productions: the new productions of the grammar
        """
        self.__productions = new_productions

    @initial_state.setter
    def initial_state(self, new_initial_state:str):
        """
        A setter for the __initial_state variable. Changes the value of the initial state defined to a new one.
        :param new_initial_state: the new initial state of the grammar
        """
        self.__initial_state = new_initial_state

    def add_production(self, variable:str, production:str):
        """
        Add a new production to a specified variable in the grammar.
        :param variable: must be an existent variable or state in the grammar. Specifies the variable that will contain the production.
        :param production: the production to add to the variable. Given that this class represents a grammar in Chomsky's normal form. the production must be a terminal or a binary production (A -> BC).
        """
        if variable not in self.__productions:
            raise RuntimeError("La variable no existe en las variables definidas de la gramatica")
        if len(production) == 1 and production not in self.__alphabet:
            raise RuntimeError("La terminal especificada no existe en el alfabeto definido de la gramatica")
        if production not in self.__productions[variable]:
            self.__productions[variable] += [production]
