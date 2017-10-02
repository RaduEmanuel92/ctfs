#!/usr/bin/env python
import sys
from ctypes import *
import struct
import io
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import multiprocessing as mp
import optparse
import string
import random


# by default pass_file is 
# pfile = "/usr/share/wordlists/rockyou.txt"
BLOCK_SIZE = 16  # 16 Bytes AES ECB mode block size

def str2bin(ss):
  """
    Transform a string (e.g. 'Hello') into a string of bits
  """
  bs = ''
  for c in ss:
    bs = bs + bin(ord(c))[2:].zfill(8)
  return bs

def str2int(ss):
  """
    Transform a string (e.g. 'Hello') into a (long) integer by converting
    first to a bistream
  """
  bs = str2bin(ss)
  li = int(bs, 2)
  return li


class BinaryHeader(BigEndianStructure):
    _fields_ = [
                ("magic", ARRAY(c_char, 4)),
                ("payload_size", c_uint32),
                ("header_md5", ARRAY(c_ubyte, 8)),
                ("etl", ARRAY(c_uint8, 7)), # always zero
                ("unused_1", c_char),
                ("password_len", c_uint16),
                ("padding_len", c_uint16),
                ("unused_2", ARRAY(c_ubyte, 4)),
                ("plaintext_md5", ARRAY(c_ubyte, 16))
                ]          



#pad and unpad methods for computing 16 byte sized blocks
#required for ECB encry mode

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

class AESCipher:
    """
    	Simple AES  ECB mode implementation
    """

    def __init__(self, key):
        self.key = md5(key).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        #enc = pad(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc))

def bruteforce(passwd, ct):
	'''
		Worker function which attempts to BF
		first block of give enc file
		BF sucessful if decrypted block lends
		the header of a .tgz file
	'''

	result = (AESCipher(passwd).decrypt(ciphertext).encode('hex'))[:6]

	#print "Check {0}".format(result)
	#gzip_header = '1f8b08'  i.e. magic + deflate
	
	if result == gzip_header: 
		print "Candidate password : {0}".format(passwd)
		decrypt_file = md5(AESCipher(passwd).decrypt(ct)).hexdigest()
		print decrypt_file

		if decrypt_file == found_pt_md5:
			print "Password found: {0}".format(passwd)
			exit(0)


def main():
	pfile       = "/usr/share/wordlists/rockyou.txt"
	global gzip_header 
	gzip_header = '1f8b08' # magic + deflate apYBg
	global ciphertext, found_pt_md5
	
	parser = optparse.OptionParser("usage%prog" +\
                    "-p <password_list>")
	parser.add_option( "-p", dest="plist", type="string", \
                    help="specify password list")
	(options, args) = parser.parse_args()
	if (options.plist == None):
		print parser.usage
		pfile       = "/usr/share/wordlists/rockyou.txt"
	else:
		pfile = options.plist

    #1. Extracting the hash of the plaintext(e84.g. the decrypted file)

	config_file = open('conf.bin', 'rb') 
	t0 = config_file.read(4)
	t9 = config_file.read(4)
	print "[+] Length of ciphertext(payload size) leaked: {0}".format(str2int(t9))
	t1 = config_file.read(8)
	t2 = config_file.read(7)
	t3 = config_file.read(1)
	t4 = config_file.read(2)
	
	t5 = config_file.read(2)
	t6 = config_file.read(4)
	t7 = config_file.read(16)


	ciphertext = config_file.read(16)
	rest_cfg = config_file.read()

	total_ct = ciphertext + rest_cfg
	total_ct_len = len(total_ct) 
	print "[+] Validity of CT lenght leak returned: {0}".format(True if str2int(t9) == total_ct_len else False)

	print "[+] Password length leaked: {0}".format(str2int(t4))
	print "[+] Found md5 for plaintext from header:"
	print 	t7.encode('hex')
	
	found_pt_md5 = t1
	#_md5 	= '626147c3d43baf2f9300bcafadf45c8c'
	#print '[+] Ciphertext chunk for AES block ATK:'
	#print ciphertext



	#2. Attempting to decrypt first AES block; check for md5 signature validity

	N_CPU   = 2
	N       = 64
	#pool    = mp.Pool(N_CPU)


	print "[+] Starting BF session..."
	
	for letter1 in (string.ascii_letters + string.digits):
			for letter2 in (string.ascii_letters + string.digits):
				for letter3 in (string.ascii_letters + string.digits):
					for letter4 in (string.ascii_letters + string.digits):
						for letter5 in (string.ascii_letters + string.digits):
							try_passwd = letter1 + letter2 + letter3 + letter4 + letter5
							bruteforce(try_passwd, total_ct)

		
	config_file.close()


    	'''
    	while True: 
			passwd = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(pass_len))
			bruteforce(passwd)


		with open(pfile) as passfile:	
        pool.imap_unordered(bruteforce, (password for password in passfile))
        pool.close()
        pool.join()
    	''' 
        

	#3. Play: Constructing a .tgz file
	obj = BinaryHeader()
	fout = open('test.bin', 'wb')
	
	obj.magic 			= '1f8b'.decode('hex')            
	obj.payload_size 	= 0x20
	headmd5 			= '04eb443b'.decode('hex')
	obj.header_md5 		= (c_ubyte * 8)(*[c_ubyte(ord(c)) for c in headmd5])
	obj.etl				= (c_ubyte * 7)(*[c_ubyte(0)])
	obj.unused_1 = 'A'  
	obj.password_len 	= 0xf
	obj.padding_len 	= 0xf
	obj.unused_2 		= (c_ubyte * 4)(*[c_ubyte(ord('A'))])
	obj.plaintext_md5 	= (c_ubyte * 16)(*[c_ubyte(ord('A'))])      
	
	fout.write(obj)
	fout.close()


if __name__ == '__main__':
	main()

