import csv

def get_data(file_path):
	data = csv.reader(open(file_path,'r'))
	for user in data:
		print(user[0])


get_data("")
