from Crypto.Util.number import bytes_to_long, long_to_bytes, isPrime
from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_OAEP

from pwn import *
r = remote('crypto.2020.chall.actf.co',20600)
n = 136018504103450744973226909842302068548152091075992057924542109508619184755376768234431340139221594830546350990111376831021784447802637892581966979028826938086172778174904402131356050027973054268478615792292786398076726225353285978936466029682788745325588134172850614459269636474769858467022326624710771957129
e = 0x10001L
def get(m, read=True):
	if read: r.readuntil(": ")
	r.sendline(str(m))
	r.readline()
	out = r.readline(keepends=False)
	return len(out)
key = RSA.construct((n,e))
r.readline()
f = int(r.readline(keepends=False))
baseline = get(f, read=False)
upper = pow(2,baseline)
lower = pow(2,baseline-1)
dd = upper-lower
# part 1: get close enough
mid = (upper+lower)>>1
for num in range(baseline+1,n.bit_length()):
	x = pow(2,num)//mid
	test = (f*key.encrypt(x,0)[0])%n
	res = get(test)
	upper = min(upper,(pow(2,res)-1)//x)
	lower = max(lower,pow(2,res-1)//x)
	if upper-lower < dd:
		dd = upper-lower
		mid = (upper+lower)>>1
	if dd <= 1:
		# binary search is hard, add a tolerance
		break
# part 2: refine
i = 5*pow(10,26) # suitably large number
shift = n*i
for num in range(n.bit_length()):
	x = (pow(2,num)+shift)//mid
	test = (f*key.encrypt(x,0)[0])%n
	res = get(test)
	if res==n.bit_length():
		# we didn't wrap around
		upper = min(upper,(shift-1)//x)
		lower = max(lower,(pow(2,res-1)+shift-n)//x)
	else:
		upper = min(upper,(shift+pow(2,res)-1)//x)
		lower = max(lower,(pow(2,res-1)+shift)//x)
	if upper-lower < dd:
		dd = upper-lower
		mid = (upper+lower)>>1
	if dd <= 1:
		break
print long_to_bytes(upper)
print long_to_bytes(mid)
print long_to_bytes(lower)