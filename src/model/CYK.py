from src.model.Grammar import Grammar
import itertools as it

class CYK:
    """
    This is the class used to process a given string with a specified grammar.
    The process consists of determining whether a given string can be produced by a independent context grammar.
    In order to do that, we implement the CYK algorithm.
    """

    def __init__(self, grammar):
        """
        This is the constructor of the CYK class. Takes only one parameter
        :param grammar: the grammar that will contain the valid alphabet, variables and productions.
        As stated before, we use a matrix that is initially defined as a list
        """
        self.__matrix = []
        self.__grammar = grammar

    def __initialize_matrix(self, string):
        """
        This method initializes the matrix that will be used to store states.
        Appens n empty lists to the initial list, where n is the length of the string to process.
        :param string: the given string to process.
        """
        for i in string:
            self.__matrix.append([])
    
    def grammar_produces_string(self, string:str):
        """
        Calls al the method involved in the process of determining whether the string can be prodced by the given grammar.
        :param string: the string to check
        :return: a boolean indicating the result. True if the string can be produced by the grammar, False if not.
        """
        for s in string:
            if s not in self.__grammar.alphabet:
                return False
        n = len(string)
        self.__initialize_matrix(string)
        self.__initial_step(string)
        self.__iterate_matrix(n)
        return self.__grammar.initial_state in self.__matrix[0][n-1]
    
    @property
    def matrix(self):
        """
        the property getter for the __matrix attribute.
        :return: the matrix attribute
        """
        return self.__matrix

    def __initial_step(self, string):
        """
        Does the initial step defined in the CYK algorithm. Adds to each row the states that can produce each symbol in the string.
        :param string: the string to process
        """
        n = len(string)
        for i in range(0, n):
            self.__matrix[i] += [self.__contains_production(string[i])]

    def __contains_production(self, production):
        """
        Determines the states that can produce a given production.
        :param production: the production to check.
        :return: the states that produce the given production. It's an empty list if the grammar does not contain the given production
        """
        return [k for k, v in self.__grammar.productions.items() if production in v]
    
    def __check_production(self, B, C, i, j):
        """
        
        """
        As = list(it.product(B, C))
        for a in As:
            try:
                self.__matrix[i][j] += self.__contains_production(str(a[0] + a[1]))
            except IndexError:
                self.__matrix[i].append(self.__contains_production(str(a[0] + a[1])))
            
    def __iterate_matrix(self, n):
        """
        The second step of the CYK algorithm.
        Iterates over the matrix to determine the states for each row and column of the matrix.
        """
        for j in range(1, n):
            for i in range(0, n-j):
                for k in range(0, j):
                    B = self.__matrix[i][k]
                    C = self.__matrix[i+k+1][j-k-1]
                    self.__check_production(B, C, i, j)
