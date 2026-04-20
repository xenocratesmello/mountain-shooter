import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Create the game's window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # To use the packege it must be initialized.
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

