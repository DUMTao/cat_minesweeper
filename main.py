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
        pass
    
    
    # Function that sets the framerate while the program runs
    def run(self):
        self.playing = True
        
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.playing = False
    
    # Setting the appareance of the window
    def draw(self):
        self.screen.fill(bg_color)
        
        pygame.display.flip()
        
    