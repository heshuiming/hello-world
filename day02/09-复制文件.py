'''
1、获取想要复制的文件名 input（）
2、打开这个文件
3、创建一个文件 xxx[复件].txt
4、从原文件中读取数据
5、将读取的数据写入到新文件中
6、关闭两个文件
'''

file_name = input("请输入你要复制的文件名:")

f1 = open(file_name,"r")  #打开这个文件
#新建复件文件
#字符串截取的方式获取新文件名（不太合适）
#copy_file_name = file_name.split(".")[0]+'[复件].'+file_name.split(".")[1]

position = file_name.rfind(".")
copy_file_name = file_name[:position] + "[复件]" + file_name[position:]

f2 = open(copy_file_name,"w")
#从原文件中读取数据
#result = f1.read()

#把读取的数据写入到新文件中
#f2.write(f1.read())
while True:
	content = f1.read()
	if len(content) == 0:
		break

	f2.write(content)


#关闭两个文件
f1.close()
f2.close()
