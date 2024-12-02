# Importing
import pygame
import os


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
TILESIZE = 32
ROWS = 15
COLS = 15
#---------------------

title = "MewoSweeper!"


AMOUNT_MINES = 5
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60

tile_numbers = []

for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileEmpty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileCookie.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_catmine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileCatcus.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileUnknown.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileNotMine.png")), (TILESIZE, TILESIZE))
