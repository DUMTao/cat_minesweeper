# Importing
import random
import pygame as py
import os

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