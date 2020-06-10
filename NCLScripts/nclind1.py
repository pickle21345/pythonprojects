fileread = open("../Downloads/transfer_log.json","r")

totalBytes = []
totalSession = []

for contents in fileread:
	x = 0
	limit = 1000
	limit1 = 1000
	byte = ""
	sessionID = ""

	for char in contents:
		if (char == "d"):
			limit1 = x + 2
		elif (x > limit1):
			if (char == ','):
				limit1 = 1000
			else:
				sessionID += char
		elif (char == "b"):
			limit = x + 6
		elif (x > limit and char != "}"):
			byte += char
		elif (char == "}"):
			totalBytes.append(int(byte))

			if sessionID not in totalSession:
				totalSession.append(int(sessionID))
			else:
				print("!!!!!!")
		x += 1

print(len(totalBytes))
print(len(totalSession))
