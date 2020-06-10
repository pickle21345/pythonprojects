import subprocess

fileread = open("/media/oscar/123E0F1A3824CA13/target.txt","r")




for guess in fileread:

	
	cmd = ["./../Downloads/root-x64", "6ed0181eab9486efb897b028870071db"]

	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate(guess)
	if "Nope" in output:
		print ("not working")
	else:
		print("This is it {}".format(guess))
		break




