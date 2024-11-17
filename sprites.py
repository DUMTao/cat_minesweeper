#Imports
import random

import pygame
from settings import *

# ---Tile key---
# "." = unknown
# "X" = cookie
# "C" = clue
# "/" = empty
# --------------


class Tile:
    
    def __init__(self, x, y, image, type, revealed = False, flagged = False):
        self.x, self.y = x * tile_size, y * tile_size
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
        
    # If conditionals for the logic of the cookie finding
    def draw(self, board_surface):
        
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        
        elif self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))
        
    def __repr__(self):
        return self.type
    
class Board:
    
    # When it initializes, it will create the grid where the mines and tiles will be placed
    def __init__(self):
        self.board_surface = pygame.Surface((width, height))
        
        self.board_list = [[Tile(columns, rows, tile_empty, ".") for row in range(rows)] for col in range(columns)]
        self.place_mines()
        self.place_clues()
        
        self.dug = []
    
    # Self Explanatory lol
    def place_mines(self):
        for n in range(mine_ammount):
            while True:
                x = random.randint(0, rows - 1)
                y = random.randint(0, columns - 1)
                
                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_cat
                    self.board_list[x][y].type = "X"
                    
                    break;
        
    def place_clues(self):
        
        for x in range(rows):
            for y in range(columns):
                
                if self.board_list[x][y].type != "X":
                    total_mines = self.around(x, y)
                
                if total_mines > 0:
                    self.board_list[x][y].image = tile_nums[total_mines - 1]
                    self.board_list[x][y].type = "C"
        
    @staticmethod
    def is_inside(x, y):
        return 0 <= x < rows and 0 <= y < columns
    
    # Logic for dealing with the cats around the tiles
    def around(self, x, y):
        total_mines = 0
        
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                x_around = x + x_offset
                y_around = y + y_offset
                
                if self.is_inside(x_around, y_around) and self.board_list[x_around][y_around].type == "X":
                    total_mines += 1
        
        return total_mines
    
    # Updating the board when a tile is dug
    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
            
        screen.blit(self.board_surface, (0, 0))
    
    # Logic for the cookie digging finding 
    def dig_up(self, x, y):
        # Check if the indices are within the valid range
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return
        
        
        self.dug.append((x, y))
        
        # If it's a cookie, the tile will disappear and the cookie will be shown
        # Else, it will be a cookie
        if self.board_list[x][y].type == "X":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_cookie
            
            return False
        
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True
            
            return True
    
        self.board_list[x][y].revealed = True
    
        for row in range(max(0, x - 1), min((rows, x + 1)) + 1):
            for col in range(max(0, y - 1), min(columns, y + 1) + 1):
                
                if (row, col) not in self.dug:
                    self.dig_up(row, col)
        return True
    
    def display_board(self):
        for row in self.board_list:
            print(row)
            
            
            