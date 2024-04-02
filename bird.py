import pygame as pg 
#from pipe import Pipe




class Bird(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/bird_up.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(center = (50,250))
        #self.screen = game.screen
        self.velocity = 0
        self.flap = False
        self.alive = True
        self.flap_sound = pg.mixer.Sound("images/flap_sound.mp3")
        #self.pipes = Pipe()
        #self.pipes = self.pipes.rects
        self.hit = False
        

    def animate(self):
        BIRD_IMAGE = pg.image.load('images/bird_down.png').convert_alpha()
        BIRD_IMAGE = pg.transform.scale(self.image, (20,20))
        bird_rect2 = BIRD_IMAGE.get_rect(center = (50,230))
        self.image = BIRD_IMAGE
        self.rect = bird_rect2

    def reset(self):
        self.velocity = 0
        self.rect.center = (50,230)
        self.flap = False

    def update(self, user_input):
        #self.check_collisions()
        self.velocity += 0.5
        if self.velocity > 5:
            self.velocity = 5
        if self.rect.y < 460:
            self.rect.y += int(self.velocity)
        if self.velocity == 0:
            self.flap = False
        if user_input[pg.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap_sound.play()
            self.flap = True
            self.velocity = -5

    


        
        
