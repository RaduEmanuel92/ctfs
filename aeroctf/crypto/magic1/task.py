#!/usr/bin/env python3.7

import numpy as np
import math
from itertools import chain
import numpy as np
import string

# Python program to generate  
# odd sized magic squares 
# A function to generate odd 
# sized magic squares 
def generateSquare(n): 
  
    # 2-D array with all  
    # slots set to 0 
    magicSquare = [[0 for x in range(n)] 
                      for y in range(n)] 
  
    # initialize position of 1 
    i = n / 2
    j = n - 1
      
    # Fill the magic square 
    # by placing values 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n: # 3rd condition 
            j = n - 2
            i = 0
        else: 
              
            # next number goes out of 
            # right side of square  
            if j == n: 
                j = 0
                  
            # next number goes  
            # out of upper side 
            if i < 0: 
                i = n - 1
                  
        if magicSquare[int(i)][int(j)]: # 2nd condition 
            j = j - 2
            i = i + 1
            continue
        else: 
            magicSquare[int(i)][int(j)] = num 
            num = num + 1
                  
        j = j + 1
        i = i - 1 # 1st condition 
   
  
    # Printing magic square
    print ("=============")
    print ("Sum of each row or column", n * (n * n + 1) / 2, "\n") 
    '''  
    print ("Magic Squre for n =", n) 
    
    
    for i in range(n): 
        for j in range(n): 
            print('%2d ' % (magicSquare[i][j]), end = '') 
              
            # To display output  
            # in matrix form 
            if j == n - 1:  
                print() 
    '''
    return magicSquare


class Cipher(object):
    def __init__(self, key: int, canary: int):
        self._key = key
        self._canary = canary
        return

    @property
    def key(self) -> int:
        return self._key

    @property
    def canary(self) -> int:
        return self._canary

    def encrypt(self, message: bytes) -> bytes:
        plaintext = int.from_bytes(message, 'big')
        # print("KEY length") 
        # print(self._key.bit_length())
        # print("PT length") 
        # print(plaintext.bit_length())
        #print("key: {}".format(self._key))
        assert self._key.bit_length() >= plaintext.bit_length()
        ciphertext = self._key ^ plaintext
        length = (ciphertext.bit_length() + 7) // 8
        return ciphertext.to_bytes(length, 'big')

    def decrypt(self, message: bytes) -> bytes:
        ct = int.from_bytes(message, byteorder='big')
        
        leng = (ct * 8 - 7)
        leng = leng.bit_length()
        #leng = ct.bit_length()
        #print(leng)
        #assert self._key.bit_length() >= ct.bit_length()
        # print("[decr] KEY:")
        # print(self._key)

        flag = self._key ^ ct 
        #print(flag)
        return flag.to_bytes(leng, 'big')
        #raise NotImplementedError

    @classmethod
    def create(cls, source: np.ndarray) -> 'Cipher':
        assert len(set(source.shape)) == 1
        line = source.reshape(-1)
        assert len(line) == len( set(line) & set(range(len(line))) ) 
        keys = set(map(sum, chain.from_iterable((*s, np.diag(s)) for s in [source, source.T])))
        print(len(line))
        assert len(keys) == 1
        key = int(keys.pop())
        print("_key:")
        print(key)
        print("_can:")
        print(key % len(line))

        return cls(key, key % len(line))
    

