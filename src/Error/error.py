class CustomRuntimeError(RuntimeError):

    def __init__(self, message=''):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message

class NonExistentSymbol(CustomRuntimeError):
    
    def __init__(self, symbol, message='El simbolo especificado no se encuentra en el alfabeto definido'):
        super().__init__(message)
        self.__symbol = symbol
    
    @property
    def symbol():
        return self.__symbol
    
    def __str__(self):
        return f'{self.__symbol} -> {self.message}'

class NonExistentState(CustomRuntimeError):
    
    def __init__(self, variable, message='La variable especificada no se encuentra definida'):
        super().__init__(message)
        self.__variable = variable
    
    @property
    def variable():
        return self.__variable
    
    def __str__(self):
        return f'{self.__variable} -> {self.message}'

class InvalidProduction(CustomRuntimeError):
    
    def __init__(self, production, message='La produccion no cumple con la forma normal de chomsky'):
        super().__init__(message)
        self.__production = production
    
    @property
    def production():
        return self.__production
    
    def __str__(self):
        return f'{self.__production} -> {self.message}'
