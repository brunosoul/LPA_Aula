#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code import Constantes as c


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./Asset/sprite/4.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Asset/sound/arcade-loop.wav')
        pygame.mixer_music.play(-1)
        menu_option = 0

        while True:

            # Desenhar na Tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(
                100,
                'MOUNTAIN SHOOTER',
                c.LARANJA,
                ((c.WIN_WIDTH / 2), (c.WIN_HEIGHT / 2)))

            self.menu_text(
                50,
                'The Space Shooter',
                c.PRETO,
                ((c.WIN_WIDTH / 2), (c.WIN_HEIGHT / 2) + 40))

            for i in range(len(c.MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        25,
                        c.MENU_OPTION[i],
                        c.BRANCO,
                        ((c.WIN_WIDTH / 2), (c.WIN_HEIGHT / 2) + (150 + i * 25))
                    )
                else:
                    self.menu_text(
                        25,
                        c.MENU_OPTION[i],
                        c.PRETO,
                        ((c.WIN_WIDTH / 2), (c.WIN_HEIGHT / 2) + (150 + i * 25))
                    )
            pygame.display.flip()

            # Verificar EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option > len(c.MENU_OPTION) - 1:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(c.MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return c.MENU_OPTION[menu_option]

    # Metodo para escrita de textos
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida sans typewrite", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
