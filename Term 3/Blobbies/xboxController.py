import pygame as pg

class Controller():
    def __init__(self,cont_number=0):
        self.dead_zone = .075
        try:
            self.controller = pg.joystick.Joystick(cont_number)
            self.controller.init()
            try:
                cont_id = self.controller.get_instance_id()
            except AttributeError:
                cont_id = self.controller.get_id()
        except IOError:
            print("no controller connected")

    def get_hat(self):
        hat = self.controller.get_hat(0)
        x = hat[0]
        y = hat[1]*-1
        hat_dict = {"H_X":x,"H_Y":y}
        return hat_dict

    def get_buttns(self):
        a_button = self.controller.get_button(0)
        b_button = self.controller.get_button(1)
        x_button = self.controller.get_button(2)
        y_button = self.controller.get_button(3)
        lb_button = self.controller.get_button(4)
        rb_button = self.controller.get_button(5)
        lm_button = self.controller.get_button(6)
        rm_button = self.controller.get_button(7)
        lj_button = self.controller.get_button(8)
        rj_button = self.controller.get_button(9)
        xbox_button = self.controller.get_button(10)


        buttons_dict = {"CONT_A":a_button,"CONT_B":b_button,"CONT_X":x_button,"CONT_Y":y_button,"CONT_LB":lb_button,"CONT_RB":rb_button,"CONT_LM":lm_button,"CONT_RM":rm_button,
                        "CONT_LJ":lj_button,"CONT_LJ":lj_button,"CONT_XBOX":xbox_button,}
        return buttons_dict

    def get_axes(self):

        lxj_axis = self.controller.get_axis(0)
        lyj_axis = self.controller.get_axis(1)
        rxj_axis = self.controller.get_axis(2)
        ryj_axis = self.controller.get_axis(3)
        lt_axis = self.controller.get_axis(4)
        rt_axis = self.controller.get_axis(5)

        if lyj_axis < self.dead_zone and lyj_axis > -self.dead_zone:
            lyj_axis = 0
        if lxj_axis < self.dead_zone and lxj_axis > -self.dead_zone:
            lxj_axis = 0
        if ryj_axis < self.dead_zone and ryj_axis > -self.dead_zone:
            ryj_axis = 0
        if rxj_axis < self.dead_zone and rxj_axis > -self.dead_zone:
            rxj_axis = 0

        axis_dict = {"CONT_LXJ":lxj_axis,"CONT_LYJ":lyj_axis,"CONT_RXJ":rxj_axis,"CONT_RYJ":ryj_axis,"CONT_LT":lt_axis,"CONT_RT":rt_axis}
        return axis_dict