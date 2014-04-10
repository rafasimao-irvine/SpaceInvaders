'''
Created on Apr 9, 2014

@author: ryanp
'''
import pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP



class Projectile:

    def __init__(self, xpos, ypos, dx, dy):
        self.x = xpos
        self.y = ypos
        self.dx = dx
        self.dy = dy
        self.shot = pygame.Rect(self.x, self.y, 5, 30)
    
    def update(self):
        self.shot.move_ip(self.dx, self.dy)
    
    def render(self):
        pygame.draw.rect(screen, (0, 191, 255), self.shot) 



#Test Projectile
pygame.init()
fpsClock = pygame.time.Clock()

##Screen
width, height = 950, 600
size = width, height
screen  = pygame.display.set_mode(size)

projectile = Projectile(width/2, height, 0, -5)
    
while True:
    
    #fpsClock.tick(50)  # frames per second
    
    
    for event in pygame.event.get():  # inputs
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            key = event.key
            if key == K_ESCAPE:
                exit()
            #elif key == K_UP:
                
            
    screen.fill((0,0,0))
    projectile.update()
    projectile.render() 
    
    pygame.display.update()
    