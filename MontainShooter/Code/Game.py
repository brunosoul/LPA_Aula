#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code import Constantes as c
from Code.Level import Level
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(c.WIN_WIDTH, c.WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [c.MENU_OPTION[0], c.MENU_OPTION[1], c.MENU_OPTION[2]]:
                level = Level(self.window, 'fase1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()
