from pwn import *

flag_u64 = [
    0x9beff28796ecf3e9, 0x2335ae47c5b3ea6a,
    0x7bd30354a9dfecfe, 0x3243804702b92b8c,
    0x7caad2839ae4bf07, 0x2749c14807c2e873,
    0xbcd9c683a3ebf11c, 0x4119a527d9aa0a73,
]

# 64バイト列（little-endian）にする
enc = flat(flag_u64, word_size=64)

# micro_kernelA の op1*op2 の積（16bit）
C = (0x1dea * 0xcafe) & 0xffff

# 各laneがONになる回数
counts = [0]*8
for j in range(0x100):
    for k in range(8):
        counts[k] += j > (1<<k)

# 結果的に各laneに足された数
deltas = [(C * c) & 0xffff for c in counts]

# エンディアン考慮した暗号化flag列から16bit毎にdeltaを引いて復号
out = bytearray()
for off in range(0, 64, 16):
    block = enc[off:off+16]
    u16s = [u16(block[i:i+2]) for i in range(0, 16, 2)]
    u16s = [(u16s[i] - deltas[i]) & 0xffff for i in range(8)]
    out += b"".join(p16(x) for x in u16s)

print(out.decode())
