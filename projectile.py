'''
Created on Apr 9, 2014

@author: ryanp
'''
import pygame


class Projectile:

    'Inits the Projectile attributes'
    def __init__(self, xpos, ypos, speed):
        self.x = xpos
        self.y = ypos
        self.speed = speed
        self.dt = 5
    
    'Moves the Projectile'
    def move(self):
        self.y += self.speed*self.dt

    'Draws the Projectile in the screen'
    def render(self, color, screen):
        pygame.draw.rect(screen, color, (self.x, self.y, 5, 30)) 
