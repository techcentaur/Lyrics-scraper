#this file have all the dataset of the program
#we will access it while training and testing

first_w=['a']
love_w1=['heart','care','happiness','forever','romance','sweet','kiss','love','hugs','kiss','sex']
love_w2=[]
love_w3=[]
love_w4=[]

def print_dataset():
	print("printing data-set for single words occuring mostly in love songs \n")
	for i in love_w1:
		print(i+" ")
	print("\n")
	print("printing data-set for double words occuring mostly in love songs \n")
	for i in love_w2:
		print(i+" ")
	print("\n")
	print("printing data-set for triple words occuring mostly in love songs \n")
	for i in love_w3:
		print(i+" ")
	print("\n")
	print("printing data-set for quadraple words occuring mostly in love songs \n")
	for i in love_w4:
		print(i + " ")
	print("\n")