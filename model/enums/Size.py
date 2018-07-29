# Python 3.6.3, Windows, PyCharm
from enum import Enum


class Size(Enum):
    '''Klasa typu Enum zawierająca stałe dotyczące rozmiaru elementów gry.'''
    FIELD_SIZE = 68
    FIELD_SIZE_X2 = 136
    BOARD_OFFSET = 28
    DISPLAY_WIDTH = 600
    DISPLAY_HIGHT = 700
    def __str__(self):
        return str(self.value)