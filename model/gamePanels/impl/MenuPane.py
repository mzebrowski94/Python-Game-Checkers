# Python 3.6.3, Windows, PyCharm
from model.gamePanels.GamePane import GamePane


class MenuPane(GamePane):
    '''Klasa zawierająca górny panel menu gry.'''
    def __init__(self, menuObject):
        imageRect = menuObject.image.get_rect()
        super().__init__(menuObject.posX, menuObject.posY, imageRect.w, imageRect.h)
        self.options = []

    def getSelectedOption(self, x, y):
        for option in self.options:
            if option.checkIfSelected(x, y):
                return option
        return None
