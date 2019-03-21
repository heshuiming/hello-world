f = open("test1.txt","r")
list = f.read()
for str in list:
	print(str,end="")
print("")
f.close()
