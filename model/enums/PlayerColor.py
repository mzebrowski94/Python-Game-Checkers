# Python 3.6.3, Windows, PyCharm
from enum import Enum


class PlayerColor(Enum):
    '''Klasa typu Enum zawierająca informację o kolorach graczy.'''
    WHITE = 'White'
    BLACK = 'Black'

    def __str__(self):
        return str(self.value)