import pygame

from code.Const import SPEED
from code.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name: str, position : tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= SPEED[self.name]