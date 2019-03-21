#做个抽奖程序，可以输入一个人的名字和抽奖号，然后随机抽取存在的抽奖号，
#程序可以指定抽取次数，抽取后显示抽奖号和名字，
#全部抽取完成后输出抽奖的总结果


#打印功能列表
print("抽奖系统")
print("="*50)
print("1、输入参与抽奖的名单")
print("2、进行抽奖")
print("3、查询中奖名单")
print("4、退出系统")
print("="*50)

prize_list = []
#算法：
while True:
	num = int(input("请输入功能编号："))
	
#1 能够死循环读入不同的名字和抽奖号，使用字典保存，在输入done的时候退出死循环。
	if num == 1:
		#new_name =  input("请输入参与抽奖人的姓名：")
		#new_phone = input("请输入参与抽奖的手机号：")
		user_input = input("请输入参与抽奖的名字和编号：")
		new_name,new_no = user_input.split(" ")
		if user_input.lower() == "done":
			continue
		else:	
			#把输入的信息存到字典中
			prize_infors = {}
			#prize_infors[new_no] = new_name
			prize_infors["name"] = new_name	
			prize_infors["no"] = new_no
			#把多个信息添加到列表上
			prize_list.append(prize_infors)
			
		print(prize_list)	
	elif num == 2:
		pass
	elif num == 3:
		pass
	elif num == 4:
		pass
	else:
		pass

	print("")
#2 输入抽奖的次数，保存到一个变量中。
#3 使用random.shuffle或者choice来随机抽奖抽奖，使用for循环抽取设定的次数，
#4 使用新的字典变量保存抽奖的结果，并输出。
