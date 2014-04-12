import pygame
from input_listener import InputListener
from projectile import Projectile

class Player(InputListener):
    
    'Inits the player attributes'
    def __init__(self): 
        self.speed = 0.25
        
        self.position_x = 425.0
        self.position_y = 500.0
    
        self.projectile_list = list()
        self.fire_delay = 15
        
        self.move_right = self.move_left = self.fire_shot = False
    
    'Makes the player actions move and fire'
    def update(self, dt):
        self.move(dt) 
        self.shoot()
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                shot.move()
        if self.fire_delay < 15:
            self.fire_delay += 1
            
    'Moves the player, based in the current pressed buttons'
    def move(self, dt):
        if self.move_left and self.position_x > 0:
            self.position_x -= self.speed*dt
        elif self.move_right and self.position_x < 900:
            self.position_x += self.speed*dt
     
    'Allows the player to fire projectiles if correct button is pressed'
    def shoot(self):
        if self.fire_shot and self.fire_delay == 15:
            projectile = Projectile(self.position_x+22.5, self.position_y, -2.5)
            self.projectile_list.append(projectile)
            print(self.projectile_list.__len__())
            self.fire_delay = 0
    
    'Draws the player and projectiles on the screen'
    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color(255,255,255), (self.position_x,self.position_y,50,50))
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                shot.render(screen)
            

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
        #Starts firing projectile
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.fire_shot = True
        #Finishes firing projectile
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.fire_shot = False
