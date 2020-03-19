import math

n = 126390312099294739294606157407778835887
e = 65537
c = 13612260682947644362892911986815626931


def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0 :
        q = b // x # integer division
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m


n_ = 9336949138571181619 * 13536574980062068373
p = 9336949138571181619
q = 13536574980062068373

phi_n = (p-1) * (q-1)

d = inverse(e, phi_n)
#print d
print ("plaintext:")

pt = pow(c, d, n)
print (pt.to_bytes(20, 'big'))