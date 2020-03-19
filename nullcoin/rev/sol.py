import subprocess
import struct

o = [296, 272, 272, 272, 296, 360, 272, 424, 272, 208, 120, 120, 120, 96, 120, 120, 120, 120, 120, 120, 120, 208, 120, 120, 208, 208, 208, 208, 208, 272, 120, 208, 208]
r = [208, 225, 237, 20, 214, 183, 79, 105, 207, 217, 125, 66, 123, 104, 97, 99, 107 , 105, 109, 50, 48, 202, 111, 111, 29, 63, 223, 36, 0, 124, 100, 219, 32]

cmd = ['./main']
rets = []

new1 = ''
new2 = ''
for ri in r :
    new1 += chr(ri) 
print(new1)   


with open('blob', 'rb') as f:
    for ofst in range(max(o)):
        data = f.read(ofst)
        print('---------------')
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

        p.stdin.write(data)
     
        #print(offset)
        #print(data)
        p.communicate()
        print(p.returncode)
        print('---------------')
        if p.returncode == r[1]:
            print(offset)
            break    
        rets.append(p.returncode)

   

if all([rets[i] == r[i] for i in range(len(r))]):
    print('Yes!')
else:
    print('No!')
