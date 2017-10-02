"""
    Hash Chain authentication.
    Exploit the fact that the seed is the hash of the ID.
"""

from pwn import *
import md5
import time

io = remote('shell2017.picoctf.com', 57048)

r = io.recvuntil('r/f?')
#print r

io.sendline('f')

r = io.recvline()
r = io.recvline()
r = io.recvline()
print r
user_id = r.split(' ')[5].replace('\n', '')
print "id: %s <---" % user_id

r = io.recvline()

r = io.recvline()
hash_digest = r.replace('\n', '')
print "stop_hash is: %s <---" % hash_digest

r = io.recvline()
print r

def authenticate(seed, stop_hash):
	hashc = seed
	while hashc != stop_hash:
  		print hashc
		previous = hashc
  		hashc = md5.new(previous).hexdigest()
 
	return previous

# this is really insecure
seed = md5.new(user_id).hexdigest()

result = authenticate(seed, hash_digest)
io.sendline(result)

r = io.recvline()
print r 
