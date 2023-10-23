#!/usr/bin/python
#-*- coding: utf-8 -*-
from Code.Entity import Entity


class Level:
    def __init__(self, window, name, modo):
        self.window = window
        self.name = name
        self.mode = modo
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass

