#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Constantes import WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./Asset/sprite/4.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Asset/sound/arcade-loop.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(
                200,
                'Mountain Shooter',
                (255, 128, 0),
                ((WIN_WIDTH / 2), 700))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida sans typewrite", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)

