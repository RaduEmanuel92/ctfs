# Import everything in the pwntools namespace
from pwn import *
import math

def get_data(conn, token):
    return conn.recvuntil(token, timeout=2, drop=True)


def gen_solution(b,a,p):
    t2 = b % p
    print "factor2: {}".format(t2)
    t1 = a 
    for x in range(1,100000000):
        
        if t1 == t2:
           return x

        t1 = pow(a,t1)
       
    return None       


s1 = "crypto.2020.chall.actf.co"
s2 = "3.228.7.55"

conn = remote(s1, 20603)

while True:
    
    data = conn.recvuntil("x: ", timeout=2, drop=True)    
    
    print data
    if len(data.split("\n")) > 1:
        data = data.split("\n")

        b = int(data[-2].split(' ')[2])
        a = int(data[-3].split(' ')[2])
        p = int(data[-4].split(' ')[2])
        
        print "b = {} \na = {} \np = {} \n".format(str(b), str(a), str(p))
        print "Gen solution"
        x = gen_solution(b,a,p)
        print x
        conn.sendline(str(x))
        print conn.recv()
        #conn.recv()
    else:
        print "[-] Time to go out"
        break

    #conn.interactive()
