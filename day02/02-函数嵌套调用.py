#键盘输入三个数，求三个数的和，再求平均值
#定义一个函数,求和
def sum(a, b, c):
	result = a + b + c
	#print("三个数的和为：%d"%result)
	return result
	
#定义一个函数求平均值
def average(a1, b1, c1):
	result = sum(a1, b1, c1)
	result /= 3
	print("三个数的平均值为：%d"%result)

#1、键盘输入三个数
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))

#sum(num1, num2, num3)
average(num1, num2, num3)
