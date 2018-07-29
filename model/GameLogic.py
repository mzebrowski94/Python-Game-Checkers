# Python 3.6.3, Windows, PyCharm
from math import fabs

import pygame

from controller.result.ResultType import ResultType
from model.drawableObjects.impl.Board import Board
from model.drawableObjects.impl.MenuOptions import MenuOptions
from model.drawableObjects.impl.MenuPanel import MenuPanel
from model.enums.PlayerColor import PlayerColor
from model.gameObjects.Checkers import Checkers
from model.gameObjects.Player import Player
from model.gamePanels.impl.BoardPane import BoardPane
from model.gamePanels.impl.MenuOptionsPane import MenuOptionsPane
from model.gamePanels.impl.MenuPane import MenuPane
from model.utilObjects.GameFilesManager import GameFilesManager


class GameLogic:
    '''Klasa odpowiedzialna, za przebieg działania gry,
    logikę aplikacji, zawiera metody sterowania obiektami programu'''
    def __init__(self):
        '''Konstruktor inicjalizujący główne obiekty potrzebne do działania logiki programu.'''
        self.board = Board()
        self.boardPane = BoardPane(self.board)
        self.menuScore = MenuPanel()
        self.menuOptions = MenuOptions()
        self.menuOptionsPane = MenuOptionsPane(self.menuOptions)
        self.menuPane = MenuPane(self.menuScore)
        self.checkers = Checkers()
        self.gameFilesManager = GameFilesManager()
        self.isGameOver = False

        self.playerBlack = None
        self.playerWhite = None
        self.selectedField = None
        self.selectedChecker = None
        self.actualPlayerColor = None
        self.highlightedOption = None
        self.selectedOption = None
        self.capturedField = None
        self.gameRunning = False

    def initCreatingGame(self):
        '''Metoda inicjalizująca pola wykorzystywane do obsługi sterowania programu.'''
        self.isGameOver = False
        self.selectedField = None
        self.selectedChecker = None
        self.highlightedOption = None
        self.selectedOption = None
        self.capturedField = None
        self.boardPane.clearfields()

    def createNewGame(self):
        '''Metoda wykonująca inicjalizację pól i odpowiednie metody
         podczas tworzenia nowej parti gry.'''
        self.playerBlack = Player(PlayerColor.BLACK)
        self.playerWhite = Player(PlayerColor.WHITE)
        self.initCreatingGame()
        self.checkers.initCheckers(self.boardPane.fields)
        self.actualPlayerColor = PlayerColor.WHITE

    def createGameFromLoad(self):
        '''Metoda wykonująca inicjalizację pól i odpowiednie metody
         podczas tworzenia parti gry z wczytanego pliku.'''
        self.initCreatingGame()
        self.actualPlayerColor = self.gameFilesManager.loadedPlayerColor
        self.checkers.assignCheckersToFieldList(self.gameFilesManager.loadedCheckers, self.boardPane)
        self.playerBlack.checkersAmount = len(self.checkers.blackCheckers)
        self.playerWhite.checkersAmount = len(self.checkers.whiteCheckers)

    def getSelectedPane(self, x, y):
        '''Metoda zwracająca wskazany panel.'''
        if self.boardPane.checkIfSelected(x, y):
            return self.boardPane.getSelectedField(x, y)
        elif self.menuOptionsPane.checkIfSelected(x, y):
            return self.menuOptionsPane.getSelectedOption(x, y)

    def selectChecker(self, field):
        '''Metoda służąca do wybrania odpowiedniego piona gry.'''
        self.selectedField = field
        self.selectedChecker = field.checker
        self.selectedChecker.updateImage()

    def isCheckerSelected(self):
        '''Metoda zwracająca czy aktualnie jakiś pion jest wybrany.'''
        return self.selectedChecker is not None

    def isSameFieldSelected(self, field):
        '''Metoda sprawdzająca czy pddane pole nie jest już polem wybranym.'''
        return self.selectedField is field

    def unselectChecker(self):
        '''Metoda odznaczająca wybrany pion.'''
        self.selectedChecker.updateImage()
        self.selectedChecker = None

    def isCheckerOnField(self, field):
        '''Metoda sprawdająca czy da wskazanym polu znajduje się pion'''
        return field.checker is not None

    def isPlayerChecker(self, checker):
        '''Metoda sprawdająca czy dany pion należy do gracza.'''
        return checker.playerColor.value is self.actualPlayerColor.value

    def isOptionHighlighted(self):
        '''Metoda sprawdzająca czy jest poświetlona któraś opcja.'''
        if self.highlightedOption is not None:
            return self.highlightedOption.isLighting
        else:
            return False

    def highlightOption(self, option):
        '''Metoda podświetlająca wybrana opcję.'''
        if self.isOptionHighlighted():
            if self.highlightedOption is not option:
                option.updateImage()
                self.highlightedOption.updateImage()
                self.highlightedOption = option
            else:
                pass
        else:
            self.highlightedOption = option
            self.highlightedOption.updateImage()

    def unhighlightOption(self):
        '''Metoda wyłączająca podświetlenie danej opcji.'''
        self.highlightedOption.isLighting = False
        self.highlightedOption = None

    def isNewCheckerSelected(self, targetField):
        '''Metoda sprawdzajaca czy wybrany został nowy pion.'''
        if targetField.checker is not None:
            if self.actualPlayerColor is targetField.checker.playerColor:
                return True
            else:
                return False
        return False

    def proceedNewCheckerSelection(self, targetField):
        '''Metoda przeprowadzajaca wybranie nowego piona.'''
        self.unselectChecker()
        self.selectChecker(targetField)

    def getMovingResultType(self, targetField):
        '''Metoda sprawdzająca czy można wykonać ruch:
        zwykły bądź bicie.'''
        distanceX = self.selectedField.x - targetField.x
        distanceY = self.selectedField.y - targetField.y

        if self.isNormalMoveAvaible(distanceX, distanceY):
            return ResultType.MOVE
        elif self.isCaptureMoveAvaible(targetField.x, targetField.y, distanceX, distanceY):
            return ResultType.CAPTURE
        else:
            return ResultType.NO_ACTION

    def isNormalMoveAvaible(self, distanceX, distanceY):
        '''Metoda sprawdzająca czy zwykly ruch jest możliwy.'''
        if fabs(distanceX) == fabs(distanceY) and (fabs(distanceX) == 68 or self.selectedChecker.isKing):
            return True
        else:
            return False

    def isCaptureMoveAvaible(self, targetFieldX, targetFieldY, distanceX, distanceY):
        '''Metoda sprawdzająca czy możliwe jest bicie.'''
        targetField = self.boardPane.getField(targetFieldX, targetFieldY)
        if targetField is not None:
            if not self.isCheckerOnField(targetField):
                if fabs(distanceX) == fabs(distanceY) and (fabs(distanceX) == 136 or self.selectedChecker.isKing):
                    if distanceX > 0:
                        capturedFieldX = targetFieldX + 68
                    else:
                        capturedFieldX = targetFieldX - 68

                    if distanceY > 0:
                        capturedFieldY = targetFieldY + 68
                    else:
                        capturedFieldY = targetFieldY - 68

                    self.capturedField = self.boardPane.getField(capturedFieldX, capturedFieldY)

                    if self.capturedField is not None:
                        if self.capturedField.checker is not None:
                            if self.capturedField.checker.playerColor is not self.actualPlayerColor:
                                return True
                return False
            else:
                return False
        else:
            return False


    def moveChecker(self, targetField):
        '''Metoda służąca do przemieszczenia piona po planszy.'''
        targetField.assignChecker(self.selectedChecker)
        self.selectedField.unAssignChecker()


    def captureChecker(self):
        '''Metoda służąca do odliczania pionów zbitych przez graczy.'''
        if self.actualPlayerColor is PlayerColor.BLACK:
            self.checkers.removeWhiteChecker(self.capturedField.checker)
            self.playerWhite.checkersAmount -= 1
        else:
            self.checkers.removeBlackChecker(self.capturedField.checker)
            self.playerBlack.checkersAmount -= 1

        self.capturedField.unAssignChecker()


    def checkPlayersStatus(self):
        '''Metoda sprawdzająca czy nie zostały spełnione ostateczne warunki gry.
        Czyli czy któryś z graczy nie ma już pionów.'''
        print(self.playerBlack.checkersAmount)
        print(self.playerWhite.checkersAmount)
        if self.playerBlack.checkersAmount == 0:
            self.isGameOver = True
        elif self.playerWhite.checkersAmount == 0:
            self.isGameOver = True


    def save(self):
        '''Metoda służąca do wywołania zapisu stanu gry.'''
        self.gameFilesManager.saveGame(self.boardPane.fields, self.actualPlayerColor)


    def load(self):
        '''Metoda służąca do wywołania wczytania stanu gry.'''
        self.gameFilesManager.loadGame()


    def quit(self):
        '''Metoda służąca do wyłączenia programu.'''
        pygame.quit()
        quit()
