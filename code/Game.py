import pygame

from code.Menu import Menu


class Game:
    def __init__(self, window):
        pygame.init()
        # Create the game's window
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        # To use the packege it must be initialized.
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close window
            #         quit()  # End pygame

