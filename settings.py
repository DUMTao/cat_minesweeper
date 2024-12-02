# Importing
import pygame
import os
import random




dark_grey = (40, 40, 40)
light_gray = (100, 100, 100)
gween = (0, 255, 0)

bg_color = gween


# Global game settings
tile_size = 32
rows = 15
columns = 15
#---------------------

title = "MewoSweeper!"

# Making the amount of mines spawned in the game dynamic
AMOUNT_MINES = random.randint(7, 10)
width = tile_size * rows
height = tile_size * columns
FPS = 60

tile_numbers = []

for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Tile{i}.png")), (tile_size, tile_size)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileEmpty.png")), (tile_size, tile_size))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileCookie.png")), (tile_size, tile_size))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileFlag.png")), (tile_size, tile_size))
tile_catmine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileCatcus.png")), (tile_size, tile_size))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileUnknown.png")), (tile_size, tile_size))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileNotMine.png")), (tile_size, tile_size))
