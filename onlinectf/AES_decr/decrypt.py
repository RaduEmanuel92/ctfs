#!/usr/bin/env python

import base64

from Crypto import Random
from Crypto.Cipher import AES
import hashlib

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]


ciphertext = 'iAtAMcPHECemSHRwfQiXlBcssGfJMHi2mvgff4Pz/e6SbUOAq09DZiLJhxXX4oWm'
key1 		= 'mysecretpassword'

class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
		#extract the IV
		#self.key 	 = hashlib.sha256(key.encode('utf-8')).digest()
		#enc 		 = pad(enc)
		b64dec    		 = base64.b64decode(ciphertext)
		IV 	   	  	 = b64dec[0:AES.block_size]
		enc 		 = b64dec[AES.block_size:]
		
		AES_instance = AES.new( self.key, AES.MODE_CBC, IV )
		pt 		  	 = AES_instance.decrypt(enc)
		return pt

def main():
	instance = AESCipher(key1)

	plaintxt = "Mama are mere."
	print instance.encrypt(plaintxt)
	print instance.decrypt(plaintxt)
	print instance.decrypt(ciphertext)

if __name__ == '__main__':
	main()