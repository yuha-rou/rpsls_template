#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：周雨柔
日期：2020.4.14
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀


def name_to_number(name):# 自定义函数将中文转换成数字
	if name=="rock":
		return 0
	elif name=="spock":
		return 1
	elif name=="paper":
		return 2
	elif name=="lizard":
		return 3
	elif name=="scissors":
		return 4
	else:
		return None
		

def number_to_name(number):# 自定义函数将数字转换为中文
	if number==0:
		return "rock"
	elif number==1:
		return "spock"
	elif number==2:
		return "paper"
	elif number==3:
		return "lizard"
	elif number==4:
		return "scissors"
	else:
		return None
		
  

def rpsls(player_choice):
	player_choice_number=name_to_number(choice_name) # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	comp_number=random.randrange(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
	comp_choice=number_to_name(comp_number) # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	print("----------------")
	print("您的选择为：",str(choice_name))
	print("计算机的选择为：",str(comp_choice)) # 在屏幕上显示计算机选择的随机对象
	if comp_number==player_choice_number:    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
		print("您和计算机出的一样呢")
	elif player_choice_number==0 and (comp_number==4 or comp_number==3):
		print("您赢了!")
	elif player_choice_number==1 and (comp_number==4 or comp_number==0):
		print("您赢了!")
	elif player_choice_number==2 and (comp_number==0 or comp_number==1):
		print("您赢了!")
	elif player_choice_number==3 and (comp_number==1 or comp_number==2):
		print("您赢了")
	elif player_choice_number==4 and (comp_number==2 or comp_number==3):
		print("您赢了!") 
	elif comp_number==0 and (player_choice_number==4 or player_choice_number==3):
		print("计算机赢了")
	elif comp_number==1 and (player_choice_number==4 or player_choice_number==0):
		print("计算机赢了")	
	elif comp_number==2 and (player_choice_number==0 or player_choice_number==1):
		print("计算机赢了") 
	elif comp_number==3 and (player_choice_number==1 or player_choice_number==2):
		print("计算机赢了")
	elif comp_number==4 and (player_choice_number==2 or player_choice_number==3):
		print("计算机赢了")
	else:
		print("Error: No Correct Name")
	
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)



