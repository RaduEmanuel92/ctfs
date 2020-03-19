#!/usr/bin/env python3
from Crypto import Random
from Crypto.Random import random
from Crypto.Util.number import *
#from secret import flag

sbox = [221, 229, 120, 8, 119, 143, 33, 79, 22, 93, 239, 118, 130, 12, 63, 207, 90, 240, 199, 20, 181, 4, 139, 98, 78, 32, 94, 108, 100, 223, 1, 173, 220, 238, 217, 152, 62, 121, 117, 132, 2, 55, 125, 6, 34, 201, 254, 0, 228, 48, 250, 193, 147, 248, 89, 127, 174, 210, 57, 38, 216, 225, 43, 15, 142, 66, 70, 177, 237, 169, 67, 192, 30, 236, 131, 158, 136, 159, 9, 148, 103, 179, 141, 11, 46, 234, 36, 18, 191, 52, 231, 23, 88, 145, 101, 17, 74, 44, 122, 75, 235, 175, 54, 40, 27, 109, 73, 202, 129, 215, 83, 186, 7, 163, 29, 115, 243, 13, 105, 184, 68, 124, 189, 39, 140, 138, 165, 219, 161, 150, 59, 233, 208, 226, 176, 144, 113, 146, 19, 224, 111, 126, 222, 178, 47, 252, 99, 87, 134, 249, 69, 198, 164, 203, 194, 170, 26, 137, 204, 157, 180, 168, 162, 56, 81, 253, 213, 45, 21, 58, 24, 171, 37, 82, 53, 50, 84, 196, 232, 242, 244, 64, 80, 10, 114, 212, 187, 205, 28, 51, 182, 16, 107, 245, 211, 85, 92, 195, 5, 197, 200, 31, 183, 61, 123, 86, 167, 154, 41, 151, 35, 247, 246, 153, 95, 206, 149, 76, 112, 71, 230, 106, 188, 172, 241, 72, 156, 49, 14, 214, 155, 110, 102, 116, 128, 160, 135, 104, 77, 91, 190, 60, 42, 185, 96, 97, 251, 218, 133, 209, 65, 227, 3, 166, 255, 25]
p = [5, 9, 1, 8, 3, 11, 0, 12, 7, 4, 14, 13, 10, 15, 6, 2]
round = 16


def pad(data, size = 16):
    pad_byte = (size - len(data) % size) % size
    data = data + bytearray([pad_byte]) * pad_byte
    return data


def repeated_xor(p, k):
    return bytearray([p[i] ^ k[i % len(k)] for i in range(len(p))])


def bytes_to_int(xbytes):
    return bytes_to_long(xbytes)


def int_to_bytes(x):
    return long_to_bytes(x, 16)


def group(input, size = 16):
    return [input[i * size: (i + 1) * size] for i in range(len(input) // size)]

def solver(choices):
    roll = [b'r', b'p', b's']
    choices = choices.split(" ")
    cd = []
    for choice in choices:
        cand_secrets = reverse_hash(choice)
        cd.append(cand_secrets)

    for idx in range(0,3):
        for idy in range(0,3):
            for idz in range(0,3):
                if cd[0][idx][0] == cd[1][idy][0] == cd[2][idz][0]: 
                    print("Found encoding:\n")
                    print("{} - {} \n".format(choices[0], cd[0][idx][1]))
                    roll.remove(cd[0][idx][1])
                    print("{} - {} \n".format(choices[1], cd[1][idy][1]))
                    roll.remove(cd[1][idy][1])
                    print("{} - {} \n".format(choices[2], roll[0]))



def reverse_hash(hash_fin):
    state = bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])
    
    hash_fin_int = int(hash_fin, 16)
    hash_fin_bytes = int_to_bytes(hash_fin_int)
    round = 16
    choices = [b'r', b'p', b's']
    idy = 0
    cand_roundkeys = [ choice + b'\x0f'*15 for choice in choices]    
    secrets = []
    for cand_round in cand_roundkeys:
        mystate = bytearray(16)
        hash_fin_int = int(hash_fin, 16)
        hash_fin_bytes = int_to_bytes(hash_fin_int)
        print("[+] ------------TRY NEW KEY -------------------")
        for _ in range(round):
            # recover round 1 of shuffling
            temp = bytearray(16)
            #print("h fin bytes is now {}".format(hash_fin_bytes))
            #print("mystate is now {}".format(mystate))
            for idx in range(len(hash_fin_bytes)):
                temp[idx] = hash_fin_bytes[p[idx]]

            mystate = temp
            #print("4:mangled")
            #print(mystate)

            # recover round 2 of shuffling
            temp = bytearray(16)
            for idx in range(len(mystate)): 
                temp[idx] = sbox.index(mystate[idx])

            mystate = temp
            #print("3:sboxed")
            #print(mystate)  
            # recover round 3 of xoring
            mystate = repeated_xor(cand_round, mystate)
            hash_fin_bytes = mystate
            #print("2:xor")
            #print(mystate)
            #print("----------")
        # check if chosen key was correct:
        #if mystate == state:
        #    print("[+] Found choice: {}".format(cand_round[1]))    
        #break
        print("-Intermediate state: {}".format(mystate))
        secrets.append([mystate, choices[idy]])
        idy += 1

    return secrets

def main():



if __name__ == "__main__":
    main()