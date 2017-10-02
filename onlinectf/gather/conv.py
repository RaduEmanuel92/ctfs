#!/usr/bin/env python

import binascii
import sys

def bin2str(bs):

  n = int(bs, 2)
  return binascii.unhexlify('%x' % n)

def string_decode(input, length=8):
    input_l = [input[i:i+length] for i in range(0,len(input),length)]
    return ''.join([chr(int(c,base=2)) for c in input_l])
     
num = ''
suma = 0
with open('b.txt') as f:
	
  while True:
    letter = f.read(1)
    if not letter:
      #print "EOF"
      break
    
    if letter.isdigit() == False:
      num = ''
    else:
        while(letter.isdigit() == True) :
          num   =  num + letter
          letter = f.read(1)
        print num
        suma += int(num)

print 'Total sum: {0}'.format(suma)
 
        
     


  #for char in f :
    #content = char
    #sys.stdout.write((bin(int(content))).lstrip('0b'))
    #content = bin(int(content)).lstrip('0b')

#print bin2str(content[0])
#print content[0]
#print content[1]
#print bin2str(content[0])
#print string_decode(content[1])
#print bin2str(content[3])
#for strg in content:
#  sys.stdout.write(string_decode(strg))
    