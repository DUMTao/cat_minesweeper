# Imports
import pygame
from settings import *
from sprites import *


class DaGame:
    
    # Function to initialize the game with the given setting parameters
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        
    
    # Function for every new game
    def new(self):
        self.board = Board()
        self.board.display_board()
    
    
    # Function that sets the framerate while the program runs
    def run(self):
        self.playing = True
        
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        
    
    # Setting the appareance of the window
    def draw(self):
        self.screen.fill(bg_color)
        
        pygame.display.flip()
        
    
    # Win conditions
    def win_conditions(self):
        for row in self.board.board_list:
            
            for tile in row:
                if tile.type != "X" and not tile.revealed:
                    return False
        
        return True
    
    
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
                
                if event.button == 1:
                    if not self.board.board_list[gy][gx].flagged:
                        
                        # Click and check if the cat was found
                        if not self.board.dig_up(gx, gy):
                            
                            # blow up
                            for row in self.board.board_list:
                                
                                for tile in row:
                                    if tile.flagged and tile.type != "X":
                                        tile.revealed = True
                                        tile.flagged = False
                                        
                                        tile.image = tile_not_cookie
                                    
                                    elif tile.type == "X" and not tile.revealed:
                                        tile.revealed = True
                            
                            self.playing = False
                
                if event.button == 3:
                    # Right click to flag the tile
                    if not self.board.board_list[gx][gy].revealed:
                        self.board.board_list[gx][gy].flagged = not self.board.board_list[gx][gy].flagged
                
                if self.win_conditions():
                    self.win = True
                    self.playing = False
                    
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True

    """
    def reset_game(self):
        self.board_list = self.initialize_board()  # Reinitialize the board
        self.dug = []  # Clear the dug tiles
        self.total_mines = self.calculate_mines()  # Recalculate mines
        self.board_surface.fill((0, 0, 0))  # Clear the board surface
        self.draw(screen) # type: ignore
    """
    
    # Show the win or lose screen
    def da_end(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return        


game = DaGame()

while True:
    game.new()
    game.run()