# Python 3.6.3, Windows, PyCharm
from model.gamePanels.GamePane import GamePane


class FieldPane(GamePane):
    ''' Klasa opisująca pojedyncze pole planszy, konstruktor przyjmuje współrzędne powstałego pola.'''
    def __init__(self, x, y):
        super().__init__(x, y, 68, 68)
        self.checker = None

    def unAssignChecker(self):
        '''Metoda służąca do odpięcia piona od danego pola.'''
        self.checker = None

    def assignChecker(self, checker):
        '''Metoda służąca do przypięcia piona do danego pola.'''
        checker.posX = self.x
        checker.posY = self.y
        self.checker = checker


