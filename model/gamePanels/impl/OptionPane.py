# Python 3.6.3, Windows, PyCharm
from model.drawableObjects.impl.OptionLighting import OptionLighting
from model.gamePanels.GamePane import GamePane


class OptionPane(GamePane):
    '''Klasa zawierająca informację o położeniu i obszarze
    pojedynczego panelu menu opcji.'''
    def __init__(self, posX, posY, sizeX, sizeY, menuOption):
        super().__init__(posX, posY, sizeX, sizeY)
        self.option = OptionLighting(menuOption, 425, 0)
