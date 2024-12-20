import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visibile_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visibile_sprites])
                if col == "p":
                    Player((x, y), [self.visibile_sprites])

    def run(self):
        # update and draw the game
        self.visibile_sprites.draw(self.display_surface)
