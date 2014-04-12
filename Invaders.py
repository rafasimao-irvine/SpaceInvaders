'''
Created on Apr 9, 2014

@author: Brian Paff
94135229
'''


import pygame
from projectile import Projectile


maxInvaders = 5
x = 0
y = 0
position = [x,y]
mvmtSpeed = 1
clock = pygame.time.Clock()
lastShot = clock
movingRight = True

class Invaders():
    
    '''
    Invader is going to spawn a new enemy on the screen. It takes how many enemies are spawned,
    then divides that number by the max number of invaders we want on a line  and takes the floor 
    of it. This will give us the amount of lines down we should drop that spawned invader.
    We then find out how many invaders are currently on the current line we're working with by 
    taking that floor we just calculated, multiplying it by the max amount of invaders, and
    then subtracting that product from the amount of invaders that have been spawned. We then move
    this invader over the appropriate amount of spaces.
    '''
    def __init__(self, amountOfInvadersSpawned):
        #check if there are destroyed invaders you can replace
        temp = amountOfInvadersSpawned/maxInvaders
        self.y = y+temp
        temp2 = temp#times maxInvaders
        #amountOfInvadersOnThisLine
        aOIOTL = amountOfInvadersSpawned-temp2
        self.x= 2 *aOIOTL
        self.myBox = pygame.Rect(x, y, 10, 10)
        
        self.projectile_list = list()
        self.fire_delay = 15
    
        '''
    Move changes the position of the invader by taking its current position, and adds the current
    movement speed to that old position value. If it hits the side of the game board or it will
    move past it during this method call, it should drop down one line and reverse direction.
    '''
    def move(self):
        ''' if self.position == #hits either side of the game Board
            self.y=y+1
            self.position = [x, y]
            self.reverseDirection(movingRight)'''
                #else:
        if movingRight == True:
            position = [self.x+mvmtSpeed, y]
            self.x = self.x+mvmtSpeed
        else:
            position = [x-mvmtSpeed, y]
            x = self.x - self.mvmtSpeed

    
    '''
    speedUp() is called by the manager class, and will make the invaders move faster when one has 
    been killed
    '''
    def speedUp(self):
        a= self.mvmentSpeed + 1
        self.mvmtSpeed = a
    
    '''
    shoot checks to see if a given interval has passed since the last time this invader fired,
    if it has, then it should make a projectile object
    '''
    def shoot(self, clockTime):
        if self.fire_delay == 15:
            #create a new projectile object moving downward
            self.fire_delay = 0
            
            projectile = Projectile(self.x+12.25, self.y+15, 2.5)
            self.projectile_list.append(projectile)
    
    '''
    update() is called by the manager class individually for each invader, and will handle calling 
    that invader's move() and shoot()
    '''
    def update(self, clockTimeStamp):
        self.move()
        self.shoot(clockTimeStamp)
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                shot.move()
        if self.fire_delay < 15:
            self.fire_delay+=1
    
    def reverseDirection(self, currentDir):
        if self.currentDir == True:
            self.currentDirection = False
        else:
            self.currentDirection = True
                            
    def render(self, screen):
        if self.projectile_list.__len__() > 0: 
            for shot in self.projectile_list:
                color = pygame.Color(255, 0, 0)
                shot.render(color, screen)
        pygame.draw.rect(screen, pygame.Color(255,255,255), (self.x,y,25,25))

    #def removeFromGameBoard():
    '''
    how should we implement this? just make them transparent and remove them from the list of
    invaders?
    '''
    #def isHit():
    '''
    #if hit by a projectile,
        return True
    else:
        return False
        '''
    