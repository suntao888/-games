import pygame as pg
import sys

pg.init()

game_window = pg.display.set_mode((600, 500))
pg.display.set_caption('接球小游戏')
window_color = (0, 0, 255)
while True:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
