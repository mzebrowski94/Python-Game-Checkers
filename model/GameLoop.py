# Python 3.6.3, Windows, PyCharm
import pygame

from controller.result.Result import Result
from controller.result.ResultType import ResultType
from model.enums.MenuOption import MenuOption
from model.enums.PlayerColor import PlayerColor


class GameLoop:
    '''Klasa służąca jako główna pętla gry, zawarte w niej jest sterowanie najwyższego poziomu.'''

    def __init__(self):
        self.clock = self.clock = pygame.time.Clock()

    def initAndRunNewGame(self, gameView, gameEventsHandler, gameLogic):
        '''Metoda służąca do inicjalizacji i uruchomienia nowej partii gry.'''
        gameLogic.createNewGame()
        gameView.menuScore.updateImage(gameLogic.actualPlayerColor)
        self.run(gameView, gameEventsHandler, gameLogic)

    def initAnDRunLoadedGame(self, gameView, gameEventsHandler, gameLogic):
        '''Metoda służąca do uruchomienia partii gry z wczytanych danych.'''
        gameLogic.createGameFromLoad()
        gameView.menuScore.updateImage(gameLogic.actualPlayerColor)
        self.run(gameView, gameEventsHandler, gameLogic)

    def run(self, gameView, gameEventsHandler, gameLogic):
        '''Metoda służąca jako główna pętla gry, w niej wywoływana jest
        interakcja z użytkownikiem i ciągłe odświeżanie stanu programu,
        odświeżanie grafiki ekrranu'''
        actionResult = Result(ResultType.NO_ACTION)
        changePlayer = False
        gameLogic.gameRunning = True

        while gameLogic.gameRunning:

            if changePlayer:
                self.prepareNextTurn(gameLogic, gameView)
                actionResult.type = ResultType.NO_ACTION
                changePlayer = False

            for event in pygame.event.get():

                if event.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    gameEventsHandler.highlightIfOptionPointed(x, y)

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    actionResult = gameEventsHandler.proceedAction(x, y)

                    if actionResult.type is ResultType.MOVE:
                        gameEventsHandler.proceedMovingChecker(actionResult.targetField)
                        changePlayer = True
                    elif actionResult.type is ResultType.CAPTURE:
                        gameEventsHandler.proceedCaptureChecker(actionResult.targetField)
                        changePlayer = not gameEventsHandler.isNextCaptureAvailable(actionResult.targetField)
                    elif actionResult.type is ResultType.OPTION:
                        actionResult = gameEventsHandler.proceedOptionExecution(gameLogic, actionResult)


                elif event.type == pygame.QUIT:
                    gameLogic.quit()
                    # print(event)

            gameView.updateBoard()
            gameView.updateMenuScore()
            gameView.updateMenuOptions()
            gameView.updateCheckers()
            if gameLogic.isGameOver:
                gameView.updateMenuGameOver()
            gameView.update()

            self.clock.tick(60)

        if actionResult.option is MenuOption.NEW:
            self.initAndRunNewGame(gameView, gameEventsHandler, gameLogic)
        elif actionResult.option is MenuOption.LOAD:
            self.initAnDRunLoadedGame(gameView, gameEventsHandler, gameLogic)

    def prepareNextTurn(self, gameLogic, gameView):
        '''Metoda wykorzystywana przy zmienie ustawień podczas nowej tury gry.'''
        if gameLogic.actualPlayerColor is PlayerColor.BLACK:
            gameLogic.actualPlayerColor = PlayerColor.WHITE
        else:
            gameLogic.actualPlayerColor = PlayerColor.BLACK
        gameView.menuScore.updateImage(gameLogic.actualPlayerColor)
