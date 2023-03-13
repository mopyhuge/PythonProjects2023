from tkinter import *
from os import path
import random
from tkinter import ttk

HEIGHT = 1080
WIDTH = 1920

SCREENSIZE = str(HEIGHT)+"x"+str(WIDTH)

title = "Christmas Countdown"

LOCATION = path.dirname(__file__)
images_folder = path.join(LOCATION,"images")
christmas_folder = path.join(images_folder, "christmasImages")
halloween_folder = path.join(images_folder, "halloweenImages")
newyears_folder = path.join(images_folder, "newyearsImages")
easter_folder = path.join(images_folder, "easterImages")
fourthofjuly_folder = path.join(images_folder, "fourthofjulyImages")
bday_folder = path.join(images_folder, "bdayImages")

christmas_image_list = []
halloween_image_list = []
easter_image_list = []
newyears_image_list = []
fourthofjuly_image_list = []
bday_image_list = []


for i in range(5):
    christmas_image_list.append(str.format("christmas{}.png",i+1))

for i in range(5):
    halloween_image_list.append(str.format("halloween{}.png",i+1))

for i in range(5):
    easter_image_list.append(str.format("easter{}.png",i+1))

for i in range(5):
    newyears_image_list.append(str.format("newyears{}.png",i+1))

for i in range(5):
    fourthofjuly_image_list.append(str.format("fourthofjuly{}.png",i+1))

for i in range(5):
    bday_image_list.append(str.format("bday{}.png",i+1))

img_folder_list = [bday_folder,fourthofjuly_folder,christmas_folder,newyears_folder,easter_folder,halloween_folder]

img_lists = [bday_image_list,fourthofjuly_image_list,christmas_image_list,newyears_image_list, easter_image_list, halloween_image_list]
