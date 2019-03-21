import os

#1、获取文件夹名称
folder_name = input("请输入要批量操作的文件夹：")

files = os.listdir("test")
print(files)

os.chdir("./test")
for file_name in files:
#	os.chdir("./test")
	new_name = os.rename(file_name,"hehe-"+file_name)

print(new_name)
