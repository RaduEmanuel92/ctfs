#!/usr/bin/python2 -u
from hashlib import sha256
from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
from subprocess import check_output, STDOUT, CalledProcessError

BLOCK_SIZE = 16
R = Random.new()

with open("parameters.txt") as f:
    p = int(f.readline().strip())
    g = int(f.readline().strip())

#password = open("password.txt").read()

def pad(m):
    o = BLOCK_SIZE - len(m) % BLOCK_SIZE
    return m + o * chr(o)

def unpad(p):
    return p[0:-ord(p[-1])]

def send_encrypted(KEY, m):
    IV = R.read(BLOCK_SIZE)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    c = aes.encrypt(pad(m))
    print (IV + c).encode('hex')

def read_encrypted(KEY):
    data = raw_input("").decode('hex')
    IV, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    m = unpad(aes.decrypt(data))
    return m

def serve_commands(KEY):
    while True:
        print "Enter cmd: (encry)"
        cmd = read_encrypted(KEY)
        #cmd = 'cat flag.txt'
        try:
            output = check_output(cmd, shell=True, stderr=STDOUT)
            #print output
        except CalledProcessError as e:
            output = str(e) + "\n"
        print "Giving cmd result, encry: "    
        send_encrypted(KEY, output)

print """Welcome to the
______ _   _   _____ _          _ _ 
|  _  \ | | | /  ___| |        | | |
| | | | |_| | \ `--.| |__   ___| | |
| | | |  _  |  `--. \ '_ \ / _ \ | |
| |/ /| | | | /\__/ / | | |  __/ | |
|___/ \_| |_/ \____/|_| |_|\___|_|_|
"""

print "Parameters:"
print "p = {}".format(p)
print "g = {}".format(g)

a = random.randint(1, 2**46)
A = pow(g, a, p)
#A = 118273972112639120186970068947944724773714770611796145560317038505039351377800437911584090954295445815108415228076067419564334318734103894856428799576147989726840111816497674618324630523684004675727128364154281009934628997112127793757633331795515579928803348552388657916707518365689221161578522942036857923828
#print "Pow 2,3,6", pow(2,3,7)
print "A = {}".format(A)

B = int(raw_input("Please supply B: "))
K = pow(B, a, p)
#print K

KEY = sha256(str(K)).digest()

pw = read_encrypted(KEY) #returns pt from  input IV+CT

print "Found pw: ", pw
####playing with iv######

cmd = 'pwd'
print "KEY: ", KEY.encode('hex')
print "Encrypting pwd command:"
send_encrypted(KEY, cmd)


######################
#added command
password = pw
if pw == password:

    serve_commands(KEY)
else:
    send_encrypted("Invalid password!\n")
