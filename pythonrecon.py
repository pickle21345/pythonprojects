#!/usr/bin/env python3

import sys
import subprocess


#take ip address from 
try:
	address = str(sys.argv[1])
except:
	print("Example: Python3 pythonrecon.py #.#.#.#")
nmap = "sudo nmap {} -sC -sV > nmapresults.txt".format(address)
smbclient = "smbclient -L \\\\\\\\{} > smbclient.txt".format(address)
smbmap = "smbmap -H \\\\\\\\{} > smbmap.txt".format(address)
gobuster = "gobuster -u {} -w directory-list-2.3-medium.txt > gobuster.txt".format(address)
nikto = "nikto -h http://{}/".format(address)
commands = []

def services():
	nmapresults = subprocess.check_output(nmap,shell=True)
	ports  = open("nmapresults.txt",'r')
	portdefs = ["80/tcp","139/tcp","135/tcp","445/tcp"]
	try:
		for line in ports:
			if "80/tcp" in line:
				print("WebServer Enumeration Available")
				commands.append(gobuster)
				commands.append(nikto)
			if "135/tcp" in line:
				print("Samba Enumeration Available")
				commands.append(smbmap)
				commands.append(smbclient)
				return 
			if "139/tcp" in line:
				print("Samba Enumeration Available")
				commands.append(smbmap)
				commands.append(smbclient)
				return
			if "445/tcp" in line:
				print("Samba Enumeration Available")
				commands.append(smbmap)
				commands.append(smbclient)
				return
	finally: 
		ports.close()
		return


services()

for command in commands:
	try:
		subprocess.check_output(command, shell=True)
	except:
		print("Error Service not Available")


