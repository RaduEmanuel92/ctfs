"""
    RSA broken signature scheme.
    Given two signatures, s1 of m1 and s2 of m2, you can forge a signature s1*s2 for m1*m2
    Obtain signatures for small primes, and HOPE
    With 180 primes, you have 4% chance to forge signature for a random challenge
"""
from sympy.ntheory import factorint
from pwn import *
from primesieve import *
import time

n_signatures = 180 # how many signatures we can find in 60 seconds?
small_primes = n_primes(n_signatures)
small_primes_signatures = {}

io = remote('shell2017.picoctf.com', 27465)
#io = process('./smallsign.py')

r = io.recvuntil('Enter a number to sign (-1 to stop): ')
#print r
N = long(r.split('\n')[1].split(' ')[1])
e = long(r.split('\n')[2].split(' ')[1])

def find_signature(m):
    io.sendline(str(m))

    r = io.recvuntil('Enter a number to sign (-1 to stop): ')
    s = long(r.split('\n')[0].split(' ')[1])
    return s

def forge_signature():
    io.sendline('-1')
    r = io.recvuntil('Enter the signature of the challenge: ')
    challenge = int(r.split('\n')[0].split(' ')[1])

    forged = compute_signature(challenge)

    io.sendline(str(forged))
    r = io.recvline()
    print r

def compute_signature(challenge):
    factors = factorint(challenge)
    print factors

    begin = time.time()
    for k in factors.keys():
        if k not in small_primes:
            print "Tough luck my friend, try again"
            exit(0)
    end = time.time()
    print 'verifying challenge factors took: %s' % (end-begin)
    
    begin = time.time()
    forged = 1
    for k, v in factors.items():
        forged = forged * (small_primes_signatures[k] ** v) % N
    end = time.time()
    print 'forgin signature took: %s' % (end-begin)
    return forged


def build_signatures_dictionary():
    for i in small_primes:
        #print "obtaining signature for: %s" % i
        s = find_signature(i)
        small_primes_signatures[i] = s

begin = time.time()
build_signatures_dictionary()
end = time.time()
print "Building dictionary took: %s" % (end-begin)

forge_signature()
