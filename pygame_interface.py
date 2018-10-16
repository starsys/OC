# -*- coding: utf8 -*-

import pygame
from pygame.locals import *
import os

class Pygame:

    BLOCK_PX_SIZE = 30

    def __init__(self, maze_dico):
        self.maze_dico = maze_dico
        # maze_dico in pixel size and x/y coordinates inversion for graph usage
        for key, value in list(self.maze_dico.items()):
            self.maze_dico[((key[1] * Pygame.BLOCK_PX_SIZE), (key[0] * Pygame.BLOCK_PX_SIZE))] = value
            # key (0, 0) is the single common key between original and updated dico. Should not be removed
            if key != ((0, 0)):
                del self.maze_dico[key]

    def get_max_line(self):
        return max([key[0] for key in self.maze_dico.keys()])

    def get_max_row(self):
        return max([key[1] for key in self.maze_dico.keys()])


    def graphic_maze(self):

        x_resolution = (self.get_max_row() + Pygame.BLOCK_PX_SIZE)
        y_resolution = (self.get_max_line() + Pygame.BLOCK_PX_SIZE)
        # self.maze_dico[(0, 0)] = "W"
        # print(self.maze_dico[(0, 0)])



        pygame.init()

        # Pygame window opening
        fenetre = pygame.display.set_mode((y_resolution, x_resolution))

        # backgroung load
        fond = pygame.image.load(os.path.dirname(__file__) + "/" + "images" + "/" + "background.jpg").convert()

        # wall block load
        wall = pygame.image.load(os.path.dirname(__file__) + "/" + "images" + "/" + "wall.png").convert_alpha()

        # charac import
        macgyver = pygame.image.load(os.path.dirname(__file__) + "/" + "images" + "/" + "macgyver.png").convert_alpha()
        # define graphical init position of character
        position_macgyver = macgyver.get_rect(topleft=[key for key, value in self.maze_dico.items() if value == "S"][0])

        # Graph loop
        continuer = 1

        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        position_macgyver = position_macgyver.move(-Pygame.BLOCK_PX_SIZE, 0)
                    if event.key == K_RIGHT:
                        position_macgyver = position_macgyver.move(Pygame.BLOCK_PX_SIZE, 0)
                    if event.key == K_UP:
                        position_macgyver = position_macgyver.move(0, -Pygame.BLOCK_PX_SIZE)
                    if event.key == K_DOWN:
                        position_macgyver = position_macgyver.move(0, Pygame.BLOCK_PX_SIZE)
             #Re-collage
            fenetre.blit(fond, (0,0))
            [fenetre.blit(wall, (key[0], key[1])) for key, value in self.maze_dico.items() if value == "W"]
            fenetre.blit(macgyver, position_macgyver)
            #Rafraichissement
            pygame.display.flip()


if __name__ == "__main__":

    pyga1 = Pygame({(0, 1): "W", (1, 2): "W"})

    # pyga1 = Pygame(dico_grid1)
    # pyga1.graphic_maze()