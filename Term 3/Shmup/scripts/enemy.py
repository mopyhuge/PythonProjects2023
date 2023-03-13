from scripts.settings import *
from scripts.player import *

class Mob(pg.sprite.Sprite):
   def __init__(self, game,img,color):
       super(Mob, self).__init__()
       self.game = game
       self.image_original = img
       # self.image = pg.Surface((50, 50))
       # self.image.fill(RED)
       self.image = self.image_original.copy()
       self.image.set_colorkey(color)
       self.rect = self.image.get_rect()
       self.radius = int(self.rect.width*.85/ 2)
       if debugging:
           pg.draw.circle(self.image, RED, self.rect.center, self.radius)


       self.respawn()
       self.addToGroups()

   def addToGroups(self):
       self.game.all_sprites.add(self)
       self.game.player_group.add(self)

   def update(self):
       self.rect.centerx += self.move_x
       self.rect.centery += self.move_y

       if self.rect.y > HEIGHT + 100:
           self.respawn()
       if self.rect.x > WIDTH + 50 or self.rect.x < -50:
           self.respawn()
       self.rotate()


   def respawn(self):
       self.rect.center = (random.randint(0 + self.rect.width, WIDTH - self.rect.width), random.randint(-250, -40))
       self.move_x = random.randint(-1, 1)
       self.move_y = random.randint(1, 3)
       self.rot = 0
       self.rot_speed = random.randint(-8, 8)
       self.last_update = pg.time.get_ticks()

   def rotate(self):
       now = pg.time.get_ticks()
       if now - self.last_update > fps:
           self.last_update = now
           self.rot = (self.rot + self.rot_speed)%360
           new_image = pg.transform.rotate(self.image_original,self.rot)
           old_center = self.rect.center
           self.image = new_image
           self.rect = self.image.get_rect()
           self.rect.center = old_center








class Enemy(Player):
   width = 50
   height = 50
   def __init__(self, game, x, y, img_dir, color_key):
       super(Enemy, self).__init__(game, x, y,img_dir, color_key)

   def addToGroups(self):
       self.game.all_sprites.add(self)
       self.game.enemy_group.add(self)

   def update(self):
       self.rect.center = (self.rect.centerx + self.move_x, self.rect.centery + self.move_y)

       if self.rect.left <= 0 or self.rect.right >= WIDTH:
           self.move_x *= -1
       if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
           self.move_y *= -1

