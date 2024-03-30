import pygame as pg 
from sys import exit
from random import randint, choice


pg.init()

screen_width = 800
screen_height = 400
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Flappy_Bird')
clock = pg.time.Clock()


sky_image = pg.image.load('images/sky.JPG').convert_alpha()
sky_image = pg.transform.scale(sky_image , (800,300))
ground_image = pg.image.load('images/ground.png').convert_alpha()
ground_image = pg.transform.scale(ground_image , (800,131))

#test_font = pygame.font.Font(None 50)






		
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
             pg.quit()
             exit()
    screen.blit(sky_image,(0,0))
    screen.blit(ground_image,(0,300))


    pg.display.update()
    clock.tick(60)