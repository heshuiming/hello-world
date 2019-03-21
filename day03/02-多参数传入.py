def dog(*args):
	list_info = list(args)
	#print(list_info)
	print("%s的年龄是%d，性别是%s"%(list_info[0],list_info[1],list_info[2]))

dog('小黄',10,'女')
