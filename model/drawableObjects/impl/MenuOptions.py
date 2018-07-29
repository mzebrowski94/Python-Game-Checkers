# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.DrawableObject import DrawableObject


class MenuOptions(DrawableObject):
    '''Klasa obiektu rysowalnego przedstawiająca menu opcji gry.
    Dostępne opcje to: NEW, SAVE, LOAD, QUIT'''

    def __init__(self):
        super().__init__("view/img/menu/MenuOptions.png")
        self.optionPanes = []
        self.posX = 425
        self.posY = 0

    def updateView(self, display, x, y):
        self.draw(display, x, y)
        for optionPane in self.optionPanes:
            optionPane.option.updateView(display, x, y)

    def updateImage(self):
        pass
