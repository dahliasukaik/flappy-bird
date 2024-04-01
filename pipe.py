import pygame as pg 


class Pipe():

    def __init__(self, game):
        self.screen = game.screen
        self.pipe_top = pg.image.load('images/pipe_up.png').convert_alpha()

        self.pipe_bottom= pg.image.load('images/pipe_down.png').convert_alpha()
        self.create_pipes()

    def create_pipes(self):
        self.scale_y_top = [200, 250, 150, 230]
        self.position_x = [100, 250, 400, 550]
        self.image_list = []  # Initialize as an empty list
        self.rect_list = []  # Initialize as an empty list
        self.scale_y_bottom = [200, 150, 250, 170]
        self.image_list2 = []  # Initialize as an empty list
        self.rect_list2 = []  # Initialize as an empty list

        for num in range(4):
            # Append scaled top pipe images and corresponding rects
            image = pg.transform.scale(self.pipe_top, (70, self.scale_y_top[num]))
            rect = image.get_rect(topleft=(self.position_x[num], 0))
            self.image_list.append(image)
            self.rect_list.append(rect)

            # Append scaled bottom pipe images and corresponding rects
            image2 = pg.transform.scale(self.pipe_bottom, (70, self.scale_y_bottom[num]))
            rect2 = image2.get_rect(bottomleft=(self.position_x[num], 460))
            self.image_list2.append(image2)
            self.rect_list2.append(rect2)

    def reset(self):
        self.create_pipes()
    def draw(self):
        for num in range(4):
            self.screen.blit(self.image_list[num],self.rect_list[num])
            self.screen.blit(self.image_list2[num],self.rect_list2[num])
    def update(self):
        for num in range(4):
            self.rect_list[num].left -= 1
            self.rect_list2[num].left -= 1
            if self.rect_list[num].right < 0 or self.rect_list2[num].right < 0:
                # Reset position based on the screen width
                self.rect_list[num].left = 600
                self.rect_list2[num].left = 600
        self.draw()

