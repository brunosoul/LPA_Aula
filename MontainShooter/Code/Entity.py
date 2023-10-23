#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC

import pygame.image


class Entity(ABC):
    def __init__(self, name, ):
        self.name = name
        self.image = pygame.image.load('/Asset/sprite/Ocean' + fase + name +'.png')
        self.rect = None

    def Move(self, ):
        pass