def compute_key(n):
    #    return int((n * (n*n + 1)/2) - n)
    return int((n * (n*n + 1)//2) - n)


def gen_cand(c, r):
    var = math.sqrt(c*c - r + 1)
    if isinstance(var, int):
        return c + var
    else:
        return -1    



def ver_key(ct, idx, crib):
    cand_key = compute_key(idx)
    #if cand_key % idx*idx == canary:
    #print("[*] try key {} -> {} bits".format(cand_key, cand_key.bit_length()))
        
    print("[***] try key {} -> {} -> {} bits".format(idx, cand_key, cand_key.bit_length()))
    cand_pt = ct ^ cand_key
    #length = (cand_pt.bit_length() + 7) // 8
    leng = (ct * 8 - 7)
    leng = leng.bit_length()
    cand_pt = cand_pt.to_bytes(leng, 'big')
    if crib in cand_pt :
        print("[+] found candidate key {} {}".format(cand_key,cand_pt ))
        return cand_pt
        # cipher    = Cipher.create(cand_secr) 
        # plaintext = cipher.decrypt(secr_enc)
        # print(plaintext)
 

def find_square(r) :
    k = 1
    while True:
        c = k*k + r - 1
        if isinstance(math.sqrt(c), int):
            print(c)
            break
        else:
            c += 1
    return 1

def main():
    #from secret import SECRET, FLAG
    #cipher = Cipher.create(SECRET)
    #print(cipher.encrypt(FLAG).hex())
    #print(cipher.canary)
    
    # test
    
    can = 1501
    candidate = generateSquare(can)
    #print(candidate)

    for idx in range(can):
        for idy in range(can):
            candidate[idx][idy] -= 1

    
    cand_secr = np.array(candidate)
    cipher = Cipher.create(cand_secr)
    print("Canary:")
    print(cipher.canary)
    print("Key:")
    print(cipher.key)

    flag = b"A{d}"
    print("test encrypt")
    encr = cipher.encrypt(flag)
    print(encr)

    print("test decrypts")
    print(cipher.decrypt(encr))
    

    SECRET_ENCR = "d9a103a6006bfba17074ef571011d8eededdf851b355bdc4795616744066433695b9e9201f6deff7577c03ba690d4d517bdaae"             
    canary = 5405053190768240950975482839552589374748349681382030872360550121041249100085609471
    secr_enc = bytes.fromhex(SECRET_ENCR)
    ct = int.from_bytes(secr_enc, byteorder='big')
    crib = b'Aero{'
    crib2 = b'oreA'
    flag = ''
    key = ''



    # lil smaller than the cananry bit len
    #can_value = 2211108169930076950954187620
    m =   103971661434914474977947909929808181577819
    #idx = 1
    # lil smaller than the enc bit len
    #idx = 2 ** 136 + 1
    # idx = can_value
    # while True:

    #     cand_key = compute_key(idx)
    #     if cand_key % idx*idx == canary:
    #     #print("[*] try key {} -> {} bits".format(cand_key, cand_key.bit_length()))
            
    #         print("[***] try key {} -> {} -> {} bits".format(idx, cand_key, cand_key.bit_length()))
    #         cand_pt = ct ^ cand_key
    #         #length = (cand_pt.bit_length() + 7) // 8
    #         leng = (ct * 8 - 7)
    #         leng = leng.bit_length()
    #         cand_pt = cand_pt.to_bytes(leng, 'big')
    #         if crib in cand_pt :
    #             print("[+] found candidate key {} {}".format(cand_key,cand_pt ))
    #             cipher    = Cipher.create(cand_secr) 
    #             plaintext = cipher.decrypt(secr_enc)
    #             print(plaintext)
    #             break
    #         else:
    #             idx -= 2
    #find_square(canary)
    print("bla")
    c = int(canary/2)
    while True:
        if (c*c - canary + 1 < 0):
            print("bayud")
            pass
        key = gen_cand(c, canary )
        if key == -1:
            pass
        elif key % 2 == 0:
            print("wrong {}".format(key))
            pass
        else:
            print(key)
            ver_key(ct, key, crib)
        
        c += 1

    # correction
    # for idx in range(cand):
    #     for idy in range(cand):
    #         candidate[idx][idy] -= 1
    
    # cand_secr = np.array(candidate)
    # print("---")
    # print(cand)
    # cipher = Cipher.create(cand_secr)
    # print(cipher.canary)

    # plaintext = cipher.decrypt(secr_enc)
    # if crib in plaintext or crib2 in plaintext:
    #     print(plaintext)
        
if __name__ == '__main__':
    main()
