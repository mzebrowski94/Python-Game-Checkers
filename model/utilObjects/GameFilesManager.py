# Python 3.6.3, Windows, PyCharm
import json
from tkinter import filedialog, Tk

from model.drawableObjects.impl.Checker import Checker
from model.enums.PlayerColor import PlayerColor


class GameFilesManager:
    '''Klasa służąca do zapisywania i wczytywania plików
    JSON dotyczących zapisanych i zapisywanych partii gry.'''
    def __init__(self):
        self.loadedPlayerColor = None
        self.loadedCheckers = []

    def saveGame(self, fields, actualPlayerColor):
        '''Metoda przeprowadzająca zapis stanu gry do pliku JSON'''
        data = {'PlayerColor': actualPlayerColor.value}
        output = []
        for field in fields:
            if field.checker is not None:
                output.append(field.checker.getObjectToSave())

        data['checkers'] = output
        jsonToSave = json.dumps(data)

        root = Tk()
        root.withdraw()
        try:
            file = filedialog.asksaveasfile(mode='w', defaultextension=".json")
            if file is not None:
                file.write(jsonToSave)
        except IOError:
            print("Error during game saving process. (IOError)")

    def loadGame(self):
        '''Metoda przeprowadzająca wczytanie stanu gry z pliku JSON'''
        self.loadedCheckers[:] = []
        self.loadedPlayerColor = None
        root = Tk()
        root.withdraw()
        try:
            file = filedialog.askopenfile(mode='r', defaultextension=".json")
        except IOError:
            print("Error during game loading process. (IOError)")

        if file is not None:
            loadedJson = json.loads(file.read())

            if loadedJson['PlayerColor'] == PlayerColor.WHITE.value:
                self.loadedPlayerColor = PlayerColor.WHITE
            elif loadedJson['PlayerColor'] == PlayerColor.BLACK.value:
                self.loadedPlayerColor = PlayerColor.BLACK
            else:
                print("Wrong json file content")

            for loadedChecker in loadedJson['checkers']:
                if loadedChecker[0] == PlayerColor.WHITE.value:
                    checker = Checker(PlayerColor.WHITE, loadedChecker[1], loadedChecker[2])
                    checker.isKing = loadedChecker[3]
                elif loadedChecker[0] == PlayerColor.BLACK.value:
                    checker = Checker(PlayerColor.BLACK, loadedChecker[1], loadedChecker[2])
                    checker.isKing = loadedChecker[3]
                self.loadedCheckers.append(checker)
