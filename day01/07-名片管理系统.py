#1、打印功能提示（增删改查）
print("="*50)
print("	名片管理系统")
print("1.添加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有名片信息")
print("6.推出系统")
print("="*50)

#用来存储名片
card_infors = []
#2、获取用户的选择
while True:
	num = int(input("请输入功能序号："))

#3、根据用户的选择，执行相应的功能
	if num == 1:  
		new_name = input("请输入名字：")
		new_age = input("请输入年龄：")
		new_qq = input("请输入QQ：")
		new_addr = input("请输入住址：")

		#定义一个字典，存储输入的信息
		personal_infor = {}
		personal_infor["name"] = new_name
		personal_infor["age"] = new_age
		personal_infor["qq"] = new_qq
		personal_infor["addr"] = new_addr

		#将一个字典，添加到列表中
		card_infors.append(personal_infor)
		
		print(card_infors) #测试名片是否添加上
	elif num == 2:
		del_name = input("请输入你要删除的名字：")
		
		find_flag = False
		for temp in card_infors:
			if del_name == temp["name"]:
				find_flag = True
				card_infors.remove(temp)
				print("已删除！")
				break
		else:
			print("你要删除的姓名不存在...")
	
		#print(card_infors) #测试删除是否删除输入的姓名名片

	elif num == 3:
		old_name = input("请问你要修改谁的名片?请输入：")
		
		find_flag = False
		for temp in card_infors:
			if old_name == temp["name"]:
				find_flag = True
				#print(temp)
				
				#修改新的信息
				new_name = input("请输入修改的名字：")
				new_age = input("请输入修改的年龄：")
				new_qq = input("请输入修改的QQ：")
				new_addr = input("请输入修改的住址：")
				
				#把输入修改的信息存入字典
				temp["name"] = new_name
				temp["age"] = new_age
				temp["qq"] = new_qq
				temp["addr"] = new_addr
				
				print("已修改！")
				break
		else:
			print("你要修改的人不存在...")
		print("姓名\t年龄\tQQ\t住址")
		#打印修改后的信息（测试用）
		print("%s\t%s\t%s\t%s"%(temp["name"],temp["age"],temp["qq"],temp["addr"]))

	elif num == 4:
		name = input("请输入你要查询的姓名:")
		
		find_flag = False	
		for temp in card_infors:
			if name == temp["name"]:
				find_flag = True
				print("姓名\t年龄\tQQ\t住址")
				print("%s\t%s\t%s\t%s"%(temp["name"],temp["age"],temp["qq"],temp["addr"]))
			else:
				print("你要查找的姓名不存在！")

	elif num == 5:
		print("姓名\t年龄\tQQ\t住址")
		for temp in card_infors:
			print("%s\t%s\t%s\t%s"%(temp["name"],temp["age"],temp["qq"],temp["addr"]))

	elif num == 6:
		print("好的，已退出系统...")
		break
	else:
		print("你输入有误！请重新输入：")
	
	print("")


