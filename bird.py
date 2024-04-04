import pygame as pg 





class Bird(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.curr_sprite = 0
        self.sprites.append(pg.image.load('images/bird_down.png'))
        self.sprites.append(pg.image.load('images/bird_mid.png'))
        self.sprites.append(pg.image.load('images/bird_up.png'))
        self.image = self.sprites[self.curr_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (50, 230)
        self.velocity = 0
        self.flap = False
        self.alive = True
        self.flap_sound = pg.mixer.Sound("images/flap_sound.mp3")
    
        self.hit = False
        self.animated = False
        
    def flap_animation(self):
        if self.animated == True:
            self.curr_sprite += .25
            if int(self.curr_sprite) >= len(self.sprites):
                self.curr_sprite = 0
                self.animated = False
            self.image = self.sprites[int(self.curr_sprite)]

    def reset(self):
        self.velocity = 0
        self.rect.center = (50,230)
        self.flap = False

    def update(self, user_input):
        self.flap_animation()
        self.velocity += 0.5
        #adopted code logic for bird flap from online tutorial
        if self.velocity > 5:
            self.velocity = 5
        if self.rect.y < 435:
            self.rect.y += int(self.velocity)
        if self.velocity == 0:
            self.flap = False
        if user_input[pg.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.animated = True
            self.flap_sound.play()
            self.flap = True
            self.velocity = -5

    


        
        
