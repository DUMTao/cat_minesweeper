# Imports
import pygame
from settings import *
from sprites import *
import os


class DaGame:
    
    # Function to initialize the game with the given setting parameters
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        
    
    # Function for every new game
    def new(self):
        self.board = Board(width, height, num_mines=10)
        #self.board.display_board()
        
        self.playing = True
    
    
    # Function that sets the framerate while the program runs
    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        
    
    # Setting the appareance of the window
    def draw(self):
        self.screen.fill(bg_color)
        for row in self.board.board_list:
            for tile in row:
                if tile.revealed:
                    color = (200, 200, 200)  # Revealed tile color
                    if tile.type == 'X':
                        color = (255, 0, 0)  # Red for mines
                    pygame.draw.rect(self.screen, color, (tile.x * tile_size, tile.y * tile_size, tile_size, tile_size))
                else:
                    pygame.draw.rect(self.screen, (100, 100, 100), (tile.x * tile_size, tile.y * tile_size, tile_size, tile_size))  # Hidden tile
        pygame.display.flip()
    
    
    
    # So the pop up window, yk actually shows up with the event
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                gx, gy = pygame.mouse.get_pos()
                gx //= tile_size
                gy //= tile_size
                if event.button == 1:  # Left click
                    self.board.board_list[gy][gx].reveal()
                    if self.board.board_list[gy][gx].type == 'X':
                        self.playing = False  # Game over
                if event.button == 3:  # Right click
                    tile = self.board.board_list[gy][gx]
                    tile.flagged = not tile.flagged  # Toggle flag

    """
    def reset_game(self):
        self.board_list = self.initialize_board()  # Reinitialize the board
        self.dug = []  # Clear the dug tiles
        self.total_mines = self.calculate_mines()  # Recalculate mines
        self.board_surface.fill((0, 0, 0))  # Clear the board surface
        self.draw(screen) # type: ignore
    """   


game = DaGame()

while True:
    game.new()
    game.run()