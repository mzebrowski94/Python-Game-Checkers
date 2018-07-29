# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.impl.Checker import Checker
from model.enums.PlayerColor import PlayerColor


class Checkers:
    '''Klasa posiadająca odwołanie do wszystkich pionów na planszy.'''
    def __init__(self):
        self.whiteCheckers = []
        self.blackCheckers = []

    def initCheckers(self, fields):
        '''Metoda służąca od inicjalizacji pionów i przypisania ich
        początkowych lokalizacji do odpowiednich pól planszy.'''
        self.whiteCheckers[:] = []
        self.blackCheckers[:] = []

        fieldListLen = len(fields)
        for i in range(0, 12):
            x = fields[i].x
            y = fields[i].y
            checker = Checker(PlayerColor.WHITE, x, y)
            self.whiteCheckers.append(checker)
            fields[i].checker = checker

        for i in range(fieldListLen - 12, fieldListLen):
            x = fields[i].x
            y = fields[i].y
            checker = Checker(PlayerColor.BLACK, x, y)
            self.blackCheckers.append(checker)
            fields[i].checker = checker

    def assignCheckersToFieldList(self, checkers, boardPane):
        '''Metoda służąca od przypisania
                początkowych lokalizacji wczytanych pionów do odpowiednich pól planszy.'''
        self.whiteCheckers[:] = []
        self.blackCheckers[:] = []

        for checker in checkers:
            if checker.playerColor == PlayerColor.WHITE:
                self.whiteCheckers.append(checker)
            else:
                self.blackCheckers.append(checker)
            field = boardPane.getSelectedField(checker.posX, checker.posY)
            field.assignChecker(checker)

    def updateCheckers(self, display):
        '''Metoda wyowłująca aktualizację stanu graficznego pionów.'''
        for checker in self.whiteCheckers:
            checker.updateView(display, 0, 0)

        for checker in self.blackCheckers:
            checker.updateView(display, 0, 0)

    def removeWhiteChecker(self, checker):
        '''Metoda wywołująca usunięcie piona z listy.'''
        self.whiteCheckers.remove(checker)

    def removeBlackChecker(self, checker):
        '''Metoda wywołująca usunięcie piona z listy.'''
        self.blackCheckers.remove(checker)
