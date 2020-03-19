from Crypto.PublicKey import RSA
import json
from hashlib import sha256
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode, b64encode
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from pwn import *
context.log_level = 'error'

message_dict = json.loads(open('message.txt', 'r').read())

nonce = b64decode(message_dict["nonce"])
aeskey = b64decode(message_dict["aeskey"])
message = b64decode(message_dict["message"])

def get_receipt(message_length):
    p = remote("crypto1.ctf.nullcon.net",  5001)
    p.recvuntil("Enter message in json format:")

    key = ECC.generate(curve='P-256')
    h = SHA256.new(aeskey + nonce + message[:message_length])
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(h)
    eccpubkey = key.public_key().export_key(format="DER")

    d = {
        "nonce":b64encode(nonce).decode("utf-8"),
        "message":b64encode(message[:message_length]).decode("utf-8"),
        "aeskey":b64encode(aeskey).decode("utf-8"),
        "signature":b64encode(signature).decode("utf-8"),
        "eccpubkey":b64encode(eccpubkey).decode("utf-8"),
    }

    p.sendline(json.dumps(d))
    p.recvline()

    return p.recvline().strip().decode("utf-8")


def crack_byte(known_plain, digest):
    for i in range(256):
        candidate = known_plain + bytes([i])
        d = sha256(candidate).hexdigest()
        if digest == d:
            return bytes([i])


flag = b""

while len(flag) < 68:
    x = get_receipt(len(flag)+1)
    b = crack_byte(flag, x)
    print(flag)
    flag += b

print(flag)
