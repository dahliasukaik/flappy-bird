import pygame as pg 

JUMP = -4

bird_velocity_y = -9
Max_Vel_Y = 10
Min_Vel_Y = -8
GRAVITY = .17
  

class Bird():
    def __init__(self, game):

        self.image = pg.image.load('images/bird_up.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(center = (30,250))
        self.screen = game.screen
        self.velocity = 0
        self.is_jumping = False

        

    def jump(self):
            self.velocity = JUMP
            self.is_jumping = True
            self.animate()

    def fall(self):
            self.velocity += GRAVITY
            self.rect.y += self.velocity

    def animate(self):
        BIRD_IMAGE = pg.image.load('images/bird_down.png').convert_alpha()
        BIRD_IMAGE = pg.transform.scale(self.image, (20,20))
        bird_rect2 = BIRD_IMAGE.get_rect(center = (50,230))
        self.image = BIRD_IMAGE
        self.rect = bird_rect2
    def reset(self):
        self.velocity = 0
        self.rect.y = 250
        self.is_jumping = False
    def draw(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.draw()
        if self.is_jumping == True: 
            self.fall()
        
