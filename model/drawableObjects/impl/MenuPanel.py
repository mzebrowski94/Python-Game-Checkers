# Python 3.6.3, Windows, PyCharm
import pygame

from model.enums.PlayerColor import PlayerColor
from model.drawableObjects.DrawableObject import DrawableObject


class MenuPanel(DrawableObject):
    '''Klasa obiektu rysowalnego opisująca górny panel menu na
    którym pokazywana jest informacja, który z graczy ma wykonać ruch'''

    def __init__(self):
        super().__init__("view/img/menu/MenuPanelWhite.png")
        self.whitePlayerPanel = self.image
        self.blackPlayerPanel = pygame.image.load("view/img/menu/MenuPanelBlack.png")

    def updateLogic(self):
        pass

    def updateView(self, display, x, y):
        self.draw(display, x, y)

    def updateImage(self, playerColor):
        if playerColor is PlayerColor.WHITE:
            self.image = self.whitePlayerPanel
        else:
            self.image = self.blackPlayerPanel



