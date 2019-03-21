def cat(**param):
	for value in param:
		print(param[value])
	#print("%s的年龄是%d"%(param['name'],param['age']))

cat(name='laowang',age=18)
