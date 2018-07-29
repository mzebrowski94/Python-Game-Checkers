# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.DrawableObject import DrawableObject


class OptionLighting(DrawableObject):
    '''Klasa obiektu rysowalnego wykorzystywana przy tworzeniu efektu podswietlenia wybranej opcji.'''
    def __init__(self, menuOption, x, y):
        self.menuOption = menuOption
        super().__init__("view/img/menu/MenuOptions" + str(self.menuOption) + ".png")
        self.posX = x
        self.posY = y
        self.isLighting = False

    def updateView(self, display, x, y):
        if self.isLighting:
            self.draw(display, self.posX, self.posY)

    def updateLogic(self):
        pass

    def updateImage(self):
        self.isLighting = not self.isLighting
