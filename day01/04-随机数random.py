# !/usr/bin/env python
# -*- coding:utf-8 -*-
import random

player = int(input("请输入 0石头 1剪刀 2布：")) #玩家出拳

computer = random.randint(0,2) #电脑玩家随机获取

#玩家赢到条件
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
	print("恭喜你赢来！")

elif player == computer:
	print("这局是平局！")
else:
	print("你输了，继续加油！")
