# Python 3.6.3, Windows, PyCharm

from abc import abstractmethod, ABC

import pygame

class DrawableObject(ABC):
    '''Klasa abstrakcyjna opisująca funkcjonalność graficznych obiektów w grze.'''

    def __init__(self, imagePath):
        '''Konstruktor klasy DrawableObject przyjmujący jako argument ścieżkę do pliku graficznego.'''
        self.image = pygame.image.load(imagePath)
        self.posX = 0
        self.posY = 0

    def setPos(self, x, y):
        '''Metoda pozwalająca na zmianę koordynatów położeia obiektu na planszy.'''
        self.posX = x
        self.posY = y

    def draw(self, display, x, y):
        '''Metoda rysująca grafikę obiektu na ekranie gry.'''
        display.blit(self.image, (x, y))

    @abstractmethod
    def updateImage(self):
        '''Metoda abstrakcyjna opisująca zmianę grafiki obiektu.'''
        pass

    @abstractmethod
    def updateView(self, display, x, y):
        '''Metoda abstrakcyjna opisująca kontekst wywołania metody draw.'''
        pass
