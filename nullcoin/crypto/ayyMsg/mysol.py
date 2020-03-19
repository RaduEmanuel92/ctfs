#/usr/bin/python3
from Crypto.PublicKey import RSA, ECC
import json
from hashlib import sha256
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode, b64encode
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from pwn import *
import string
context.log_level = 'error'

def read_message():
    f = open("message.txt", 'r').read()
    message = json.loads(f)
    return message

    
def craft_message(msg, len_msg):
    # generate ECC public key used to sign the forged message
    ecckey  = ECC.generate(curve='P-256')
    pubkey  = ecckey.public_key()
    pubkey_bytes = pubkey.export_key(format='DER')

    # forge the new message
    h       = SHA256.new(msg["aeskey"] + msg["nonce"] + msg["message"][:len_msg])
    signer  = DSS.new(ecckey, 'fips-186-3')
    
    # sign the message
    signature = signer.sign(h)
    
    # put togheder the message
    json_file = {
        "nonce"     : b64encode(msg["nonce"]).decode('utf-8'),
        "message"   : b64encode(msg["message"][:len_msg]).decode('utf-8'),
        "aeskey"    : b64encode(msg["aeskey"]).decode('utf-8'),
        "signature" : b64encode(signature).decode('utf-8'),
        "eccpubkey" : b64encode(pubkey_bytes).decode('utf-8')
    }
    json_msg = json.dumps(json_file)
    return json_msg


def find_flagbyte(flag_hash, flag):
    flag_hash = flag_hash[2:-3]
    for cand_chr in string.printable:
        cand_byte = cand_chr.encode('utf-8')
        tmp_flag  = flag + cand_byte
        cand_hash = sha256(tmp_flag).hexdigest()
        if cand_hash == flag_hash:
            flag += cand_byte
            print("[+] FLAG: {}".format(flag))
            break
    return flag        

def main():
    message = read_message()
    #print(message)
    message["nonce"]     = b64decode(message["nonce"])
    message["message"]   = b64decode(message["message"])
    message["aeskey"]    = b64decode(message["aeskey"])
    message["signature"] = b64decode(message["signature"])
    message["eccpubkey"] = b64decode(message["eccpubkey"])

    msg_len = len(message["message"])

    # Begin attack
    flag = b''
    for msg_l in range(1, msg_len):
        new_msg = craft_message(message, msg_l)
        conn = remote("crypto1.ctf.nullcon.net", 5001)
        conn.recvuntil('Enter message in json format:', drop=True)
        conn.send("{}{}".format(new_msg, '\n'))
        conn.recvline()
        flag_hash = str(conn.recvline())
        flag = find_flagbyte(flag_hash, flag)


if __name__ == "__main__":
    main()