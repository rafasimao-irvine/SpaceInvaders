import pygame
from input_listener import InputListener

class Player(InputListener):
    
    'Inits the player attributes'
    def __init__(self): 
        self.speed = 0.5
        
        self.position_x = 100.0
        self.position_y = 500.0
    
        self.move_right = self.move_left = False
    
    'Makes the player actions move and fire'
    def update(self, dt):
        self.move(dt)
        
    'Moves the player, based in the current pressed buttons'
    def move(self, dt):
        if self.move_left:
            self.position_x -= self.speed*dt
        elif self.move_right:
            self.position_x += self.speed*dt
        
    'Draws the player in the screen'
    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color(255,255,255), (self.position_x,self.position_y,50,50))

    'Receives inputs and treats them if they corresponds to moving or firing'
    def receiveInput(self, event):
        #Starts moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
            elif event.key == pygame.K_d:
                self.move_right = True
        #Finishes moving
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_left = False
            elif event.key == pygame.K_d:
                self.move_right = False
