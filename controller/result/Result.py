# Python 3.6.3, Windows, PyCharm

class Result:
    '''Klasa wykorzystywana do przenoszenia rezultatów zdarzeń między komponentami.'''


    def __init__(self, resultType):
        '''Metoda inicjalizująca klasy Result, jako argument przyjmuje tym rezultatu'''
        self.targetField = None
        self.selectedChecker = None
        self.type = resultType
        self.option = None
