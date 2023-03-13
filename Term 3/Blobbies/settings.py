import pygame as pg
from xboxController import *


TITLE = ""

BG_WIDTH = 800
BG_HEIGHT = 1000

tile_size = BG_HEIGHT//20

T_WIDTH= 50
T_HEIGHT= 50

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

fps = 40

bgimg_location = "sprites/background.png"
treasure_location = "sprites/treasure.png"
player_img = "sprites/player.png"
enemy_img = "sprites/enemy.png"
start_screen = "sprites/startscreen.png"
extra_life = "sprites/heart.png"

player_start_pos_x = BG_WIDTH//2-tile_size//2
player_start_pos_y = BG_HEIGHT - tile_size
player_speed = 5
sprint_mod = 2

enemy_speed = 10



