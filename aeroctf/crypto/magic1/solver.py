from gmpy2 import mpz
import gmpy2
from Crypto.Util.number import *

def factors(n):
    result = set()
    n = mpz(n)
    for i in range(1, gmpy2.isqrt(n) + 1):
        div, mod = divmod(n, i)
        if not mod:
            result |= {mpz(i), div}
    return result

def compute_key(n):
    #    return int((n * (n*n + 1)/2) - n)
    return int((n * (n*n + 1)//2) - n)

flag = 'd9a103a6006bfba17074ef571011d8eededdf851b355bdc4795616744066433695b9e9201f6deff7577c03ba690d4d517bdaae'
secr_enc = bytes.fromhex(flag)
ct = int.from_bytes(secr_enc, byteorder='big')
c = 5405053190768240950975482839552589374748349681382030872360550121041249100085609471

#p = factors(2*c)
p =  [13 , 523 , 3989 ,147419 , 1123483 , 59798254331, 7868139393451, 5637813537472069, 453627807529130112554537]
print(p)
perm = []

for item in p:
    perm.append(item)

perm =  [13 , 523 , 3989 ,147419 , 1123483 , 59798254331, 7868139393451, 5637813537472069, 453627807529130112554537]

import itertools

nn = -1
found = False
crib = b"Aero{"
for k in range(1, len(perm) + 1):
    if found:
        break
    for item in itertools.combinations(perm, k):
        n = 1
        for i in item:
            n *= i
            key = compute_key(n)
            pt = int(key)^int(ct)
            pt = long_to_bytes(pt)
            if crib in pt:
                print("found:")
                print(pt)
                break
        # if (0.5*(n*(n**2 + 1)) - n) % (n**2) == c:
        #     print("found:")
        #     print(n)
        #     nn = n
            
        #     found = True
        #     break


n = nn
n = 103971661434914474977947909929808181577819
key = compute_key(n)



#ct = bytes_to_long(flag)
pt = int(key)^int(ct)
print(['ct', ct])
print(['pt', pt])
print(['key', key])
print([long_to_bytes(pt)])