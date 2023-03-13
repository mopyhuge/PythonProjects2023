import os.path

from scripts.settings import *
from scripts.player import *
from scripts.enemy import *
from scripts.explosions import *



class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.mob_img = []
        self.explosion_animation = {}
        self.explosion_animation["L"] = []
        self.explosion_animation["S"] = []
        self.load_imgs()

        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()
        #pg.mouse.set_visible(False)

        self.player = Player(self,WIDTH/2,HEIGHT-50,self.player_image,BLACK)
        for i in range(10):
            Mob(self,random.choice(self.mob_img),BLACK)


    def load_imgs(self):
        self.bg_image = pg.image.load(os.path.join(bg_folder,bg_image)).convert()
        self.bg_image = pg.transform.scale(self.bg_image,(WIDTH,HEIGHT))
        self.player_image = pg.image.load(os.path.join(player_folder,player_img)).convert()
        self.player_image = pg.transform.scale(self.player_image,(playerW,playerH))
        for i in range(10):
            z = pg.image.load(os.path.join(enemy_folder,str.format("Meteor_0{}.png",i)))
            z = pg.transform.scale(z,(50,50))
            self.mob_img.append(z)
        self.bullet_image = pg.image.load(os.path.join(bullet_folder,"Bomb_2_Explosion_004.png"))
        self.bullet_image = pg.transform.scale(self.bullet_image,(bulletw,bulleth))

        for i in range(8):
            filename = str.format("Explosion_3_00{}.png",i)
            img = pg.image.load(os.path.join(exp_folder,filename)).convert()
            img.set_colorkey(BLACK)
            img_l = pg.transform.scale(img,(75,75))
            img_s = pg.transform.scale(img, (25, 25))
            self.explosion_animation["L"].append(img_l)
            self.explosion_animation["S"].append(img_s)



    def gameLoop(self):
        while self.playing:
            self.checkEvents()
            self.update()
            self.draw()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_a or event.key == pg.K_LEFT:
            #         self.player.setMovex(-movespeed)
            #     if event.key == pg.K_d or event.key == pg.K_RIGHT:
            #         self.player.setMovex(movespeed)
            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_a or event.key == pg.K_LEFT or event.key == pg.K_d or event.key == pg.K_RIGHT:
            #         self.player.setMovex(0)


        # hits = pg.sprite.spritecollide(self.player,self.enemy_group,False)
        # if hits:
        #     for hit in hits:
        #         if self.player.leftclick:
        #             hit.kill()
        #         else:
        #             self.player.kill()
        # hits = pg.sprite.groupcollide(self.player_group,self.enemy_group,True,True)
        # if hits:
        #     self.playing = False


    def update(self):
        self.all_sprites.update()

        hits = pg.sprite.spritecollide(self.player,self.enemy_group,False,pg.sprite.collide_circle)
        if hits:
            self.playing = False
        hits = pg.sprite.groupcollide(self.enemy_group,self.bullet_group,True,True)
        if hits:
            for hit in hits:
                Explosion(self, hit.rect.center, "S")


    def draw(self):
        self.screen.fill(DEFAULT_COLOR)
        self.screen.blit(self.bg_image,self.bg_image.get_rect())
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def startScreen(self):
        pass

    def endScreen(self):
        pass