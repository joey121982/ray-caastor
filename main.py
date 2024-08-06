import pygame

from settings import *
from map import Map
from player import Player
from raycaster import Raycaster
from controls import Controls

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()
player = Player()
controls = Controls(FISH_EYE_EFFECT, SHADING_EFFECT, SHADING_DISTANCE)
raycaster = Raycaster(player, map, controls)

clock = pygame.time.Clock()

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

timer = 0
while True:
    if timer == 240:
        timer = 0
    timer += 1

    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_image, (0, 0))

    player.update()

    if timer % 10 == 0:
        controls.update()

    raycaster.castAllRays()

    # map.render(screen)
    # player.render(screen)
    raycaster.render(screen)

    pygame.display.update()
