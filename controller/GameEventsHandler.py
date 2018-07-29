# Python 3.6.3, Windows, PyCharm

from controller.result.Result import Result
from controller.result.ResultType import ResultType
from model.enums.MenuOption import MenuOption
from model.enums.Size import Size
from model.gamePanels.impl.FieldPane import FieldPane
from model.gamePanels.impl.OptionPane import OptionPane


class GameEventsHandler:
    '''Klasa służaca do wywoływnia odpowiednich metod
    klasy gameLogic w odpowiedzi na przebieg sterowania
    głowniej pętli gry'''

    def __init__(self, gameLogic):
        self.gameLogic = gameLogic

    def proceedAction(self, x, y):
        '''Metoda wywoływana gdy gracz naciśnie przycisk myszy,
        służy do przekierowania sterowania ze względu na wybrany panel.'''
        pane = self.gameLogic.getSelectedPane(x, y)
        if isinstance(pane, FieldPane):
            actionResult = self.proceedFieldSelection(self.gameLogic, pane)
        elif isinstance(pane, OptionPane):
            actionResult = self.proceedOptionSelection(pane)
        else:
            actionResult = Result(ResultType.NO_ACTION)
        return actionResult

    def proceedFieldSelection(self, gameLogic, field):
        '''Metoda wywoływana gdy gracz wciśnie
        przycisk myszy na wybranym polu planszy.
        Służy do przekierowania sterowania ze względu na
        rodzaj pola.'''

        if gameLogic.isCheckerSelected():
            if gameLogic.isSameFieldSelected(field):
                gameLogic.unselectChecker()
                return Result(ResultType.UNSELECT)
            else:
                if gameLogic.isCheckerOnField(field):
                    if gameLogic.isNewCheckerSelected(field):
                        gameLogic.proceedNewCheckerSelection(field)
                        return Result(ResultType.SELECT)
                    else:
                        pass
                else:
                    return self.getMovingResult(field)

        else:
            if gameLogic.isCheckerOnField(field):
                if gameLogic.isPlayerChecker(field.checker):
                    gameLogic.selectChecker(field)
                    return Result(ResultType.SELECT)
                else:
                    pass
            else:
                pass
        return Result(ResultType.NO_ACTION)

        # print("Field clicked at: " + str(x) + ":" + str(y))

    def getMovingResult(self, field):
        '''Metoda służąca do wysłania resultatu dotyczącego
        zmiany położenia pionka na planszy'''

        movingResultType = self.gameLogic.getMovingResultType(field)
        movingResult = Result(movingResultType)
        movingResult.targetField = field
        return movingResult

    def proceedMovingChecker(self, targetField):
        '''Metoda wywołująca przemieszczenie pionka na planszy'''
        self.gameLogic.moveChecker(targetField)
        self.gameLogic.unselectChecker()

    def proceedCaptureChecker(self, targetField):
        '''Metoda wywołująca zbicie pionka,
        odjęcie punktów przecinikowi i sprawdzenie
         statusu graczy.'''

        self.gameLogic.moveChecker(targetField)
        self.gameLogic.captureChecker()
        self.gameLogic.checkPlayersStatus()
        self.gameLogic.selectedField = targetField

    def isNextCaptureAvailable(self, actualCheckerField):
        ''' Metoda wywołująca sprawdzenie czy są dostępne kolejne piony do zbicia. '''
        moveSize = Size.FIELD_SIZE_X2.value
        if self.isCaptureAvaibleFromField(actualCheckerField, moveSize, moveSize):
            return True
        elif self.isCaptureAvaibleFromField(actualCheckerField, moveSize, -moveSize):
            return True
        elif self.isCaptureAvaibleFromField(actualCheckerField, -moveSize, moveSize):
            return True
        elif self.isCaptureAvaibleFromField(actualCheckerField, -moveSize, -moveSize):
            return True
        else:
            self.gameLogic.unselectChecker()
            return False

    def isCaptureAvaibleFromField(self, targetField, distanceX, distanceY):
        ''' Metoda wywołująca sprawdzenie czy są dostępne kolejne piony do zbicia. '''
        if self.gameLogic.isCaptureMoveAvaible(targetField.x + distanceX, targetField.y + distanceY, -distanceY,
                                               -distanceX):
            return True
        else:
            return False

    def highlightIfOptionPointed(self, x, y):
        '''Metoda służaca do wywołania podświetlania opcji menu po najechaniu myszą.'''
        pane = self.gameLogic.getSelectedPane(x, y)
        if isinstance(pane, OptionPane):
            self.gameLogic.highlightOption(pane.option)
        else:
            if self.gameLogic.isOptionHighlighted():
                self.gameLogic.unhighlightOption()

    def proceedOptionSelection(self, optionPane):
        '''Metoda służąca do wysłania resultatu dotyczącego
        wybranej opcji'''
        optionResult = Result(ResultType.OPTION)
        optionResult.option = optionPane.option.menuOption
        return optionResult

    def proceedOptionExecution(self, gameLogic, optionResult):
        '''Metoda sterująca przebiegiem wywoływania
        funkcjonalności związanych z opcjami menu gry.'''
        if optionResult.option is MenuOption.NEW:
            gameLogic.gameRunning = False
        elif optionResult.option is MenuOption.QUIT:
            gameLogic.quit()
        elif optionResult.option is MenuOption.SAVE:
            gameLogic.save()
        elif optionResult.option is MenuOption.LOAD:
            gameLogic.load()
            gameLogic.gameRunning = False

        if gameLogic.isOptionHighlighted():
            gameLogic.unhighlightOption()
        return optionResult
