#!/usr/bin/env python
from base64 import b64encode as be
from base64 import b64decode as de
import string
#from secret import msg, KEY

#msg and KEY are meaningful english sentences in l33t
#msg2 = msg.replace('_','')
#KEY = KEY.replace('_','')
#msg2 	= 'n00bCTFenevergoingtoguessthept'
#KEY 	= '1234567'

#assert  (len(KEY)==7) and KEY.isalnum() and msg2.isalnum()
#assert 'n00bCTF' in msg2

def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))

def encryption(msg, key):
	return be(XOR(msg, KEY))

def print_flag(msg):
	print 'CTF{%s}' % msg

if __name__ == '__main__':
	#print encryption(msg2, KEY)					
	#Decrypt msg2 to get the flag
	#print_flag(msg2)

	'''
	Hint:XOR(XOR(text,key),text) = key.
	cipher = b64encode(XOR(msg2,key))
	'''
	
	crib 	= 'n00bCTF'
	ct		= 'DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa'
	ct = de(ct)

	keys = []
	for index in range(len(ct)):
		key =  XOR(crib, ct[index:index+7])
		if key.isalnum() == True:
			print "[+] Key candidate: {}".format(key)
			keys.append(key)

	print "\n"
	counter = 1
	for key in keys:
		
		print "[+] Attempt #{0} to decrypt CT: ".format(counter)
		print XOR(ct, key)
		counter += 1	
		print "\n"	
		

