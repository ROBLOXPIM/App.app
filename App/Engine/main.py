import pygame as pg
import sys

from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

from ascii_renderer import *
from controller import *



class Game:


    def __init__(self):

        pg.init()

        pg.joystick.init()


        pg.mouse.set_visible(False)


        self.screen = pg.display.set_mode(
            RES
        )


        pg.event.set_grab(True)


        self.clock = pg.time.Clock()


        self.delta_time = 1


        self.global_trigger = False


        self.global_event = pg.USEREVENT + 0


        pg.time.set_timer(
            self.global_event,
            40
        )


        self.new_game()




    def new_game(self):

        self.map = Map(self)


        self.player = Player(self)



        # precisa vir antes do raycasting
        self.object_renderer = ObjectRenderer(self)



        self.raycasting = RayCasting(self)


        self.object_handler = ObjectHandler(self)


        self.weapon = Weapon(self)


        self.sound = Sound(self)


        self.pathfinding = PathFinding(self)



        self.ascii_renderer = ASCIIRenderer(self)



        self.controller = Controller(self)



        if self.controller.joystick:

            print(
                "Controle ativo:",
                self.controller.joystick.get_name()
            )

        else:

            print(
                "Nenhum controle encontrado"
            )



        try:

            pg.mixer.music.play(-1)

        except:

            pass






    def update(self):


        # DualSense

        if self.controller:

            self.controller.update()



        self.player.update()



        self.raycasting.update()



        self.object_handler.update()



        self.weapon.update()



        self.delta_time = self.clock.tick(
            FPS
        )



        pg.display.set_caption(
            f'{self.clock.get_fps():.1f}'
        )






    def draw(self):


        self.screen.fill(
            "black"
        )



        # Modo ASCII

        if self.ascii_renderer.enabled:


            self.ascii_renderer.draw()



        # Modo normal

        else:


            self.object_renderer.draw()


            self.weapon.draw()



        pg.display.flip()







    def check_events(self):


        self.global_trigger = False



        for event in pg.event.get():



            if event.type == pg.QUIT:

                pg.quit()

                sys.exit()





            elif event.type == self.global_event:

                self.global_trigger = True





            # Alternar ASCII

            if event.type == pg.KEYDOWN:


                if event.key == pg.K_F1:

                    self.ascii_renderer.toggle()





            # player eventos

            self.player.single_fire_event(
                event
            )








    def run(self):


        while True:


            self.check_events()


            self.update()


            self.draw()






if __name__ == "__main__":


    game = Game()

    game.run()