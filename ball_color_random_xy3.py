import pygame as pg
import random
import sys

pg.init()

game_window = pg.display.set_mode((600, 500))
pg.display.set_caption('接球小游戏')
window_color = (0, 0, 255)
ball_color = (255, 255, 0)
ball_x = random.randint(20, 580)
ball_y = 20
while True:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)

    pg.display.update()
