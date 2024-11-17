# Importing
import random

import pygame as py
import os
from settings import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
bg_color = LIGHTGREY


# Global game settings
tile_size = 32
rows = 15
columns = 15
#---------------------

title = "MewoSweeper!"

FPS = 60

width = tile_size * rows
height = tile_size * columns


mine_ammount = random.randint(1, 6)

tile_nums = []

# Making sure that the tile pngs scale to the size of the time_size variable
for i in range(1, 9):
    tile_nums.append(py.transform.scale(py.image.load(os.path.join("Assets", f"Tile{i}.png")), (tile_size, tile_size)))
    
# Setting up the png's for the tiles
tile_empty = py.transform.scale(py.image.load(os.path.join("Assets", "TileEmpty.png")), (tile_size, tile_size))

# Tile exloded
tile_cookie = py.transform.scale(py.image.load(os.path.join("Assets", "TileCookie.png")), (tile_size, tile_size))

tile_flag = py.transform.scale(py.image.load(os.path.join("Assets", "TileFlag.png")), (tile_size, tile_size))
tile_cat = py.transform.scale(py.image.load(os.path.join("Assets", "TileCatcus.png")), (tile_size, tile_size))
tile_unknown = py.transform.scale(py.image.load(os.path.join("Assets", "TileUnknown.png")), (tile_size, tile_size))
tile_not_cookie = py.transform.scale(py.image.load(os.path.join("Assets", "TileNotMine.png")), (tile_size, tile_size))