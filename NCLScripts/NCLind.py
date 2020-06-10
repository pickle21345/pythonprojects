

fileread = open("../Downloads/aws_vpc_flow.log","r")

#text = "QWERTYUIOPASDFGHJKLZXCVBNM"
#ekc = [0110, 69, 88, 72,]

#for char in text:
#	for text in ekc:
#		if (char == chr(text)):
#			print("Letter{} =  {}".format(char,text))


streams = {}
address = {}
count = 0
y = 0 
datatransferred = 0
packetsent = 0

for contents in fileread:
	x = 0 
	Switch = False
	content = []

	data1 = ""


	for char in contents:
		if (x == 0):
			content.append(char)

		elif (char== " "and x!= 1):
			content.append(data1)
			count += 1
			data1= ""

			if (count >11):
				streams[y]= content
				count = 0

			
				if content[3] not in address:
					try:
						address[content[3]] = int(content[9])
					except ValueError:
						#print("Error:{}".format(content[9]))
						pass
				else:
					try:
						fuck = address[content[3]]
						address[content[3]] = int(content[9]) + fuck
					except ValueError:
						pass

				try:
					datatransferred += int(content[9])
					packetsent += int(content[8])
				except ValueError:
					pass
					#print ("N/A:{}".format(content))


			

		elif (x > 1 and x !=" "  ):
			data1+=  char

		

		x += 1
	
	y += 1

one = []

for x in address.keys():
	one.append(address[x])
	if (address[x] == 149825103):
		print (x)
one.sort()
print(one)
