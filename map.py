import pygame

from settings import *


class Map:
    def __init__(self) -> None:
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def has_wall_at(self, x, y):
        return self.grid[int(y // TILESIZE)][int(x // TILESIZE)] != 0

    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE

                if self.grid[i][j] == 0:
                    pygame.draw.rect(
                        screen, (255, 255, 255), (tile_x, tile_y, TILESIZE - 1, TILESIZE - 1),
                    )
                else:
                    pygame.draw.rect(
                        screen, (0, 0, 0), (tile_x, tile_y, TILESIZE - 1, TILESIZE - 1)
                    )
