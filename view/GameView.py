# Python 3.6.3, Windows, PyCharm
import pygame

from model.drawableObjects.impl.MenuGameOver import MenuGameOver
from model.enums.Size import Size


class GameView:
    '''Klasa odpowiedzialna z wyświetlania i odświerzanie widków graficznych komponentów gry.'''
    def __init__(self, board, checkers, menuScore, menuOptions):
        "Konstruktor ustalający rozmiary okna gry, przyjmujący jako argumenty elementy graficzne."
        self.display_w = Size.DISPLAY_WIDTH.value
        self.display_h = Size.DISPLAY_HIGHT.value
        self.gameDisplay = pygame.display.set_mode((self.display_w, self.display_h))
        pygame.display.set_caption('PyGame Checkers by Mateusz Żebrowski 95281')
        self.board = board
        self.menuScore = menuScore
        self.menuOptions = menuOptions
        self.checkers = checkers
        self.menuGameover = MenuGameOver()
        self.initGameView()

    def updateBoard(self):
        self.board.updateView(self.gameDisplay, self.board.posX, self.board.posY)

    def updateMenuScore(self):
        self.menuScore.updateView(self.gameDisplay, self.menuScore.posX, self.menuScore.posY)

    def updateCheckers(self):
        self.checkers.updateCheckers(self.gameDisplay)

    def updateMenuOptions(self):
        self.menuOptions.updateView(self.gameDisplay, self.menuOptions.posX, self.menuOptions.posY)

    def updateMenuGameOver(self):
        self.menuGameover.updateView(self.gameDisplay, self.menuGameover.posX, self.menuGameover.posY)

    def initGameView(self):
        self.board.posX = 0
        self.board.posY = self.display_h - 600

    def update(self):
        '''Metoda odświeżająca główny ekran programu.'''
        pygame.display.update()
