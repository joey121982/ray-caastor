import math

TILESIZE = 64
ROWS = 10
COLS = 15

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FOV = 60 * (math.pi / 180)

RES = 1000 / 250  # resolution, increase the divisor to increase visual quality

NUM_RAYS = int(WINDOW_WIDTH // RES)
