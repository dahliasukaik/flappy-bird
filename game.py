import pygame as pg 
from sys import exit
from random import randint, choice
'''
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_image1 = pg.image.load('images/bird_up.png').convert_alpha()
        bird_image2 = pg.image.load('images/bird_down.png').convert_alpha()
        self.bird_fly = [bird_image1,bird_image2]
        self.bird_index = 0

        self.image = self.bird_fly[self.bird_index]
		self.rect = self.image.get_rect(midbottom = (80,100))
        self.gravity = 0

'''


pg.init()

screen_width = 600
screen_height = 500
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Flappy_Bird')
clock = pg.time.Clock()
game_active = True


sky_image = pg.image.load('images/sky.JPG').convert_alpha()
sky_image = pg.transform.scale(sky_image , (600,500))
ground_image = pg.image.load('images/ground.png').convert_alpha()
ground_image = pg.transform.scale(ground_image , (600,40))
bird_image1 = pg.image.load('images/bird_up.png').convert_alpha()
#bird_image2 = pg.image.load('images/bird_down.png').convert_alpha()
bird_image = pg.transform.scale(bird_image1 , (20,20))
bird_rect = bird_image.get_rect(center = (50,230))



pipe_top = pg.image.load('images/pipe_up.png').convert_alpha()

pipe_top1 = pg.transform.scale(pipe_top, (70,200))
pipe1_rect1 = pipe_top1.get_rect(topleft = (150,0))

pipe_top2 = pg.transform.scale(pipe_top, (70,250))
pipe1_rect2= pipe_top2.get_rect(topleft = (300,0))

pipe_top3 = pg.transform.scale(pipe_top, (70,150))
pipe1_rect3 = pipe_top3.get_rect(topleft = (450,0))


pipe_top4 = pg.transform.scale(pipe_top, (70,230))
pipe1_rect4 = pipe_top4.get_rect(topleft = (600,0))


pipe_bottom= pg.image.load('images/pipe_down.png').convert_alpha()

pipe_bottom1 = pg.transform.scale(pipe_bottom, (70,200))
pipe2_rect1 = pipe_bottom1.get_rect(bottomleft = (150,460))

pipe_bottom2 = pg.transform.scale(pipe_bottom, (70,150))
pipe2_rect2 = pipe_bottom2.get_rect(bottomleft= (300,460))

pipe_bottom3 = pg.transform.scale(pipe_bottom, (70, 250))
pipe2_rect3 = pipe_bottom3.get_rect(bottomleft = (450,460))

pipe_bottom4 = pg.transform.scale(pipe_bottom, (70,170))
pipe2_rect4 = pipe_bottom4.get_rect(bottomleft = (600,460))


bird_gravity = 0





flag = False
		
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
             pg.quit()
             exit()
        if game_active:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and bird_rect.top >= 10:
                    bird_gravity -= 5
                    
            if event.type == pg.KEYUP:
                flag = True
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_active = True
                bird_rect.x = 50
 
                
      
    if game_active:
        # if event.type == pg.KEYDOWN:
            
        screen.blit(sky_image,(0,0))
        screen.blit(ground_image,(0,460))
        screen.blit(bird_image,bird_rect)
        if (flag):
            bird_gravity += .5
            bird_rect.y += bird_gravity
        
        

        
        pipe1_rect1.left -= 1
        pipe1_rect2.left -= 1
        pipe1_rect3.left -= 1
        pipe1_rect4.left -= 1

        if(pipe1_rect1.right < 0): 
            pipe1_rect1.left = 550
        if(pipe1_rect2.right < 0): 
            pipe1_rect2.left = 550
        if(pipe1_rect3.right < 0): 
            pipe1_rect3.left = 550
        if(pipe1_rect4.right < 0): 
            pipe1_rect4.left = 550

        screen.blit(pipe_top1,pipe1_rect1)
        screen.blit(pipe_top2,pipe1_rect2)
        screen.blit(pipe_top3,pipe1_rect3)
        screen.blit(pipe_top4,pipe1_rect4)

        pipe2_rect1.left -= 1
        pipe2_rect2.left -= 1
        pipe2_rect3.left -= 1
        pipe2_rect4.left -= 1

        

        

        

        if(pipe2_rect1.right < 0): 
            pipe2_rect1.left = 550
        if(pipe2_rect2.right < 0): 
            pipe2_rect2.left = 550
        if(pipe2_rect3.right < 0): 
            pipe2_rect3.left = 550
        if(pipe2_rect4.right < 0): 
            pipe2_rect4.left = 550
        screen.blit(pipe_bottom1,pipe2_rect1)
        screen.blit(pipe_bottom2,pipe2_rect2)
        screen.blit(pipe_bottom3,pipe2_rect3)
        screen.blit(pipe_bottom4,pipe2_rect4)

        if ( (bird_rect.bottom >= 460) or bird_rect.colliderect(pipe1_rect1) or bird_rect.colliderect(pipe1_rect1)): 
            game_active = False

    else:
        screen.fill('yellow')

    
  




    pg.display.update()
    clock.tick(60)