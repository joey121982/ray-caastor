import pygame

from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player, map, controls) -> None:
        self.rays = []
        self.player = player
        self.map = map
        self.controls = controls

    def castAllRays(self):
        self.rays = []
        rayAngle = (self.player.rotationAngle - FOV / 2)
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map, self.controls)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS

    def render(self, screen):

        i = 0
        for ray in self.rays:
            # ray.render(screen)

            line_height = (TILESIZE / ray.distance) * 415

            draw_begin = WINDOW_HEIGHT / 2 - line_height / 2
            draw_end = line_height

            pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i * RES, draw_begin, RES, draw_end))

            i += 1