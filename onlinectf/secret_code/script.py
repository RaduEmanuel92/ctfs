#!/usr/bin/python

import sys
ok = 0

with open('c.txt') as file:
	while True:
		char = file.read(1)
		if not char:
			exit(1)
		else:	
			#char = ord(char) ^ ord('X')
			if char == '-' or char == '.':
				sys.stdout.write(char)
				ok = 0
			else:
				if ok == 0 :
				 	sys.stdout.write(' ')
				 	ok = 1