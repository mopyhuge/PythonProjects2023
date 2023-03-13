from settings import *
from gameObjects import *
import random

def draw_Text(screen,text,size,x,y,color):
    font_name = pg.font.match_font("Papyrus")
    font = pg.font.Font(font_name,size)
    text_sprite = font.render(text,True,color)
    text_rect = text_sprite.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_sprite,text_rect)

class Game():

    def __init__(self):
        enemies = []
        self.playing = True
        self.level = 1
        self.game_window = pg.display.set_mode((BG_WIDTH, BG_HEIGHT))
        self.clock = pg.time.Clock()

        joystick_count = pg.joystick.get_count()
        if joystick_count > 0:
            self.xbox_controller = Controller()
        else:
            self.xbox_controller = None

        self.startscreen = GameObject(0, 0, BG_WIDTH, BG_HEIGHT, start_screen)
        self.background_img = GameObject(0,0,BG_WIDTH,BG_HEIGHT,bgimg_location)

        self.treasure = GameObject(375, 30, T_WIDTH, T_HEIGHT, treasure_location)
        self.player = Player(player_start_pos_x, player_start_pos_y, tile_size, tile_size, player_img, player_speed)
        self.hasXtrLife = False
        self.extraLife_x = 1000
        self.extraLife_y = 0


        self.extraLife = GameObject(self.extraLife_x, self.extraLife_y, T_WIDTH, T_HEIGHT, extra_life)

        self.nextLevel()

    def spawn_enemies(self,number):
        start = 0
        x = 0
        for i in range(number):
            enemy_x = random.randint(0, BG_WIDTH - tile_size)
            start += 105
            enemy_y = start
            flip = random.choice(("h", "t"))
            speed = random.randint(10, 15)
            if flip == "t":
                speed *= -1
            enemy = Enemy(enemy_x, enemy_y+75, tile_size, tile_size, enemy_img, enemy_speed)
            self.enemies_list.append(enemy)
            x+=1
            if x > 6:
                start = 0
                x = 0

    def start_game_loop(self):
        while self.playing:

            self.clock.tick(fps)

            self.get_inputs()

            self.update()

            self.draw()

    def get_inputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.playing = False
        self.get_player_inputs(events)

    def update(self):
        self.player.move()

        for enemy in self.enemies_list:
            enemy.move(BG_WIDTH)

        if self.detect_Collisions(self.player,self.treasure):
            self.player.collect()
            self.treasure.collect()
        if self.detect_Collisions(self.player,self.extraLife):
            self.extraLife.x += 1000
            self.player.lives += 1

        for enemy in self.enemies_list:
            if self.detect_Collisions(self.player, enemy):
                self.player.die()
                if self.player.lives > 0:
                    self.resetLevel()
                else:
                    self.playing = False

        if self.player.collected and self.player.y > BG_HEIGHT-75:
            self.nextLevel()

    def show_start_screen(self):
        self.game_window.fill(blue)
        self.game_window.blit(self.startscreen.image, (self.startscreen.x, self.startscreen.y))
        draw_Text(self.game_window, "Welcome", 60, BG_WIDTH / 2, BG_HEIGHT / 5, black)
        draw_Text(self.game_window, "to", 60, BG_WIDTH / 2, BG_HEIGHT / 4, black)
        draw_Text(self.game_window, "Blobbies", 60, BG_WIDTH / 2, BG_HEIGHT / 3.15, black)
        draw_Text(self.game_window, "Press A / Space to start", 40, BG_WIDTH / 2, BG_HEIGHT / 2.25, black)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"
            button_inputs = self.xbox_controller.get_buttns()
            a = button_inputs.get("CONT_A")
            if a > 0:
                waiting = False
            start = button_inputs.get("CONT_RM")
            if start > 0:
                return "end"

    def draw(self):
        self.game_window.fill(blue)
        self.game_window.blit(self.background_img.image,(self.background_img.x, self.background_img.y))
        self.game_window.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        self.game_window.blit(self.player.image,(self.player.x,self.player.y))
        self.game_window.blit(self.extraLife.image,(self.extraLife.x,self.extraLife.y))
        for enemy in self.enemies_list:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))


        pg.display.update()

    def get_player_inputs(self, events):
        if self.xbox_controller:
            #hat = self.xbox_controller.get_hat()
            #self.player.set_move_dir(hat.get("H_X"),hat.get("H_Y"))
            axis = self.xbox_controller.get_axes()
            self.player.set_move_dir(axis.get("CONT_LXJ"),axis.get("CONT_LYJ"))

            button_inputs = self.xbox_controller.get_buttns()
            a = button_inputs.get("CONT_A")

            if(a>0):
                self.player.sprint()
            else:
                self.player.walk()

        else:
            for event in events:
                if event.type == pg.KEYDOWN:
                    if pg.K_LEFT or pg.K_a:
                         self.player.set_move_dir(0, -1)
                    if pg.K_RIGHT or pg.K_d:
                        self.player.set_move_dir(0, 1)
                    if pg.K_UP or pg.K_w:
                        self.player.set_move_dir(-1, 0)
                    if pg.K_DOWn or pg.K_s:
                        self.player.set_move_dir(1, 0)
                    if event.key == pg.K_RSHIFT:
                        self.player.sprint()

                elif event.type == pg.KEYUP:
                    if event.key == pg.K_w or event.key == pg.K_UP or event.key == pg.K_s or \
                            event.key == pg.K_DOWN or event.key == pg.K_a or event.key == pg.K_LEFT \
                            or event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.player.set_move_dir(0, 0)
                    if event.key == pg.K_RSHIFT:
                        self.player.walk()

    def detect_Collisions(self,obj1,obj2):
        if obj1.x > (obj2.x + obj2.width):
            return False
        elif (obj1.x + obj1.width) < obj2.x:
            return False

        if obj1.y > (obj2.y + obj2.height):
            return False
        elif (obj1.y + obj1.height) < obj2.y:
            return False

        return True

    def show_game_over_screen(self):
        self.game_window.fill(red)
        draw_Text(self.game_window,"Game Over",80,BG_WIDTH/2,BG_HEIGHT/3,black)
        draw_Text(self.game_window, "Press A / Enter to play again", 30, BG_WIDTH / 2, BG_HEIGHT / 2, black)
        draw_Text(self.game_window, "Press the Menu Button / Escape to quit", 30, BG_WIDTH / 2, BG_HEIGHT/1.8, black)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"
            button_inputs = self.xbox_controller.get_buttns()
            a = button_inputs.get("CONT_A")
            if a > 0:
                waiting = False
            start = button_inputs.get("CONT_RM")
            if start > 0:
                return "end"

    def nextLevel(self):
        self.level+=1
        self.player.collected = False
        self.resetLevel()
        self.enemies_list = []
        self.spawn_enemies(self.level)
        self.hasXtrLife = random.choice([True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False])
        if self.hasXtrLife:
            self.extraLife_x = random.randint(0+tile_size/2,BG_WIDTH-tile_size)
            self.extraLife_y = random.randint(0+tile_size/2,BG_HEIGHT-tile_size)
        else:
            self.extraLife_x = 1000
            self.extraLife_y = 0
        self.extraLife.x = self.extraLife_x
        self.extraLife.y = self.extraLife_y


    def resetLevel(self):
        self.treasure.reset()
        self.player.reset()
