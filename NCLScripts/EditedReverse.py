#!/usr/bin/env python

import sys
import math
import re

def verify(guess,characters):
  
  vals = [ 
    130,
    154,
    136,
    252,
    131,
    157,
    155,
    137,
    252,
    233,
    224,
    232,
    227
  ] 

    # i is an integer regular 
    # C is the character of a string. ord converts it to represent the unicode

  if (ord(guess) ^ 209) != vals[characters]:
    return False 
  return True



if len(sys.argv) != 1:
  print 'Usage: python check.pyc'
  exit(1)


characters = re.escape("1234567890-=qwertyuiop[]asdfgh\\jkl;'zxcvbnm,./`~!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCV}BNM{|:<>?")
answer = ""
characters = 0
while True:
  for char in characters:
    if(verify(char,characters) == True):
      answer += char
      characters += 1
      print(answer)
    else:
      pass
    
      



