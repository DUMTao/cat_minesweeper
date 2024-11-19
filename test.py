# import the pygame module 
import pygame 

'''  
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
'''

import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = 10, 10
NUM_MINES = 10
BACKGROUND_COLOR = (200, 200, 200)
TILE_COLOR = (255, 255, 255)
REVEALED_COLOR = (180, 180, 180)
MINE_COLOR = (255, 0, 0)
FONT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Font
font = pygame.font.Font(None, 36)

# Tile Class
class Tile:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0

    def reveal(self):
        self.is_revealed = True

# Game Class
class Minesweeper:
    def __init__(self):
        self.grid = [[Tile() for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.place_mines()
        self.calculate_adjacent_mines()
    
    def place_mines(self):
        mines_placed = 0
        while mines_placed < NUM_MINES:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if not self.grid[y][x].is_mine:
                self.grid[y][x].is_mine = True
                mines_placed += 1

    def calculate_adjacent_mines(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x].is_mine:
                    continue
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= x + dx < GRID_WIDTH and 0 <= y + dy < GRID_HEIGHT:
                            if self.grid[y + dy][x + dx].is_mine:
                                self.grid[y][x].adjacent_mines += 1

    def reveal_tile(self, x, y):
        if not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT):
            return
        tile = self.grid[y][x]
        if tile.is_revealed:
            return
        tile.reveal()
        if tile.adjacent_mines == 0 and not tile.is_mine:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    self.reveal_tile(x + dx, y + dy)

    def draw(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                tile = self.grid[y][x]
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile.is_revealed:
                    pygame.draw.rect(screen, REVEALED_COLOR, rect)
                    if tile.is_mine:
                        pygame.draw.circle(screen, MINE_COLOR, rect.center, TILE_SIZE // 4)
                    elif tile.adjacent_mines > 0:
                        text = font.render(str(tile.adjacent_mines), True, FONT_COLOR)
                        screen.blit(text, text.get_rect(center=rect.center))
                else:
                    pygame.draw.rect(screen, TILE_COLOR, rect)
                pygame.draw.rect(screen, BACKGROUND_COLOR, rect, 2)

# Main Loop
def main():
    game = Minesweeper()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    game.reveal_tile(x // TILE_SIZE, y // TILE_SIZE)

        screen.fill(BACKGROUND_COLOR)
        game.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()