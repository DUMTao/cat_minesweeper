import random

import pygame
from settings import *

# types list
# "." -> unknown
# "X" -> cat
# "C" -> nums
# "/" -> empty


class Tile:
    def __init__(self, x, y, image, type, revealed= False, flagged= False):
        self.x, self.y = x * tile_size, y * tile_size
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    # Assigns the default tile type to be unknown; 
    # if it's left clicked, it will change to either a number tile, a cat tile, or an empty tile
    # if it's right clicked, it will flag the tile
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
    
    def __init__(self):
        self.board_surface = pygame.Surface((width, height))
        self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(rows)] for col in range(columns)]
        self.place_mines()
        self.place_clues()
        self.dug = []

    # Logic that prevents from mines spawning outside of the range of the width and height
    def place_mines(self):
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, rows-1)
                y = random.randint(0, columns-1)

                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_catmine
                    self.board_list[x][y].type = "X"
                    break

    # Logic for how the clues are placed around the cats
    def place_clues(self):
        for x in range(rows):
            for y in range(columns):
                if self.board_list[x][y].type != "X":
                    total_mines = self.check_neighbours(x, y)
                    if total_mines > 0:
                        self.board_list[x][y].image = tile_numbers[total_mines-1]
                        self.board_list[x][y].type = "C"

    # Follow-up method for checking that mines are not placed outside of the board and it returns their location
    @staticmethod
    def is_inside(x, y):
        return 0 <= x < rows and 0 <= y < columns

    # Logic for tile numbers assigned nearby the cats
    # If there is a mine around a 3x3 grid, the tile number will display on top of the empty tile
    def check_neighbours(self, x, y):
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                neighbor_x = x + x_offset
                neighbor_y = y + y_offset
                if self.is_inside(neighbor_x, neighbor_y) and self.board_list[neighbor_x][neighbor_y].type == "X":
                  total_mines += 1

        return total_mines

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def dig(self, x, y):
        self.dug.append((x, y))
        if self.board_list[x][y].type == "X":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True
            return True

        self.board_list[x][y].revealed = True

        for row in range(max(0, x-1), min(rows-1, x+1) + 1):
            for col in range(max(0, y-1), min(columns-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def display_board(self):
        for row in self.board_list:
            print(row)