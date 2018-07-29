# Python 3.6.3, Windows, PyCharm
from enum import Enum


class MenuOption(Enum):
    '''Klasa Enum zawierająca informację o opcji menu.'''
    SAVE = 'Save'
    NEW = 'New'
    LOAD = 'Load'
    QUIT = 'Quit'

    def __str__(self):
        return str(self.value)