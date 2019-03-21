#1、打印功能提示（增删改查）
print("="*50)
print("="*50)
print("	名字关系管理系统")
print("1.添加一个新的名字")
print("2.删除一个名字")
print("3.修改一个名字")
print("4.查询一个名字")
print("="*50)

names = [] #定义一个空的列表，来存储添加的名字
#2、获取用户的选择
while True:
	num = int(input("请输入功能序号："))

#3、根据用户的选择，执行相应的功能
	if num == 1:  
		name = input("请输入名字：")
		names.append(name)
		print(names)

	elif num == 2:
		#name = input("请输入你要删除的名字：")
		#names.remove(name)
		names.remove(input("请输入你要删除出的名字："))
		print(names)

	elif num == 3:
		print("当前系统里面已有的名字为：%s"%name)
		#i = int(input("请问你要修改第几个？")) #直接输入元素下标
		#names[i-1] = input("输入新的名字:")  #按下标元素提示用户修改
		j = names.index(input("请输入你想要修改的名字：")) #用户输入已有的名字，获取元素下标
		names[j] = input("输入新的名字:")  #按下标元素提示用户修改
		print("修改后的系统列表为：%s"%names)
		
	elif num == 4:
		name1 = input("请输入要查询的名字：")
		if name1 in names:
			print("您要查询的人在系统里面！系统列表为：%s"%names)
		else:
			print("您要查询的人不在系统里面哦！")
	else:
		print("你输入有误！")
		break



