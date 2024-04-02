import pygame as pg 
import random

class Pipe():

    def __init__(self, game):
        self.screen = game.screen
        self.pipe_top = pg.image.load('images/pipe_up.png').convert_alpha()

        self.pipe_bottom= pg.image.load('images/pipe_down.png').convert_alpha()
        self.create_pipes()


    def create_pipes(self):

        self.scale_y_top = [200, 260, 150, 240]
        self.position_x = [100, 250, 400, 550]
        self.image_list = []  # Initialize as an empty list
        self.rect_list = []  # Initialize as an empty list
        self.scale_y_bottom = [200, 140, 250, 150]
        self.image_list2 = []  # Initialize as an empty list
        self.rect_list2 = []  # Initialize as an empty list

        for num in range(0,4):
            # For top pipes
            image = pg.transform.scale(self.pipe_top, (70, self.scale_y_top[num]))
            rect = image.get_rect(topleft=(self.position_x[num], 0))
            self.image_list.append(image)
            self.rect_list.append(rect)

            # For bottom pipes
            image2 = pg.transform.scale(self.pipe_bottom, (70, self.scale_y_bottom[num]))
            bottom_pos_y = 500 - self.scale_y_bottom[num] - (500 - 460)
            rect2 = image2.get_rect(bottomleft=(self.position_x[num], 460))
            self.image_list2.append(image2)
            self.rect_list2.append(rect2)
        
        self.pipe_pairs = list(zip(zip(self.image_list, self.rect_list), zip(self.image_list2, self.rect_list2)))



    def draw(self):
        for top_pipe, bottom_pipe in self.pipe_pairs:
            self.screen.blit(top_pipe[0], top_pipe[1])
            self.screen.blit(bottom_pipe[0], bottom_pipe[1])
    def reset(self):
        self.create_pipes()

    
    def update(self):
        off_screen_pipes_indices = []

        # Check each pipe pair to see if it's off-screen
        for index, ((_, top_rect), (_, bottom_rect)) in enumerate(self.pipe_pairs):
            top_rect.left -= 1  # Move the top pipe left
            bottom_rect.left -= 1  # Move the bottom pipe left

            # Collect indices of off-screen pipes
            if top_rect.right < 0 or bottom_rect.right < 0:
                off_screen_pipes_indices.append(index)

        # If there are any off-screen pipes, choose one at random to move to x = 600
        if off_screen_pipes_indices:
            # Choose a random index from those that went off-screen
            random_index = random.choice(off_screen_pipes_indices)
            selected_top_rect, selected_bottom_rect = self.pipe_pairs[random_index][0][1], self.pipe_pairs[random_index][1][1]

            # Move the randomly selected pipe pair to x = 600
            selected_top_rect.left = 600
            selected_bottom_rect.left = 600
    


