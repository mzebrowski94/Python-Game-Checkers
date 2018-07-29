# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.DrawableObject import DrawableObject


class MenuGameOver(DrawableObject):
    '''Klasa obiektu rysowalnego przedstawiająca końcowy ekran gry.'''

    def __init__(self):
        super().__init__("view/img/Gameover.png")
        self.posX = 0
        self.posY = 100

    def updateView(self, display, x, y):
        self.draw(display, x, y)

    def updateImage(self):
        pass
