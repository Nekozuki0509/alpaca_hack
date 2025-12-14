w0 = 0
w1 = 0
w4 = 1
w2 = 0
pc = 0x864 # jump to 0x864

while True:
    if pc == 0x854:
        w0 += w3
        w1 += 1
        pc = 0x85c

    if pc == 0x85c:
        w4 = w2
        w2 = w3
        pc = 0x864

    if pc == 0x864:
        w3 = w2 + w4
        if w1 & 1 == 0:
            pc = 0x854
            continue

        w1 += 1
        if w1 != 0x28:
            pc = 0x85c
            continue
        break

# w0が返り値
print(w0)
