#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020.4.14
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����


def name_to_number(name):# �Զ��庯��������ת��������
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
		

def number_to_name(number):# �Զ��庯��������ת��Ϊ����
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
	player_choice_number=name_to_number(choice_name) # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
	comp_number=random.randrange(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
	comp_choice=number_to_name(comp_number) # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
	print("----------------")
	print("����ѡ��Ϊ��",str(choice_name))
	print("�������ѡ��Ϊ��",str(comp_choice)) # ����Ļ����ʾ�����ѡ����������
	if comp_number==player_choice_number:    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
		print("���ͼ��������һ����")
	elif player_choice_number==0 and (comp_number==4 or comp_number==3):
		print("��Ӯ��!")
	elif player_choice_number==1 and (comp_number==4 or comp_number==0):
		print("��Ӯ��!")
	elif player_choice_number==2 and (comp_number==0 or comp_number==1):
		print("��Ӯ��!")
	elif player_choice_number==3 and (comp_number==1 or comp_number==2):
		print("��Ӯ��")
	elif player_choice_number==4 and (comp_number==2 or comp_number==3):
		print("��Ӯ��!") 
	elif comp_number==0 and (player_choice_number==4 or player_choice_number==3):
		print("�����Ӯ��")
	elif comp_number==1 and (player_choice_number==4 or player_choice_number==0):
		print("�����Ӯ��")	
	elif comp_number==2 and (player_choice_number==0 or player_choice_number==1):
		print("�����Ӯ��") 
	elif comp_number==3 and (player_choice_number==1 or player_choice_number==2):
		print("�����Ӯ��")
	elif comp_number==4 and (player_choice_number==2 or player_choice_number==3):
		print("�����Ӯ��")
	else:
		print("Error: No Correct Name")
	
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


