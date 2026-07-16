import pygame as pg
from settings import *


class ASCIIRenderer:

    def __init__(self, game):

        self.game = game

        # Liga por padrão
        self.enabled = False


        # Resolução interna do "monitor ASCII"
        self.width = 100
        self.height = 50


        self.char_width = 8
        self.char_height = 12


        self.font = pg.font.SysFont(
            "consolas",
            12
        )


        self.surface_width = self.width * self.char_width
        self.surface_height = self.height * self.char_height


        self.surface = pg.Surface(
            (
                self.surface_width,
                self.surface_height
            )
        )


        self.chars = "@%#*+=-:. "




    def toggle(self):

        self.enabled = not self.enabled

        print(
            "ASCII Renderer:",
            "ATIVADO" if self.enabled else "DESATIVADO"
        )




    def enable(self):

        self.enabled = True




    def disable(self):

        self.enabled = False





    def get_shade(self, depth):

        index = int(depth * 2)


        if index >= len(self.chars):

            index = len(self.chars) - 1


        return self.chars[index]





    def render(self):

        buffer = [
            [" " for _ in range(self.width)]
            for _ in range(self.height)
        ]



        rays = self.game.raycasting.ray_casting_result



        if not rays:

            return





        for ray, data in enumerate(rays):

            depth, proj_height, texture, offset = data



            if proj_height <= 0:

                continue




            column_height = int(
                self.height * HEIGHT / proj_height
            )



            if column_height < 1:

                column_height = 1



            if column_height > self.height:

                column_height = self.height





            start = (
                self.height - column_height
            ) // 2



            end = start + column_height





            x = int(
                ray * self.width / len(rays)
            )



            if x >= self.width:

                x = self.width - 1





            char = self.get_shade(depth)





            for y in range(start, end):

                if 0 <= y < self.height:

                    buffer[y][x] = char






        self.surface.fill(
            (0, 0, 0)
        )





        for y, row in enumerate(buffer):

            line = "".join(row)



            text = self.font.render(
                line,
                True,
                (200, 200, 200)
            )



            self.surface.blit(
                text,
                (
                    0,
                    y * self.char_height
                )
            )






    def draw(self):

        if not self.enabled:

            return



        self.render()



        screen_width, screen_height = self.game.screen.get_size()



        x = (
            screen_width - self.surface_width
        ) // 2


        y = (
            screen_height - self.surface_height
        ) // 2





        self.game.screen.blit(
            self.surface,
            (
                x,
                y
            )
        )