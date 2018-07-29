# Python 3.6.3, Windows, PyCharm

class Player:
    '''Klasa gracza, zawierająca informację o:
     jego kolorze, stanie pionów i nazwie.'''


    def __init__(self, playerColor):
        self.playerColor = playerColor
        self.name = "".join(str(playerColor)).join(" player")
        self.checkersAmount = 12
