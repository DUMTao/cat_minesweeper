# Imports
import pygame
from settings import *
from colors import *

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


game = DaGame()

while True:
    game.new()
    game.run()