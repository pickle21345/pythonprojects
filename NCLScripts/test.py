#!/usr/bin/env python

import sys

def verify(submission):
    processed = [ ]
    if len(submission) % 2 != 0:
        return False

    for i in range(0, len(submission) / 2):
        processed.append(int(submission[i * 2] + submission[(i * 2) + 1], 16))

    ekc = [ 0x53, 75, 0x59, 0x2D, 0110, 0x45, 88, 72, 0x2D, 0x31, 0x39, 0x34, 0x32 ]
    if len(processed) != len(ekc):
        return False

    for i in range(len(processed)):
        if ekc[i] != processed[i]:
            return False

    return True

if len(sys.argv) != 1:
    print "Usage: python bytes.pyc"
    exit(1)

submission = raw_input("What is the password? ")

if verify(submission):
    print "That is correct"
    exit(0)
else:
    print "That is incorrect"
    exit(2)