'''
Created on Apr 9, 2014

@author: Brian Paff
94135229
'''


import pygame

maxInvaders = 5
x = 0
y = 0
position = [x,y]
mvmtSpeed = 1
clock = pygame.time.Clock()
lastShot = clock
currentDirection = "right"
myBox #invader's model


'''
Invader is going to spawn a new enemy on the screen. It takes how many enemies are spawned,
then divides that number by the max number of invaders we want on a line  and takes the floor 
of it. This will give us the amount of lines down we should drop that spawned invader.
We then find out how many invaders are currently on the current line we're working with by 
taking that floor we just calculated, multiplying it by the max amount of invaders, and
then subtracting that product from the amount of invaders that have been spawned. We then move
this invader over the appropriate amount of spaces.
'''
def Invader(amountOfInvadersSpawned):
    #check if there are destroyed invaders you can replace
    temp = #floor of amountOfInvadersCurrentlySpawned/maxInvaders
    self.y = y+temp
    temp2 = temp#times maxInvaders
    #amountOfInvadersOnThisLine
    aOIOTL = amountOfInvadersSpawned-temp2
    self.x= 2 #times aOIOTL
    self.myBox = pygame.Rect(x, y, 10, 10)
    
'''
Move changes the position of the invader by taking its current position, and adds the current
movement speed to that old position value. If it hits the side of the game board or it will
move past it during this method call, it should drop down one line and reverse direction.
'''
def move():
    if self.position == #hits either side of the game Board
        self.y=y+1
        self.position = [x, y]
        self.reverseDirection(currentDirection)
    else:
        if self.currentDirection == "right":
            self.position = [x+mvmtSpeed, y]
            self.x = x+mvmtSpeed
        else:
            self.position = [x-mvmtSpeed, y]
            self.x = self.x - self.mvmtSpeed
    
'''
speedUp() is called by the manager class, and will make the invaders move faster when one has 
been killed
'''
def speedUp():
    self.mvmtSpeed = self.mvmentSpeed++
    
'''
shoot checks to see if a given interval has passed since the last time this invader fired,
if it has, then it should make a projectile object
'''
def shoot(self, clockTime):
    if clockTime >= self.lastShot+3
        #create a new projectile object moving downward
        self.lastShot= clockTime 
    
'''
update() is called by the manager class individually for each invader, and will handle calling 
that invader's move() and shoot()
'''
def update(self, clockTimeStamp):
    self.move()
    self.shoot(clockTimeStamp)
    #render?
    
def reverseDirection(self, currentDir):
    if self.currentDir == "right":
        self.currentDirection = "left"
    else:
        self.currentDirection = "right"

def removeFromGameBoard():
    '''
    how should we implement this? just make them transparent and remove them from the list of
    invaders?
    '''
def isHit():
    #if hit by a projectile,
        return True
    else:
        return False
    