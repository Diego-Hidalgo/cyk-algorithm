from src.model.Grammar import Grammar
import itertools as it

class CYK:
    
    def __init__(self, grammar):
        self.__matrix = []
        self.__grammar = grammar

    def __initialize_matrix(self, string):
        for i in string:
            self.__matrix.append([])
    
    def grammar_produces_string(self, string:str):
        n = len(string)
        self.__initialize_matrix(string)
        self.__initial_step(string)
        self.__iterate_matrix(n)
        return self.__grammar.initial_state in self.__matrix[0][n-1]
    
    @property
    def matrix(self):
        return self.__matrix

    def __initial_step(self, string):
        n = len(string)
        for i in range(0, n):
            self.__matrix[i] += [self.__contains_production(string[i])]

    def __contains_production(self, production):
        return [k for k, v in self.__grammar.productions.items() if production in v]
    
    def __check_production(self, B, C, i, j):
        As = list(it.product(B, C))
        for a in As:
            try:
                self.__matrix[i][j] += self.__contains_production(str(a[0] + a[1]))
            except IndexError:
                self.__matrix[i].append(self.__contains_production(str(a[0] + a[1])))
            
    def __iterate_matrix(self, n):
        for j in range(1, n):
            for i in range(0, n-j):
                for k in range(0, j):
                    B = self.__matrix[i][k]
                    C = self.__matrix[i+k+1][j-k-1]
                    self.__check_production(B, C, i, j)
