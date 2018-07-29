# Python 3.6.3, Windows, PyCharm
from model.enums.Size import Size
from model.gamePanels.GamePane import GamePane
from model.gamePanels.impl.FieldPane import FieldPane


class BoardPane(GamePane):
    '''Klasa opisująca panel planszy i jego obsługę, posiadająca odwołanie do wszystkich pól planszy.'''
    def __init__(self, boardObject):
        imageRect = boardObject.image.get_rect()
        super().__init__(boardObject.posX, boardObject.posY, imageRect.w, imageRect.h)
        self.fields = self.initFields(boardObject.posX + Size.BOARD_OFFSET.value, boardObject.posY + Size.BOARD_OFFSET.value)

    def initFields(self, posX, posY):
        '''Metoda inicjalizująca pola planszy w odpowiedniej ilości i odległości'''
        fields = []
        for i in range(8):
            y = posY + (i * Size.FIELD_SIZE.value)
            if i % 2 == 0:
                x = posX - Size.FIELD_SIZE.value
            else:
                x = posX - (Size.FIELD_SIZE.value * 2)
            for j in range(4):
                x += Size.FIELD_SIZE.value * 2
                fields.append(FieldPane(x, y))
        return fields

    def clearfields(self):
        '''Metoda czyszcząca wszystkie pola z pionów.'''
        for field in self.fields:
            field.unAssignChecker()

    def getSelectedField(self, x, y):
        '''Metoda zwracająca pole na którę wskazano następującymi współrzędnymi.'''
        for field in self.fields:
            if field.checkIfSelected(x, y):
                return field
        return None

    def getField(self, x, y):
        '''Metoda dostarczająca pole o zadanych współrzędnych.'''
        for field in self.fields:
            if field.x == x and field.y == y:
                return field
        return None
