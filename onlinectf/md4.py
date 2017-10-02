#!/usr/bin/env pyhton

import hashlib 
import multiprocessing as mp

hashes = [
			'd3aabca693b6abb2bea3bfb6fdb0bcbe',
			'9be2f4eedbfee3faf6ebf7feb5f8f4f6',
			'255c4a5065405d44485549400b464a48',
			'f881978db89d80999588949dd69b9795',
			'eb92849eab8e938a869b878ec5888486',
			'2e57415b6e4b564f435e424b004d4143',
			'0871677d486d70696578646d266b6765',
			'60190f15200518010d100c054e030f0d'
		]	


username 	= "admin"
pfile       = "/usr/share/wordlists/rockyou.txt"
N_CPU 		= 2


def md4checker(password):
	md4_passwd =  hashlib.new('md4', password.encode('utf-8')).hexdigest().lower()
	md4_passwd = md4_passwd + username
	final_hash = hashlib.new('md4', md4_passwd.encode('utf-8')).hexdigest().lower()
	if final_hash  in hashes:
		print "[+] Pass found: {0}".format(password)
		return 1


def main():
	pool = mp.Pool(N_CPU)

	with open(pfile) as passfile:
		for passwd in passfile:
			semaphore 	= 0
			print "Try {0}".format(passwd)
			try:
			 	enc = passwd.encode('utf-8')
			except Exception, e:
			 	pass
			else:
			 	semaphore = md4checker(passwd)
			finally:
			 	if semaphore is 1:
			 		break
			

if __name__ == '__main__':
			main()		
