#/usr/bin/env python

import sys
import subprocess
import string


global key , t, i, msg2
key = "CENSORED"
i 	= 0
t   = 0

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(i=0,t=0)
def verify(p, key,letter):
	#print "------------------"
	t1 = ord(p)
	#print t1
	t2 = ord(key[verify.i % len(key)])
	#print t2
	c = (t1 + (t2 ^ verify.t) + (verify.i)*(verify.i)) & 0xff
	if (c == ord(letter)):
		verify.t = t1
		verify.i += 1
		sys.stdout.write(chr(c))
		return 1 
	#print "------------------"


def main():

	input_msg1 	= open('msg001', 'r')
	enc_msg1 	= open('test', 'rb')
	input_msg2 	= open('msg002.enc', 'r')
	msg1 		= input_msg1.read()
	msg2 		= input_msg2.read()
	msg1_enc	= enc_msg1.read()	

	msg2_list = [ord(b) for b in msg2]
	msg1_list = [ord(b) for b in msg1]
	enc1_list = [ord(b) for b in msg1_enc]


	key = "CENSORED"
	c = 0
	t = 0
	i = 0
	
	print "Encrypted \"{0}\" is: ".format(msg1)
	for letter in msg1 : 
		c = (ord(letter) + (ord(key[i % len(key)]) ^ t) + i*i) & 0xff
		t = ord(letter)
		i += 1
		sys.stdout.write(chr(c))

	#for index in range(len(msg2)):
	#	sys.stdout.write(str(ord(msg2[index])) + ' ')
	#print "\n\n[+] Attempting to decrypt msg001.enc of len {0}".format(len(msg1_list))
	index = 0
	c = 0
	t = 0
	i = 0
	for letter1 in enc1_list:
		p = letter1 - ((ord(key[i % len(key)]) ^ t) + i*i)
		t = p
		i += 1
		if (p>0 and p <255):
			#print '\n----------'
			#print p
			sys.stdout.write(chr(p))

		elif (p<0 and p > -255 ):
			#print '\n----------'
			#print p
			p = 255 + p + 1
			t = p 
			sys.stdout.write(chr(p))
		elif(p >256):
			#print '\n----------'
			#print p
			p = p - 256
			t = p
			sys.stdout.write(chr(p))
		else:
			#print '\n'
			#print p, " "
			p = (256 - (abs(p) & 0xff))
			t = p
			sys.stdout.write(chr(p))		
	
	#print "\n\n[+] Attempting to decrypt msg002.enc of len {0}".format(len(msg1_list))
	index = 0
	c = 0
	t = 0
	i = 0
	for letter1 in msg2_list:
		p = letter1 - ((ord(key[i % len(key)]) ^ t) + i*i)
		t = p
		i += 1
		if (p>0 and p <256):
			#print '\n----------'
			#print p
			sys.stdout.write(chr(p))

		elif (p<0 and p >= -256 ):
			#print '\n----------'
			#print p
			p = 255 + p + 1
			t = p 
			sys.stdout.write(chr(p))
		elif(p >256):
			#print '\n----------'
			#print p
			p = p - 256
			t = p
			sys.stdout.write(chr(p))
		else:
			#print '\n'
			#print p, " "
			catch = p
			p = (256 - (abs(p) & 0xff))
			t = p
			try :
				sys.stdout.write(chr(p))
			except Exception, e:
				sys.stdout.write(chr(0))
				t = 0
			else:
				pass
			finally:
				pass 

	'''
	for letter1 in msg1_enc:
		for letter2 in (string.printable):
			c = chr((ord(letter2) + (ord(key[i % len(key)]) ^ t) + i*i) & 0xff)
			if (c == letter1):
				t = ord(letter2)
				i += 1
				sys.stdout.write(letter2)

			else:
			print '\n----------'
			print p
			p = abs(-p -512)
			t = p
			sys.stdout.write(chr(p))
			
			# 397 -> s
			# 396 -> t
	'''


if __name__ == '__main__':
	main()
