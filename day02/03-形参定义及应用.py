#计算多个数的和
def sum_num(a,b,*args):
	result = a+b
	sum = 0
	for i in range(0,len(args)):
		sum = sum + args[i]
	result = result + sum
	#result = a+b
	print("result=%d"%result)

sum_num(11,2,1,1,1,1,1,1,1)
