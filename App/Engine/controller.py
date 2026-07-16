import pygame as pg


class Controller:

    def __init__(self, game):

        self.game = game

        self.joystick = None

        pg.joystick.init()


        # Procura o DualSense automaticamente
        for i in range(pg.joystick.get_count()):

            joy = pg.joystick.Joystick(i)

            joy.init()


            print(
                f"Joystick {i}: {joy.get_name()}"
            )


            if "DualSense" in joy.get_name():

                self.joystick = joy

                break



        if self.joystick:

            print(
                "Controle ativo:",
                self.joystick.get_name()
            )

        else:

            print(
                "DualSense não encontrado"
            )




    def get_axis(self, axis):

        if not self.joystick:

            return 0


        if axis >= self.joystick.get_numaxes():

            return 0


        value = self.joystick.get_axis(axis)



        # Deadzone para evitar drift

        if abs(value) < 0.15:

            value = 0



        return value





    def update(self):

        if not self.joystick:

            return



        # DualSense padrão SDL

        move_x = self.get_axis(0)

        move_y = self.get_axis(1)


        look_x = self.get_axis(2)



        # Envia para o Player

        self.game.player.controller_input(
            move_x,
            move_y,
            look_x
        )





    def r2_pressed(self):

        if not self.joystick:

            return False


        # Alguns DualSense usam eixo 5 para R2

        if self.joystick.get_numaxes() > 5:

            r2 = self.get_axis(5)

            return r2 > 0.5



        return False