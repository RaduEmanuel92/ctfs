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


def modInverse( a, m):  
    a = a%m; 
    for x in range(m):
       if ((a*x) % m == 1): 
          return x

    return 251

flag = Image.open(r"enc2.png")

img = array(flag)
a, b, c = img.shape
key     = [41, 37, 23]
key_inv = [49, 95, 131]

for x in range (0, a):
    for y in range (0, b):
        #cand = [0,0,0,255]
        pixel     = img[x, y]
        for i in range(0,3):
            #print pixel[i]

            pixel[i] = pixel[i] * key_inv[i] % 251
            #print pixel[i]
            

        '''
        can_r = []

        br = 1
        for r in range(251):      
            br = r * key_inv[0] % 251
            
            if br == pixel[0]:
                can_r.append(r)


        if len(can_r) > 1:
            print can_r
            pixel[0] = can_r[1]
        else:
            pixel[0] = can_r[0]

        can_g = []
        for g in range(251):
            br = g * key_inv[1] % 251
            
            if br == pixel[1]:
                can_g.append(g)

        if len(can_g) > 1:
            print can_g
            pixel[1] = can_g[1]
        else:
            
            pixel[1] = can_g[0]

        can_b = []
        for b in range(251):
            br = b * key_inv[2] % 251
            
            if br == pixel[2]:
                can_b.append(b)
        
        if len(can_b) > 1:
            print can_b
            pixel[2] = can_b[1]
        else:
            
            pixel[2] = can_b[0]
        '''

        img[x][y] = pixel

dec = Image.fromarray(img)
dec.save('dec2.png')


# actf{m0dd}
# actf{m0dd3rn_xx#xxx}
# actf{x#xx#xx_xx#xxx}
