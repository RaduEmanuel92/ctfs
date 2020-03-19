import random, time
import string
import base64
import os
from pwn import *


def get_data(conn, token):
    return conn.recvuntil(token, timeout=2, drop=True)


def otp(a, b):
	r = ""
	for i, j in zip(a, b):
		r += chr(ord(i) ^ ord(j))
	return r


def return_cand(xor):
    for letter1 in string.ascii_letters:
        for letter2 in string.ascii_letters:
            if otp(letter1, letter2) == xor:
                return letter1


def main():
    conn = remote('misc.2020.chall.actf.co', 20301)
    conn.recvuntil("> ", timeout=1, drop=True)
    while True:
        conn.sendline("2")
        xor_b64 = conn.recvuntil("answer: ", timeout=1, drop=True)    
        xorb = xor_b64.split('\n')[0]
        #print xorb
        if (len(xorb) == 4) and xorb[-2] == '=' :
            xor_ascii = base64.b64decode(xorb)
            print "Finding cand for {} (ASCII: {} )".format(xorb, xor_ascii)
            cand = return_cand(xor_ascii)
            print "Chosen cand: {}".format(cand)
            conn.sendline(cand)
            print conn.recvline()
        else:
            conn.sendline("2")
            conn.recvuntil("> ", timeout=1, drop=True)    
            continue 

if __name__ == "__main__":
    main()       