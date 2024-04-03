import pygame as pg
import random

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
PIPE_WIDTH = 70
GAP_SIZE = 140 # Gap size between top and bottom pipes
BOTTOM_PIPE_Y = 460  # Y position for the top edge of bottom pipes

class TopPipe(pg.sprite.Sprite):
    def __init__(self, x, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('images/pipe_up.png').convert_alpha(), (PIPE_WIDTH, height))
        self.rect = self.image.get_rect(topleft=(x, 0))
    
    def update(self):
        self.rect.x -= 2
        if self.rect.right < 0:
            self.rect.left = 600

class BottomPipe(pg.sprite.Sprite):
    def __init__(self, x, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('images/pipe_down.png').convert_alpha(), (PIPE_WIDTH, height))
        self.rect = self.image.get_rect(bottomleft =(x, BOTTOM_PIPE_Y))
    
    def update(self):
        self.rect.x -= 2
        if self.rect.right < 0:
            self.rect.left = 600

class PipePair:
    def __init__(self, x):
        top_height = random.randint(100, BOTTOM_PIPE_Y - GAP_SIZE - 90)  # Ensure there's enough room for the gap
        
        bottom_height = SCREEN_HEIGHT - (top_height + GAP_SIZE)  # Calculate bottom pipe height based on top pipe and gap

        self.top_pipe = TopPipe(x, top_height)
        self.bottom_pipe = BottomPipe(x, bottom_height)
        self.pipes = pg.sprite.Group(self.top_pipe, self.bottom_pipe)
        self.passed = False
    
    def update(self):
        self.pipes.update()

    def draw(self, screen):
        self.pipes.draw(screen)











































'''



import pygame as pg 
import random


class Pipe():

    def __init__(self):
        self.pipe_top = pg.image.load('images/pipe_up.png').convert_alpha()

        self.pipe_bottom= pg.image.load('images/pipe_down.png').convert_alpha()
        self.rects = self.create_pipes()
        


    def create_pipes(self):

        self.scale_y_top = [200, 260, 150, 240]
        self.position_x = [100, 250, 400, 550]
        self.image_list = [] 
        self.rect_list = [] 
        self.scale_y_bottom = [200, 140, 250, 150]
        self.image_list2 = []  
        self.rect_list2 = []
        #list of all rects:  
        self.combined_rects = []

        for num in range(0,4):
            # For top pipes
            image = pg.transform.scale(self.pipe_top, (70, self.scale_y_top[num]))
            rect = image.get_rect(topleft=(self.position_x[num], 0))
            self.image_list.append(image)
            self.rect_list.append(rect)
            self.combined_rects.append(rect)

            # For bottom pipes
            image2 = pg.transform.scale(self.pipe_bottom, (70, self.scale_y_bottom[num]))
            bottom_pos_y = 500 - self.scale_y_bottom[num] - (500 - 460)
            rect2 = image2.get_rect(bottomleft=(self.position_x[num], 460))
            self.image_list2.append(image2)
            self.rect_list2.append(rect2)
            self.combined_rects.append(rect2)

    
        
        self.pipe_pairs = list(zip(zip(self.image_list, self.rect_list), zip(self.image_list2, self.rect_list2)))
        return self.combined_rects
        



    def draw(self, screen):
        self.screen = screen
        for top_pipe, bottom_pipe in self.pipe_pairs:
            self.screen.blit(top_pipe[0], top_pipe[1])
            self.screen.blit(bottom_pipe[0], bottom_pipe[1])
    def reset(self):
        self.create_pipes()

    
    def update(self):
        off_screen_pipes_indices = []
        for index, ((_, top_rect), (_, bottom_rect)) in enumerate(self.pipe_pairs):
            top_rect.left -= 1  
            bottom_rect.left -= 1  

            if top_rect.right < 0 or bottom_rect.right < 0:
                off_screen_pipes_indices.append(index)

        if off_screen_pipes_indices:
            random_index = random.choice(off_screen_pipes_indices)
            selected_top_rect, selected_bottom_rect = self.pipe_pairs[random_index][0][1], self.pipe_pairs[random_index][1][1]

            selected_top_rect.left = 600
            selected_bottom_rect.left = 600
    


'''