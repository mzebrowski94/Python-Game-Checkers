# Python 3.6.3, Windows, PyCharm
from pygame.rect import Rect


class GamePane(Rect):
    '''Klasa panelu, dziedzcząca po klasie Rect,
    służy do oznaczania obszarów wyboru elementów na ekranie gry.'''
    def __init__(self, x, y, width, hight):
        super().__init__(x, y, width, hight)

    def checkIfSelected(self, x, y):
        '''Metoda sprawdzająca czy zadany punkt (miejsce naciśnięćia myszą),
        znajduje się na wyranym panelu.'''
        return self.collidepoint(x, y)
