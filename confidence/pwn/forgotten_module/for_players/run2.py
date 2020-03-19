#!/usr/bin/python3 -u
import subprocess
import random 
import string
from subprocess import PIPE, Popen
from pwn import *


def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def compute_key(iv):
    bits = 25
    cmd = "hashcash -mb{bits} {iv}"
    p =  Popen(["hashcash", f"-mb{bits}", iv],stdin=PIPE, stdout=PIPE, stderr=PIPE) 
    output, err = p.communicate()
    return output

def main():
    conn = remote('forgotten-module.zajebistyc.tf', 31002)
    #iv = random_string(10)
    #iv =  str(conn.readline())
    #iv = str(conn.readline()).split(' ')[2][0:-3]
    iv =  conn.recvuntil("Solution:", timeout=2, drop=True)
    iv = str(iv).split(' ')[2][0:-3] 
    print(iv)
    key = str(compute_key(iv))[2:-3]
    print(key)
    #conn.recvuntil("Solution:", timeout=2, drop=True)
    conn.send(key)
    conn.recvuntil("bytes:", timeout=2, drop=False)
    conn.send("0")
    
    #conn.recvline()

    #conn.interactive()


if __name__ == "__main__":
    main()


