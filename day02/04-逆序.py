# 递归去字符
l = '1234'

def revert(x):
	if x == -1:
		return []
	return [l[x]] + revert(x-1) # 每次生成新的列表

result = revert(len(l)-1)
print(result)
