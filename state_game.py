import pygame
from state import State
from player import Player
from invaders_manager import InvadersManager
#from Invaders import Invaders

'''
Main game state. Might be the class where the whole game will run at.
'''
class StateGame(State):

    player = Player() 
    #invader = Invaders(0)
    invader_manager = InvadersManager()

    def __init__(self, screen, inputManager):
        State.__init__(self, screen, inputManager)
        inputManager.attach(self.player)
        
        self.board_bounds = pygame.Rect(0,0,950,600)
        
        self.fontObj = pygame.font.Font('freesansbold.ttf', 22)
        
    def destroy(self): pass
    
    
    
    '''Update'''
    def update(self, dt):
        State.update(self, dt) 

        #Updates the game objects
        self.player.update(dt)   
        #self.invader.update(dt)
        self.invader_manager.update(dt)

        #treats projectiles hits        
        self._treat_invader_projectiles()
        self._treat_player_projectiles()
        
    'Make invaders projectiles collisions and perform the consequences'
    def _treat_invader_projectiles(self):
        if self.invader_manager.projectile_list.__len__() > 0: 
            #Goes through all the invaders projectiles
            for shot in self.invader_manager.projectile_list:
                #If it is out of the board game box, it is removed
                self._remove_if_out_of_board(self.invader_manager.projectile_list, shot)
                #If it collides with the player, the player receives the damage and the projectile is removed
                if shot.is_colliding_with(self.player):
                    self.player.receive_hit()
                    self.invader_manager.projectile_list.remove(shot)

    'Make players projectiles collisions and perform the consequences'
    def _treat_player_projectiles(self):
        if self.player.projectile_list.__len__() > 0: 
            #Goes through all the invaders projectiles
            for shot in self.player.projectile_list:
                #If it is out of the board game box, it is removed
                self._remove_if_out_of_board(self.player.projectile_list, shot)
                
                for invader in self.invader_manager.invaders_list:
                    if shot.is_colliding_with(invader):
                        self.player.projectile_list.remove(shot)
                        self.invader_manager.invaders_list.remove(invader)
                        
                        
                    
    'Removes a projectile from a projectile list if it is out of the board bounds'
    def _remove_if_out_of_board(self, projectile_list, projectile):
        #If it is out of the board game box, it is removed
        if not self.board_bounds.colliderect(projectile.get_collision_box()):
            projectile_list.remove(projectile)
   

    
    '''Render'''
    def render(self):
        State.render(self) 
        #background
        self.screen.fill(pygame.Color(0,0,0))
        
        self.player.render(self.screen)
        #self.invader.render(self.screen)
        self.invader_manager.render(self.screen)
        
        self.draw_player_life()
       
    'Draws the main player life' 
    def draw_player_life(self):
        msgSurfaceObject = self.fontObj.render("Life "+str(self.player.life), False, pygame.Color(205,255,205))
        msgRectObject = msgSurfaceObject.get_rect()
        msgRectObject.topleft = (25, 25)

        self.screen.blit(msgSurfaceObject, msgRectObject)
