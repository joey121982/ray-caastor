import math

TILESIZE = 64
ROWS = 10
COLS = 15

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FOV = 60 * (math.pi / 180)

RES = 1000 / 250  # resolution, increase the divisor to increase visual quality

NUM_RAYS = int(WINDOW_WIDTH // RES)

# EFFECT SETTINGS

FISH_EYE_EFFECT = False
SHADING_EFFECT = True
SHADING_DISTANCE = 10 # 10 - darker, 60 - normal, 100 - lighter  -- change to anything between 0 and 255
