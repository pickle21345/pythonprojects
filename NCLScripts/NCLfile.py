import re

#read file 
#open file

#count swipe in 
#Names no duplicates 
#count swipe out 

fileread = open("../Downloads/access.log","r")
employees = []


for contents in fileread:

	employee = ""

	x = 0
	count = 1000
	xcount = 0   
	acceptable = 100

	for char in contents:

		
		if(char == "-" and x > 40):
			acceptable = x

		elif (char == "K" and x > 40):

			employees.append(int(employee))
			break 

		elif (x > acceptable):
			employee += char

		x += 1


print(max(employees))


#21 character read 
#add to list 
#if inside list delete 
#print list