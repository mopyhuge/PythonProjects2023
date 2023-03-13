from scripts.settings import *

class Explosion(pg.sprite.Sprite):
    def __init__(self,game,center,size):
        super(Explosion, self).__init__()
        self.size = size
        self.game = game
        self.frame = 0
        self.image = self.game.explosion_animation[self.size][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 30
        self.game.all_sprites.add(self)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame+= 1
            if self.frame == len(self.game.explosion_animation[self.size]):
                self.kill()
            else:
                old_center = self.rect.center
                self.image = self.game.explosion_animation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = old_center

