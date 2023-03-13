from settings import *

class GameObject():
   def __init__(self, x, y, width, height,  image_path):
       image = pg.image.load(image_path)
       self.image = pg.transform.scale(image, (width,height))
       self.start_x = x
       self.start_y = y
       self.width = width
       self.height = height

       self.x = x
       self.y = y
   def collect(self):
       self.y -= 100

   def reset(self):
       self.x = self.start_x
       self.y = self.start_y




class Player(GameObject):

   def __init__(self,x,y,width,height,image_path,speed):
       super(Player, self).__init__(x,y,width,height,image_path)
       self.speed = speed
       self.lives = 3
       self.move_dir_y = 0
       self.move_dir_x = 0
       self.sprint_speed = speed*2
       self.norm_speed = speed
       self.collected = False

   def move(self):
       if self.y < 0:
           self.y = 0
           return
       if self.y > BG_HEIGHT-tile_size:
           self.y = BG_HEIGHT-tile_size
           return
       self.y += (self.move_dir_y * self.speed)

       if self.x < 0:
           self.x = 0
           return
       if self.x > BG_WIDTH-tile_size:
           self.x = BG_WIDTH-tile_size
           return
       self.x += (self.move_dir_x * self.speed)

   def set_move_dir(self,x,y):
       self.move_dir_x = x
       self.move_dir_y = y

   def sprint(self):
       self.speed = self.sprint_speed

   def walk(self):
       self.speed = self.norm_speed

   def collect(self):
       self.collected = True

   def die(self):

       self.x += 500
       self.lives -= 1
       self.collected = False
       print(self.lives)

class Enemy(GameObject):
    def __init__(self,x,y,width,height,image_path,speed):
        super().__init__(x,y,width,height,image_path)
        self.speed = speed

    def move(self,max_width):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x > max_width - self.width:
            self.speed = -self.speed
        self.x+= self.speed