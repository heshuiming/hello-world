import random
pool = {}
while 1:
	user_input_content = input("please input No and name,sep by ,:")
	if user_input_content.lower() == "done":break
	no,name = user_input_content.split(",")
	pool[no] = name
print (pool)

while 1:
	try:
		lotte_times=int(input("please input lotter times:"))
	except:
		print ("please input a int number bigger than 0,try again.")
		continue
	if lotte_times>0:
		break
	else:
		print ("please input a int number bigger than 0,try again.")
print ("lotte times:",lotte_times)

result={}
for i in range(lotte_times):
	r = random.choice(list(pool.keys()))
	result[r] = pool[r]
	del pool[r]

print (result.values())
