#!/usr/bin/env python

import binascii
import sys


def bin2str(bs):

  n = int(bs, 2)
  return binascii.unhexlify('%x' % n)

def bin2str(bs):
  """
    Transform a binary srting into an ASCII string
  """
  n = int(bs, 2)
  return binascii.unhexlify('%x' % n)

def byte2bin(bval):
  """
    Transform a byte (8-bit) value into a bitstring
  """
  return bin(bval)[2:].zfill(8) 

def str2bin(ss):
  """
    Transform a string (e.g. 'Hello') into a string of bits
  """
  bs = ''
  for c in ss:
    bs = bs + bin(ord(c))[2:].zfill(8)
  return bs


def bin2hex(bs):
  """
    Transform a bit string into a hex string
  """
  return hex(int(bs,2))[2:-1]
 
def hexxor(a, b): # xor two hex strings (trims the longer input)
  ha = a.decode('hex')
  hb = b.decode('hex')
  return "".join([chr(ord(x) ^ ord(y)).encode('hex') for (x, y) in zip(ha, hb)])

def bitxor(a, b): # xor two bit strings (trims the longer input)
  return "".join([str(int(x)^int(y)) for (x, y) in zip(a, b)])

def strxor(a, b): # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

with open('conf.bin') as f:
	content = f.readlines()
	data = [x for x in content]
	print "Data has {0} strings".format(len(data))
	for i in range(len(data)):
		for string in data:
			print strxor(data[i], string)




'''
		#count = 0
	for x in data:
		if x.isalpha(): 
			sys.stdout.write(x)
			count +=1
		  	if count % 24 == 0:
		  		sys.stdout.write('\n')
'''