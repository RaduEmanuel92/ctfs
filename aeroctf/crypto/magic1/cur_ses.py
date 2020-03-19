# coding: utf-8
list([1,2,3])
generateSquare(3)
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
    '''  
    print ("Magic Squre for n =", n) 
    print ("Sum of each row or column", n * (n * n + 1) / 2, "\n") 
    
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
    def canary(self) -> int:
        return self._canary

    def encrypt(self, message: bytes) -> bytes:
        plaintext = int.from_bytes(message, 'big')
        assert self._key.bit_length() >= plaintext.bit_length()
        ciphertext = self._key ^ plaintext
        length = (ciphertext.bit_length() + 7) // 8
        return ciphertext.to_bytes(length, 'big')

    def decrypt(self, message: bytes) -> bytes:
        ct = int.from_bytes(message, byteorder='big')
        leng = (ct * 8 - 7)
        leng = leng.bit_length()
        #leng = ct.bit_length()
        
        print(leng)
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
        print(keys)
        assert len(keys) == 1
        key = int(keys.pop())
        return cls(key, key % len(line))
    
import numpy as np

from itertools import chain
import numpy as np


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
    '''  
    print ("Magic Squre for n =", n) 
    print ("Sum of each row or column", n * (n * n + 1) / 2, "\n") 
    
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
    def canary(self) -> int:
        return self._canary

    def encrypt(self, message: bytes) -> bytes:
        plaintext = int.from_bytes(message, 'big')
        assert self._key.bit_length() >= plaintext.bit_length()
        ciphertext = self._key ^ plaintext
        length = (ciphertext.bit_length() + 7) // 8
        return ciphertext.to_bytes(length, 'big')

    def decrypt(self, message: bytes) -> bytes:
        ct = int.from_bytes(message, byteorder='big')
        leng = (ct * 8 - 7)
        leng = leng.bit_length()
        #leng = ct.bit_length()
        
        print(leng)
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
        print(keys)
        assert len(keys) == 1
        key = int(keys.pop())
        return cls(key, key % len(line))
    
get_ipython().system('ls')
get_ipython().system('pwd')
get_ipython().magic('cd mega/')
dir
get_ipython().system('dir')
get_ipython().magic('cd ..')
dir
get_ipython().magic('cd magic1/')
get_ipython().magic('save cur_ses ~0/')



def magic(N):
    magic_square = np.zeros((N,N), dtype=np.intp)

    n = 1
    i, j = 0, N//2

    while n <= N**2:
        magic_square[i, j] = n
        n += 1
        newi, newj = (i-1) % N, (j+1)% N
        if magic_square[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    return magic_square        