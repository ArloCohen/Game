import os, sys
import pygame
from pygame.locals import *

import Classes as classes
from classes import *


class GAME:
    def __init__(self, difficulty):
        if difficulty == 1:
            self.gameObjects = games.easyGameObjects
        if difficulty == 2:
            self.gameObjects = games.easyGameObjects
        if difficulty == 3:
            self.gameObjects = games.easyGameObjects
        self.player = Player()
        self.score = 0
        
    def __init__(self, save):
        self.gameObjects = save.gameObjects
        self.score = save.score
        self.player = save.player

    def saveGame(self):
        #write save using pickle to DATA 
    
    
 
