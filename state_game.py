import pygame
from state import State
from player import Player

'''
Main game state. Might be the class where the whole game will run at.
'''
class StateGame(State):

    player = Player() 

    def __init__(self, screen, inputManager):
        State.__init__(self, screen, inputManager)
        inputManager.attach(self.player)
        
    def destroy(self): pass
    
    def update(self, dt):
        State.update(self, dt) 
        self.player.update(dt,self.screen)   
        
    def render(self):
        State.render(self) 
        #background
        self.screen.fill(pygame.Color(0,0,0))
        
        self.player.render(self.screen)