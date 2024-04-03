import pygame as pg 

import sys
from bird import Bird
from pipe import PipePair




SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

POSITION_X = [150, 300, 450, 600]

class Game:
    def __init__(self):
        pg.init()
        size = SCREEN_WIDTH,  SCREEN_HEIGHT
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption('Flappy_Bird')
        self.clock = pg.time.Clock()
        self.font = pg.font.Font( None, 50)
        self.start_ = self.font.render('Start', False, (100,196,20))
        self.start_rect = self.start_.get_rect(midtop = (300,400))
        self.restart_ = self.font.render('Restart', False, (100,196,20))
        self.restart_rect = self.restart_.get_rect(midtop = (300,400))
        self.sky_image = pg.image.load('images/sky.JPG').convert_alpha()
        self.sky_image = pg.transform.scale(self.sky_image , (600,500))
        self.sky_rect = self.sky_image.get_rect(topleft = (0,0))
        self.ground_image = pg.image.load('images/ground.png').convert_alpha()
        self.ground_image = pg.transform.scale(self.ground_image , (600,40))
        self.hit_sound = pg.mixer.Sound("images/hit_sound.mp3")
        self.bird_active = False
        self.bird = pg.sprite.GroupSingle()
        self.bird.add(Bird())
        self.pipes = [PipePair(x) for x in POSITION_X]
        self.game_active = False
        self.user_input = 0
        self.score = 0


    def launch_screen(self):
        title = self.font.render('Flappy Bird', False, (100,196,20))
        title_rect = title.get_rect(midtop = (300,100))
        self.screen.blit(title,title_rect)
        self.screen.blit(self.start_,self.start_rect)
        pg.display.flip()

    def game_over(self):
        game_over = self.font.render('Game Over', False, (100,196,20))
        over_rect = game_over.get_rect(midtop = (300,200))
        show_score = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.screen.blit(show_score, (230,300))
        self.screen.blit(game_over,over_rect)
        self.screen.blit(self.restart_,self.restart_rect)
        self.handle_events()
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.bird_active = True
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()
                if self.start_rect.collidepoint(mouse_pos_x, mouse_pos_y):
                    self.game_active = True
                elif self.restart_rect.collidepoint(mouse_pos_x, mouse_pos_y):
                    self.game_active = True


    def update_score(self):
        for pipe_pair in self.pipes:
            if self.bird.sprite.rect.left > pipe_pair.top_pipe.rect.left  and self.bird.sprite.rect.right  < pipe_pair.top_pipe.rect.right and not pipe_pair.passed:
                pipe_pair.passed = True
            if pipe_pair.passed:
                if self.bird.sprite.rect.left >  pipe_pair.top_pipe.rect.right:
                    self.score += 1
                    pipe_pair.passed = False

    
                


    def draw_score(self):
        score_surface = self.font.render(f'{self.score}', True, (0, 0, 0))
        self.screen.blit(score_surface, (20, 20))


    def check_collison (self):
        if self.bird.sprite.rect.y == 434:
            self.hit_sound.play()
            self.game_active = False

        for pipe_pair in self.pipes:
            if pg.sprite.spritecollideany(self.bird.sprite, pipe_pair.pipes):
                self.hit_sound.play()
                self.game_active = False
                break


    def reset_score(self):
        self.score = 0
        for pipe_pair in self.pipes:
            pipe_pair.passed = False

    def play(self):
        self.launch_screen()
        while True:      
            self.handle_events()
            user_input = pg.key.get_pressed()
            pg.display.flip()
            self.clock.tick(32) 
            #if game isnt over yet
            if self.game_active: 
                self.screen.blit(self.sky_image,self.sky_rect)
                self.screen.blit(self.ground_image, (0,460))
                self.bird.draw(self.screen) 
                for pipe_pair in self.pipes:
                    pipe_pair.draw(self.screen)
                    self.draw_score()
                #when the bird starts moving
                if self.bird_active:
                    self.check_collison() 
                    self.bird.update(user_input) 
                    for pipe_pair in self.pipes:
                        pipe_pair.update()
                        pipe_pair.draw(self.screen)
                self.update_score()
            #bird has already been active but not game is inactive
            elif self.bird_active:
                 self.game_over()
                 self.reset_score()
                 self.bird_active = False
                 self.pipes.clear() 
                 self.pipes = [PipePair(x) for x in POSITION_X]
                 self.bird.sprite.reset() 


  

def main():
    g = Game()
    g.play()

if __name__ == '__main__':
    main()