import pygame as pg 

import sys
from bird import Bird
from pipe import PipePair




SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

POSITION_X = [100, 250, 400, 550]

class Game:
    def __init__(self):
        pg.init()
        size = SCREEN_WIDTH,  SCREEN_HEIGHT
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption('Flappy_Bird')
        self.clock = pg.time.Clock()
        self.font_t = pg.font.Font( None, 50)
        self.sky_image = pg.image.load('images/sky.JPG').convert_alpha()
        self.sky_image = pg.transform.scale(self.sky_image , (600,500))
        self.sky_rect = self.sky_image.get_rect(topleft = (0,0))
        self.ground_image = pg.image.load('images/ground.png').convert_alpha()
        self.ground_image = pg.transform.scale(self.ground_image , (600,40))
        self.g_rect = self.ground_image.get_rect(topleft = (0, 460))
        self.play_button = self.font_t.render('Play', False, (111,196,169))
        self.play_rect = self.play_button.get_rect(midtop = (300,400))
        self.play_button2 = self.font_t.render('Play again?', False, (111,196,169))
        self.play_rect2 = self.play_button2.get_rect(midtop = (300,400))
        self.bird_active = False
        self.bird = pg.sprite.GroupSingle()
        self.bird.add(Bird())
        self.pipes = [PipePair(x) for x in POSITION_X]
        self.game_active = False
        self.user_input = 0
        
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.bird_active = True
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()
                if self.play_rect.collidepoint(mouse_pos_x, mouse_pos_y):
                    self.activate()
                if self.play_rect2.collidepoint(mouse_pos_x, mouse_pos_y):
                    self.activate()
               
        


    def launch_screen(self):
        title = self.font_t.render('Flappy Bird', False, (111,196,169))
        title_rect = title.get_rect(midtop = (300,100))
        self.screen.blit(title,title_rect)

        self.screen.blit(self.play_button,self.play_rect)
        pg.display.flip()

    def game_over(self):
        self.screen.fill('Black')
        game_over = self.font_t.render('Game Over', False, (111,196,169))
        over_rect = game_over.get_rect(midtop = (300,200))
        self.screen.blit(game_over,over_rect)
        self.screen.blit(self.play_button2,self.play_rect2)
        self.handle_events()
        pg.display.flip()


    def activate(self): 
        self.game_active = True


        

    def play(self):

        self.launch_screen()



        while True:       
            self.handle_events()
            user_input = pg.key.get_pressed()
            if self.game_active: 
                self.screen.blit(self.sky_image,self.sky_rect)
                self.screen.blit(self.ground_image, self.g_rect)
                self.bird.draw(self.screen)
                self.handle_events()
                for pipe_pair in self.pipes: 
                    pipe_pair.draw(self.screen)
                
                if self.bird_active:
                    self.bird.update(user_input) 
                    for pipe_pair in self.pipes:
                        pipe_pair.update()
                        pipe_pair.draw(self.screen)
                
              
                    for pipe_pair in self.pipes:
                        if pg.sprite.spritecollideany(self.bird.sprite, pipe_pair.pipes):
                            self.hit_sound = pg.mixer.Sound("images/hit_sound.mp3")
                            self.hit_sound.play()
                            self.game_active = False
                            break

            elif self.bird_active:
                 self.game_over()
                 self.bird_active = False
                 self.pipes.clear()  # Remove all pipe pairs
                 self.pipes = [PipePair(x) for x in POSITION_X]
                 self.bird.sprite.reset()
        
                
  
    
              # self.Scores_button.update() 
            pg.display.flip()
            self.clock.tick(60)


  

def main():
    g = Game()
    g.play()

if __name__ == '__main__':
    main()