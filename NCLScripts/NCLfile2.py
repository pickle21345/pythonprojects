import re

fileread = open("../Downloads/badge (1).log","r")
employees = []
employeedict = {}

fileread1 = open("../Downloads/access.log","r")
employees1 = []


for contents in fileread:

	employee = ""
	timestamp = ""
	time = []

	
	y = 0
	x = 0
	
	acceptable = 1000
	acceptable2 = 1000

	for char in contents:

		if (x < 19):
			timestamp += char

		elif(char == '['):
			acceptable = x

		elif(char == ']'):
			acceptable2 = x
			
		elif ( x > (acceptable2 + 6) ):

			if (char == "I"):
				if employee not in employees:
					employees.append(employee)
					time.append(timestamp)
					employeedict[employee] = [1,0,1,time]
				
					
				elif employeedict[employee][2] == 0:
					time.append(timestamp)
					employeedict[employee][2] = 1	
					employeedict[employee][0] += 1
					employeedict[employee][3].append(timestamp)
				

				else:
					print("\n Access Error In {}".format(employee))

			elif (char == "O"):
				if employee not in employees:
					print('\nERROR{}'.format(employee))
					time.append(timestamp)
					employees.append(employee)
					employeedict[employee] = [0,1,0]

				elif employeedict[employee][2] == 1:
					time.append(timestamp)
					employeedict[employee][2] = 0
					employeedict[employee][1] += 1
					employeedict[employee][3].append(timestamp)

				else:
					print("\n Access Error Outside{}".format(employee))	

		
		elif (x > acceptable and x < acceptable2):
			employee += char

		x += 1

#List of Addresses
lazyboy = []

for contents in fileread1:

	employee = ""
	address = ""
	timestamp = ""
	acceptable = 1000
	x = 0
	acceptable2 = 1000
	acceptable3 = 1000
	
	for char in contents:

		if (x < 19):
			timestamp += char

		
		if (char == '['):
			acceptable = x
		elif (char == ']'):
			acceptable2= x
			if employee not in employees1:
				employees1.append(employee)

				try:
					if (timestamp > employeedict[employee][3][0] and timestamp < employeedict[employee][3][1]):
						pass
					elif(timestamp > employeedict[employee][3][2] and timestamp < employeedict[employee][3][3]):
						pass
					elif(timestamp > employeedict[employee][3][4] and timestamp < employeedict [employee][3][5]):
						pass
					elif(timestamp > employeedict[employee][3][6]and timestamp < employeedict [employee][3][7]):
						pass
					elif(timestamp > employeedict[employee][3][8] and timestamp < employeedict [employee][3][9]):
						pass
					elif (timestamp > employeedict[employee][3][10] and timestamp < employeedict [employee][3][11]):
						pass
					elif(timestamp > employeedict[employee][3][12]and timestamp < employeedict[employee][3][13]):
						pass
					elif (timestamp > employeedict[employee][3][14] and timestamp < employeedict [employee][3][15]):
						pass
					elif(timestamp > employeedict[employee][3][16]and timestamp < employeedict[employee][3][17]):
						pass
					elif (timestamp > employeedict[employee][3][18] and timestamp < employeedict [employee][3][19]):
						pass
					elif(timestamp > employeedict[employee][3][20]and timestamp < employeedict[employee][3][21]):	
						pass
					elif (timestamp > employeedict[employee][3][22] and timestamp < employeedict [employee][3][23]):
						pass
					elif(timestamp > employeedict[employee][3][24]and timestamp < employeedict[employee][3][25]):
						pass
					elif(timestamp > employeedict[employee][3][26] and timestamp < employeedict[employee][3][27]):
						pass
					else:
						print(employee + timestamp)
				except IndexError:
					pass
				#break
			else:
				try:
					if (timestamp > employeedict[employee][3][0] and timestamp < employeedict[employee][3][1]):
						pass
					elif(timestamp > employeedict[employee][3][2] and timestamp < employeedict[employee][3][3]):
						pass
					elif(timestamp > employeedict[employee][3][4] and timestamp < employeedict [employee][3][5]):
						pass
					elif(timestamp > employeedict[employee][3][6]and timestamp < employeedict [employee][3][7]):
						pass
					elif(timestamp > employeedict[employee][3][8] and timestamp < employeedict [employee][3][9]):
						pass
					elif (timestamp > employeedict[employee][3][10] and timestamp < employeedict [employee][3][11]):
						pass
					elif(timestamp > employeedict[employee][3][12]and timestamp < employeedict[employee][3][13]):
						pass
					elif (timestamp > employeedict[employee][3][14] and timestamp < employeedict [employee][3][15]):
						pass
					elif(timestamp > employeedict[employee][3][16]and timestamp < employeedict[employee][3][17]):
						pass
					elif (timestamp > employeedict[employee][3][18] and timestamp < employeedict [employee][3][19]):
						pass
					elif(timestamp > employeedict[employee][3][20]and timestamp < employeedict[employee][3][21]):	
						pass
					elif (timestamp > employeedict[employee][3][22] and timestamp < employeedict [employee][3][23]):
						pass
					elif(timestamp > employeedict[employee][3][24]and timestamp < employeedict[employee][3][25]):
						pass
					elif(timestamp > employeedict[employee][3][26] and timestamp < employeedict[employee][3][27]):
						pass
					elif(timestamp > employeedict[employee][3][28]and timestamp < employeedict[employee][3][29]):	
						pass
					elif (timestamp > employeedict[employee][3][30] and timestamp < employeedict [employee][3][31]):
						pass
					elif(timestamp > employeedict[employee][3][32]and timestamp < employeedict[employee][3][33]):
						pass
					elif(timestamp > employeedict[employee][3][34] and timestamp < employeedict[employee][3][35]):
						pass
					else:
						print(employee + timestamp)
				except IndexError:
					pass
		elif (char in "Access" and x > acceptable2):
			acceptable3 = x
		elif (x > acceptable3):
			address += char
			if char is '-':
				if address not in lazyboy:
					lazyboy.append(address)
				else:
					print("Error {}".format(address))
		elif (x > acceptable):
			employee += char

		x += 1 

for employee in employees1:
	if employee not in employees:
		print("\nFake employee: {}".format(employee))

