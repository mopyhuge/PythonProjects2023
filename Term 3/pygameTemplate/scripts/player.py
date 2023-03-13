from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self, game,x,y,img_dir,color_key):
        super(Player, self).__init__()

        self.image = self.getImage(img_dir)
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.game = game
        # self.image = pg.Surface((50, 50))
        # self.image.fill(color)
        # self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.move_x = 1
        self.move_y = 1
        self.leftclick = False

        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    def getImage(self,img_dir):
        self.img = pg.image.load(img_dir).convert()
        self.img = pg.transform.scale(self.img, (75, 75))

        return self.img


    def update(self):
        self.rect.center = pg.mouse.get_pos()
        self.leftclick = pg.mouse.get_pressed()[0]


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
