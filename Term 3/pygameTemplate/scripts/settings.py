import os.path

import pygame as pg
import random


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ANTIMBLUE = (50,82,123)
POOPBROWN = (74, 65, 42)

TITLE = ""

WIDTH = 500
HEIGHT = 500
DEFAULT_COLOR = ANTIMBLUE

fps = 60


game_folder = os.path.dirname(__file__)
game_folder= game_folder.replace("\scripts","")
sprites_folder = os.path.join(game_folder,"sprites")
player_sprites = os.path.join(sprites_folder,"player sprites")
enemy_sprites = os.path.join(sprites_folder,"enemy_sprites")






solidbounds = False
bouncy = True
player_img = os.path.join(player_sprites,"download.png")

enemy_img = os.path.join(enemy_sprites,"robot-preview.png")