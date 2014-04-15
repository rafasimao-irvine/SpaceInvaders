'''
Created on 14/04/2014

@author: rafaelsimao
'''
import pygame
from invader import Invader

class InvadersManager():
    
    'Inits InvadersManager'
    def __init__(self):
        self.invaders_list = list()
        self.projectile_list = list()
        self.number_of_invaders_alive = 0;

        self.spawn_time = 60
        self._create_row_of_invaders()

    def _create_row_of_invaders(self):
        for i in range(1, 8):
            self.invaders_list.append(Invader(self.projectile_list,100*i,30,100))

    def update(self, dt):
        self.update_projectiles(dt)
        self.update_invaders(dt)
        
        if self.spawn_time < 0:
            self.spawn_time = 60
            self._create_row_of_invaders()
        else:
            self.spawn_time -= 0.01*dt
                            
    def update_projectiles(self, dt):
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                shot.move()
                
    def update_invaders(self, dt):
        if self.invaders_list.__len__() > 0: 
            for invader in self.invaders_list:
                invader.update(dt)
        

    def render(self, screen):
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                shot.render(pygame.Color(255, 0, 0), screen)

        if self.invaders_list.__len__() > 0: 
            for invader in self.invaders_list:
                invader.render(screen)
