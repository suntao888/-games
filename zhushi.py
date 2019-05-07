#!/usr/bin/env python

import pygame as pg  # 进入pygame模块，如果没有需要在终端里用pip命令装一下pygame模块

import sys
import random
import time  # 循环如果不加控制，电脑处理起来还是非常快的，慢一点的话，需要让循环等一会，用到time模块

pg.init()  # 开发的代码第一步就是对模块进行初始化操作
game_window = pg.display.set_mode((600, 500))  # 画窗口，用方法，这个方法可以生成一个游戏窗口，里面的参数需要给一个元组，元组的两个元素分别是窗口的宽和高
pg.display.set_caption('接球')  # 标题
window_color = (0, 0, 255)  # 蓝色rgb元组里面的元素，用rgb来表示
ball_color = (255, 165, 0)  # 黄色的rgb值
rect_color = (255, 0, 0)
score = 0
font = pg.font.SysFont('arial', 70)
ball_x = random.randint(20, 580)  # 用random模块生成一个随机数，不让球固定定义两个变量来保存球的位置，球的半径定义为20
ball_y = 20  # 球在y轴的变量
move_x = 1  # 通过一个变量将值保存下来，通过改变变值得大小来改变球的速度
move_y = 1
point = 1
count = 0
print("\n")
print("游戏开始\n")
while True:

    game_window.fill(window_color)  # 传递参数
    for event in pg.event.get():  # 可退出，这是一个状态
        if event.type == pg.QUIT:  #
            sys.exit()  # sys模块里面的方法

    mouse_x, mouse_y = pg.mouse.get_pos()  # 用来接收鼠标返回的xy坐标
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)  #
    pg.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))  # rectangle的缩写，画一个矩形
    my_text = font.render(str(score), False, (255, 255, 255))
    game_window.blit(my_text, (500, 30))  # 这个位置是经过调试，感觉比较合适
    ball_x += move_x  # 每次横纵坐标都加1，这样看起来比较快，就像球在动
    ball_y += move_y
    if ball_x <= 20 or ball_x >= 580:
        move_x = -move_x  # 将加改为减就是向反方向移动
    if ball_y <= 20:
        move_y = -move_y
    elif mouse_x - 20 < ball_x < mouse_x + 120 and ball_y >= 470:
        move_y = -move_y
        score += point  # 需要一个变量来保存每次加的点数
        count += 1
        if count == 3:  # 需要一个变量来保存每次接的次数
            count = 0  # 将其重置为0
            point += point
            if move_x > 0:
                move_x += 1
            else:
                move_x -= 1
            move_y -= 1
    elif ball_y >= 480 and (ball_x <= mouse_x - 20 or ball_x >= mouse_x + 120):
        print("游戏结束")
        time.sleep(3)
        break
    pg.display.update()  # 更新窗口
    time.sleep(0.005)  # 别这么快，睡一会，这个0.005是我实验出来的，如果感觉慢的话，自己可以调
