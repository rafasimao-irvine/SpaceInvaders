import pygame
from state import State

class StateGame(State):

    def __init__(self, screen, inputManager):
        State.__init__(self, screen, inputManager)
        
    def destroy(self): pass
    
    def update(self):
        State.update(self)    
        
    def render(self):
        State.render(self) 
        #background
        self.screen.fill(pygame.Color(0,0,0))