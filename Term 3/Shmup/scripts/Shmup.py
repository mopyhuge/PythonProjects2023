from scripts.settings import *
from scripts.player import *
from scripts.enemy import *



class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        pg.mouse.set_visible(False)

        self.player = Player(self,300,100,player_img,BLACK)


    def gameLoop(self):
        while self.playing:
            self.checkEvents()
            self.update()
            self.draw()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
        # hits = pg.sprite.spritecollide(self.player,self.enemy_group,False)
        # if hits:
        #     for hit in hits:
        #         if self.player.leftclick:
        #             hit.kill()
        #         else:
        #             self.player.kill()
        hits = pg.sprite.groupcollide(self.player_group,self.enemy_group,True,True)
        if hits:
            self.playing = False


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(DEFAULT_COLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def startScreen(self):
        pass

    def endScreen(self):
        pass