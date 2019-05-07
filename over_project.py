import pygame as pg
import sys
import random
import time
print("""

""")
# print("""			 
# 		            _oo8oo_
# 		           o8888888o
# 		           88: . :88
# 		           (: -_- :)
# 		           0\  =  /0
# 		        ____/'==='\____
		         
# 	""")
print("""
			            _oo8oo_
			           o8888888o
			           88: . :88
			           (: -_- :)
			           0\  =  /0
			        ____/'==='\____
				 欢迎使用Python游戏平台

	1.登录账号密码，正确直接进入2，若输入3次也可以进入，但提示游客身份进入。
	2.系统产生1-10随机数，猜对直接进入3，或猜错5次也可以进入，但提示未通关。
	3.接小球游戏，每三次速度加快，分数翻倍。

		********谢谢大家观看*******
	""")
count = 0
while count < 3:
    name = str(input("请输入帐号"))
    passwd = str(input("请输入密码"))
    if (name != "suntao" or passwd != "123456"):
        count += 1
        s = 3 - count
        print("输入错误,还剩%d次机会\n" % s)
        if s == 0:
            print("您是游客身份登录")
    else:
        print("尊敬的VIP，您已登录成功,直接进入游戏\n")
        break

count1 = 0
number = random.randint(1, 10)
print("""		######系统将要产生1-10随机数######
	  #########猜对直接进入游戏###############
	 ########猜大会提示大，猜小提示小了########
	###猜错6次也可以进入游戏，但本次游戏未通关####

	""")
print(number)
while True:
    num = int(input("请输入您要猜的整数"))
    count1 += 1
    if (count1 < 6):
        if (num == number):
            print("您通关了，总共输入了%d次\n" % (count1))
            print("成功，进入下一个游戏\n")
            break
        elif (num < number):
            print("您输入小了,请再猜猜看\n")
        else:
            print("您输入大了,请再猜猜看\n")
    else:
        print("""	        ******本关未通关*********
            *******输入次数已经达到6次***
           *********进入下一个游戏************

                """)
        break

pg.init()
print("游戏开始，您的初始分值为0\n")
game_window = pg.display.set_mode((600, 500))
pg.display.set_caption('接球小游戏')
window_color = (0, 0, 255)
ball_color = (255, 165, 0)
rect_color = (255, 0, 0)
score = 0
font = pg.font.SysFont('arial', 70)
ball_x = random.randint(20, 580)
ball_y = 20
move_x = 1
move_y = 1
point = 1
count = 0
while True:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    mouse_x, mouse_y = pg.mouse.get_pos()
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)
    pg.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))
    my_text = font.render(str(score), False, (255, 255, 255))
    game_window.blit(my_text, (500, 30))
    ball_x += move_x
    ball_y += move_y
    if ball_x <= 20 or ball_x >= 580:
        move_x = -move_x
    if ball_y <= 20:
        move_y = -move_y
    elif mouse_x - 20 < ball_x < mouse_x + 120 and ball_y >= 470:
        move_y = -move_y
        score += point
        count += 1
        if count == 3:
            count = 0
            point += point
            if move_x > 0:
                move_x += 1
            else:
                move_x -= 1
            move_y -= 1
    elif ball_y >= 480 and (ball_x <= mouse_x - 20 or ball_x >= mouse_x + 120):
        time.sleep(3)
        break
    pg.display.update()
    time.sleep(0.005)
print("游戏结束,您的得分为%d" % (score))
