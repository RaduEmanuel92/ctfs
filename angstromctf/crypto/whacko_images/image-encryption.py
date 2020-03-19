from numpy import *
from PIL import Image

'''flag = Image.open(r"flag.png")
img = array(flag)

key = [41, 37, 23]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            pixel[i] = pixel[i] * key[i] % 251
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('enc.png')'''

from random import shuffle

flag = Image.open(r"enc.png")
img = array(flag)
decr = img
a, b, c = img.shape
key = [41, 37, 23]

for x in range (0, a):
    for y in range (0, b):
        #cand = [0,0,0,255]
        pixel = list(img[x, y])
        can_r = []
        for r in range(255):
            can = r        
            can = can * key[0] % 251
            
            if can == pixel[0]:
                can_r.append(r)
        
        if len(can_r) > 1:
            #print can_r
            pixel[0] = can_r[1]
        else:
            pixel[0] = can_r[0]

        can_r = []
        for g in range(255):
            can = g
            can = can * key[1] % 251
            
            if can == pixel[1]:
                can_r.append(g)

        if len(can_r) > 1:
            #print can_r
            pixel[1] = can_r[1]
        else:
            
            pixel[1] = can_r[0]

        can_r = []
        for b in range(255):
            can = b
            can = can * key[2] % 251
            
            if can == pixel[2]:
                can_r.append(b)
        
        if len(can_r) > 1:
            #print can_r
            pixel[2] = can_r[1]
        else:
            
            pixel[2] = can_r[0]

        decr[x][y] = pixel

dec = Image.fromarray(decr)
dec.save('dec2.png')


# actf{m0dd}
# first 3f9bf1a3f9511b733bd30502f842c627 011
# sec   15781875632139cce7a1a04cdb4a9da8 101
# th    922369da3a30d1e011f9040c956fffdc 110

# 001:  85f5b1129c2f578b8b0d7f59e57acde8
# 010:  964e2931c661b48e86027c2a88c488b7
# 100:  d10ef455c18713ab5034a1a8cc18d666


# 111: nope
