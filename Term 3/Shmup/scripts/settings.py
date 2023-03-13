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

TITLE = "Hi"

WIDTH = 700
HEIGHT = 1000
DEFAULT_COLOR = ANTIMBLUE

fps = 40


game_folder = os.path.dirname(__file__)
game_folder= game_folder.replace("\scripts","")
sprites_folder = os.path.join(game_folder,"sprites")
player_folder = os.path.join(sprites_folder,"player sprites")
enemy_folder = os.path.join(sprites_folder,"enemy_sprites")
bg_folder = os.path.join(sprites_folder,"backgrounds")
exp_folder = os.path.join(bg_folder,"explosions")
bullet_folder = os.path.join(player_folder,"bullets")
powerup_folder = os.path.join(player_folder,"powerups")





debugging = False
solidbounds = True
bouncy = False
playerW = 65
playerH = 65
movespeed = 2

player_img = "Ship_LVL_4.png"
enemy_img = ""
bg_images = ["Space_BG_01.png","Space_BG_02.png","Space_BG_03.png","Space_BG_04.png"]
bg_image = random.choice(bg_images)
bullet_image = "Bomb_2_Explosion_004.png"
bulletw = 10
bulleth = 10