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
tile_size = 40
width = 800
height = 600
#---------------------

title = "MewoSweeper!"
FPS = 60


tile_nums = []

for i in range(1, 9):
    tile_nums.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (tile_size, tile_size)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")), (tile_size, tile_size))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (tile_size, tile_size))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")), (tile_size, tile_size))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileMine.png")), (tile_size, tile_size))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (tile_size, tile_size))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")), (tile_size, tile_size))
