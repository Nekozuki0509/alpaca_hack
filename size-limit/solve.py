c = int(input("c"))
d = int(input("d"))
n = int(input("n"))

from Crypto.Util.number import long_to_bytes
m = pow(c, d, N)
flag = long_to_bytes(m)
print(flag)
