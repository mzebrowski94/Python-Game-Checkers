# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.DrawableObject import DrawableObject


class Board(DrawableObject):
    '''Klasa obiektu rysowalnego przedstawiająca planszę gry.'''

    def __init__(self):
        super().__init__("view/img/Background.png")
        self.posX = 0
        self.posY = 100

    def updateView(self,display, x, y):
        self.draw(display, x, y)

    def updateImage(self):
        pass
