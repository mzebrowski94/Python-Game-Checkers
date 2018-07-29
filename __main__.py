# Python 3.6.3, Windows, PyCharm
from GameMain import GameMain


def main():
    "Klasa służaca jako miejsce rozpoczęcia działania programu."
    gameMain = GameMain()
    gameMain.initComponents()
    gameMain.run()


if __name__ == '__main__':
    main()
