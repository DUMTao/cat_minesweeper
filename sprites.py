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
    
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.type = tile_type
        self.revealed = False
        self.flagged = False
        self.image = None
        
    def reveal(self):
        self.revealed = True
    
    '''# If conditionals for the logic of the cookie finding
    def draw(self, board_surface):
        
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        
        elif self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))
        
    def __repr__(self):
        return self.type
    '''
    
class Board:
    
    # When it initializes, it will create the grid where the mines and tiles will be placed
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        
        self.board_list = self.initalize_board()
        self.place_mines()
    
    def initalize_board(self):
        return [[Tile(x, y, ' ') for x in range(self.width // tile_size)] for y in range(self.height // tile_size)]
    
    
    # Self Explanatory lol
    def place_mines(self):
        mines_placed = 0
        
        while mines_placed < self.num_mines:
            x = random.randint(0, len(self.board_list[0]) - 1)
            y = random.randint(0, len(self.board_list) - 1)
            
            if 0 <= x < len(self.board_list) and 0 <= y < len(self.board_list[x]):
                self.board_list[x][y].type = 'X'
                mines_placed += 1
            
    def dig_up(self, x, y):
        # Check if the indices are within the valid range
        if x < 0 or x >= len(self.board_list[0]) or y < 0 or y >= len(self.board_list):
            return
        
        self.board_list[y][x].revealed = True
    
    
    
    
    '''   
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
    '''
            
            