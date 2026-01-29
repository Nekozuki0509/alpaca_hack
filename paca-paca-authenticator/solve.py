from pwn import *

sc = remote("34.170.146.252", "13161")
sc.recvuntil(b"[debug] ")
original_iv = bytes.fromhex(sc.recvline().decode())
sc.recvuntil(b"token: ")
token = bytes.fromhex(sc.recvline().decode())
iv = xor(b"{\"name\": \"alpaca", b"{ \"name\": \"llama", original_iv)
sc.sendlineafter(b"> ", iv.hex())
print(sc.recvline())
