# Python 3.6.3, Windows, PyCharm
from enum import Enum


class ResultType(Enum):
    '''Klasa typu Enum zawierająca typy rezultatów zwracane przez komponenty'''
    MOVE = 'Moved'
    CAPTURE = 'Captured'
    SELECT = 'Selected'
    UNSELECT = 'Unselected'
    CHANGE_TO_KING = "Changed to King"
    NO_ACTION = "No action"
    OPTION = "Option"

    def __str__(self):
        return str(self.value)
