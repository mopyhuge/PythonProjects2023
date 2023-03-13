import pygame as pg


BLACK = pg.Color("black")
WHITE= pg.Color("white")

class TextPrint(object):
    def __init__(self,fontsize):
        self.fontsize = fontsize
        self.x = ""
        self.y = ""
        self.line_height = ""
        self.font = pg.font.Font(None,fontsize)


    def tprint(self,screen,text):
        textBitmap = self.font.render(text,True,BLACK)
        screen.blit(textBitmap,(self.x,self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 15
        self.y = 15
        self.line_height = self.fontsize-5

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10




pg.init()
screen = pg.display.set_mode((500,800))
pg.display.set_caption("XBOX Controller Test")

running = True

clock = pg.time.Clock()
fps = 40
text = TextPrint(25)


pg.joystick.init()
controller_list = []

while running:


    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.JOYBUTTONDOWN:
            print("Pressed a button")
        elif event.type == pg.JOYBUTTONUP:
            print("Released a button")
    screen.fill(WHITE)
    text.reset()

    joystick_count = pg.joystick.get_count()
    text.tprint(screen,"number of joysticks {}".format(joystick_count))
    text.indent()

    for i in range(joystick_count):
        controller = pg.joystick.Joystick(i)
        controller.init()

        try:
            cont_id = controller.get_instance_id()
        except AttributeError:
            cont_id = controller.get_id()
        text.tprint(screen,"Controller {}".format(cont_id))
        text.indent()

        cont_name = controller.get_name()
        text.tprint(screen,"controller name {}".format(cont_name))

        try:
            guid = controller.get_guid()
        except AttributeError:
            pass
        else:
            text.tprint(screen,"GUID {}".format(guid))

        axes = controller.get_numaxes()
        text.tprint(screen,"number of axes {}".format(axes))
        text.indent()

        for i in range(axes):
            axis = controller.get_axis(i)
            text.tprint(screen,"Axis {} value{:>6.3f}".format(i,axis))
        text.unindent()

        buttons = controller.get_numbuttons()
        text.tprint(screen, "number of buttons {}".format(buttons))
        text.indent()

        for i in range(buttons):
            button = controller.get_button(i)
            text.tprint(screen, "Button {:>2} value: {}".format(i,button))
        text.unindent()

        hats = controller.get_numhats()
        text.tprint(screen, "number of hats {}".format(hats))
        text.indent()

        for i in range(hats):
            hat = controller.get_hat(i)
            text.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        text.unindent()

    pg.display.flip()

pg.quit()
quit()