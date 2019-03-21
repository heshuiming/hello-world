#-*- conding:utf-8 -*-
i = 1 
while  i <= 9:
	j = 1
	while j <= i:
		sum = i*j
		print(str(j) + "*" + str(i) + "=" + str(sum)),
		j += 1
	print("")
	i += 1