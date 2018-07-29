# Python 3.6.3, Windows, PyCharm
import pygame
from controller.GameEventsHandler import GameEventsHandler
from model.GameLogic import GameLogic
from model.GameLoop import GameLoop
from view.GameView import GameView


class GameMain:
    '''Klasa inicjalizująca najważniejsze komponenty programu i uruchamiająca główną pętlę gry.'''
    def __init__(self):
        self.gameView = None
        self.gameLoop = None
        self.gameEventsHandler = None
        self.gameLogic = None

    def initComponents(self):
        "Metoda służąca do inicjalizacji głównych komponentów programu."
        status = pygame.init()
        print("PyGame initialization status: " + str(status) + " (Succed/Failure)")
        self.gameLogic = GameLogic()
        self.gameView = GameView(self.gameLogic.board, self.gameLogic.checkers, self.gameLogic.menuScore, self.gameLogic.menuOptions)
        self.gameEventsHandler = GameEventsHandler(self.gameLogic)
        self.gameLoop = GameLoop()

    def run(self):
        "Metoda służaca do uruchomienia głównej pętli gry."
        self.gameLoop.initAndRunNewGame(self.gameView, self.gameEventsHandler, self.gameLogic)


