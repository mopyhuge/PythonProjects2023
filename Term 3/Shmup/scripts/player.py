from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self, game,x,y,img,color):
        super(Player, self).__init__()

        self.game = game
        # self.image = pg.Surface((50, 50))
        # self.image.fill(color)
        self.image = img
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        if debugging:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (x,y)
        self.move_x = 0
        # self.move_y = 1
        # self.leftclick = False
        self.addToGroups()
        self.canShoot = True


    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    # def getImage(self,img_dir):
    #     self.img = pg.image.load(img_dir).convert()
    #     self.img = pg.transform.scale(self.img, (75, 75))
    #
    #     return self.img

    def setMovex(self,value):
        self.move_x = value

    def update(self):
        self.move_x = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.setMovex(-movespeed)
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.setMovex(movespeed)
        if keystate[pg.K_SPACE]:
            self.shootBullet()

        # if self.rect.x > WIDTH:
        #     self.rect.bottom = 0
        #     self.rect.centerx = WIDTH/2
        #     self.move_x=0
        #     self.move_y = 100
        # if self.rect.y > HEIGHT:
        #     self.rect.right = 0
        #     self.rect.centery = HEIGHT/2
        #     self.move_x=100
        #     self.move_y = 0
        if not solidbounds:
            if self.rect.left > WIDTH:
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = WIDTH
            if self.rect.top > HEIGHT:
                self.rect.bottom = 0
            if self.rect.bottom < 0:
                self.rect.top = HEIGHT
        else:
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.top > 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        if bouncy:
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.move_x *= -1
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.move_y *= -1

        self.rect.x += self.move_x
    def shootBullet(self):
        Bullet(self.game,self.rect.centerx,self.rect.top-2,self.game.bullet_image)

class Bullet(pg.sprite.Sprite):
    def __init__(self,game,x,y,img):
        super(Bullet, self).__init__()
        self.game = game
        self.image = img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.bottom = y
        self.rect.centerx = x
        self.move_y = 0
        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    def update(self):
        self.rect.y += self.move_y
        if self.rect.bottom < 0:
            self.kill()