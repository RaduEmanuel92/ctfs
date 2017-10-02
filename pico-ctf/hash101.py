#!/usr/bin/python
import struct
import socket
import telnetlib

def readuntil(f, delim='> '):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def p(v):
    return struct.pack('<Q', v)

def u(v):
    return struct.unpack('<Q', v)[0]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('shell2017.picoctf.com', 9661))
f = s.makefile('rw', bufsize=0)

readuntil(f, 'of ')
num = int(readuntil(f, '\n'), 2)
payload = hex(num)[2:].decode('hex')
f.write(payload + "\n")
print num
print payload
readuntil(f, 'equivalent')
#f.write(payload + "\n")
f.write(hex(num)[2:] + "\n")
f.write(str(num) + "\n")
print hex(num)
print str(num)
text = readuntil(f, "example hashing function").split(' ')
hsh = text[text.index('transformed') - 3]
payload = chr(ord('a') - 1 + int(hsh))
print hsh
print int(hsh)
print payload
f.write(payload + '\n')

t = telnetlib.Telnet()
t.sock = s
t.interact()

