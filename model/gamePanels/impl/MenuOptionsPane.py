# Python 3.6.3, Windows, PyCharm
from model.enums.MenuOption import MenuOption
from model.gamePanels.GamePane import GamePane
from model.gamePanels.impl.OptionPane import OptionPane


class MenuOptionsPane(GamePane):
    '''Klasa odpowiadajaca za panel wyboru opcji menu. Przechowuje graficzne elementy wszystkich opcji. '''
    def __init__(self, menuOptionsObject):
        imageRect = menuOptionsObject.image.get_rect()
        super().__init__(menuOptionsObject.posX, menuOptionsObject.posY, imageRect.w, imageRect.h)
        self.options = self.initOptions(menuOptionsObject.posX, menuOptionsObject.posY)
        menuOptionsObject.optionPanes = self.options

    def initOptions(self, posX, posY):
        '''Metoda inicjalizująca obiekty graficzne opcji.'''
        options = []
        options.append(OptionPane(posX + 41, posY + 4, 47, 24, MenuOption.SAVE))
        options.append(OptionPane(posX + 111, posY + 18, 45, 25, MenuOption.NEW))
        options.append(OptionPane(posX + 53, posY + 43, 50, 23, MenuOption.LOAD))
        options.append(OptionPane(posX + 126, posY + 57, 44, 23, MenuOption.QUIT))
        return options

    def getSelectedOption(self, x, y):
        '''Metoda zwracająca wskazaną opcję.'''
        for option in self.options:
            if option.checkIfSelected(x, y):
                return option
        return None
