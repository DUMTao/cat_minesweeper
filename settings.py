# Importing
import random

# Global game settings
tile_size = 32
rows = 15
columns = 15
title = "MewoSweeper!"

FPS = 60

mine_ammount = random.randint(1, 6)
    
width = tile_size * rows
height = tile_size * columns