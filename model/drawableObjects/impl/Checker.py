# Python 3.6.3, Windows, PyCharm
import pygame

from model.drawableObjects.DrawableObject import DrawableObject


class Checker(DrawableObject):
    '''Klasa obiektu rysowalnego przedstawiająca piona gry.'''
    def __init__(self, playerColor, x, y):
        '''Konstrukor klasy Checker, przyjmujący kolor piona oraz jego położenie.'''
        self.playerColor = playerColor
        self.nonSelectedImage = pygame.image.load("view/img/" + str(self.playerColor) + "Checker.png")
        self.selectedImage = pygame.image.load("view/img/" + str(self.playerColor) + "CheckerL.png")
        self.image = self.nonSelectedImage
        self.posX = x
        self.posY = y
        self.isLighting = False
        self.isKing = False

    def getObjectToSave(self):
        '''Metoda służąca do konwersji najistotniejszych pól piona do dalszego zapisu.'''
        return [self.playerColor.value, self.posX, self.posY, self.isKing]

    def updateView(self, display, x, y):
        self.draw(display, self.posX, self.posY)

    def updateImage(self):
        self.isLighting = not self.isLighting
        if self.isLighting:
            self.image = self.selectedImage
        else:
            self.image = self.nonSelectedImage
