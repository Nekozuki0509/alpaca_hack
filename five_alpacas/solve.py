from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# 接続設定（実際のホストとポートに置き換えてください）
HOST = "34.170.146.252"
PORT = 58209

# ローカルテストの場合
# io = process(["python3", "challenge.py"])

# リモート接続
io = remote(HOST, PORT)

# Welcomeメッセージを受信
io.recvline()  # "Welcome to my login service 🦙"

# DEBUGメッセージから鍵を取得
debug_line = io.recvline().decode()
log.info(f"Received: {debug_line}")

# 鍵を抽出（"[DEBUG] key: " の後の16進数）
key_hex = debug_line.split("key: ")[1].strip()
key = bytes.fromhex(key_hex)
log.success(f"Extracted key: {key_hex}")

# 目標のユーザー名を準備
ALPACA = chr(129433)  # "🦙"
target_username = ALPACA * 5
plaintext = target_username.encode('utf-8')
log.info(f"Target username: {target_username}")
log.info(f"Plaintext bytes: {plaintext.hex()}")

# パディングを追加
padded_plaintext = pad(plaintext, AES.block_size)

# IVを設定（任意の16バイト）
iv = b'\x00' * 16

# 暗号化
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(padded_plaintext)

log.success(f"Ciphertext: {ciphertext.hex()}")
log.success(f"IV: {iv.hex()}")

# 暗号文を送信
io.recvuntil(b"Enter your ciphertext (hex): ")
io.sendline(ciphertext.hex().encode())

# IVを送信
io.recvuntil(b"Enter your IV (hex): ")
io.sendline(iv.hex().encode())

# 結果を受信
response = io.recvall().decode()
log.info(f"Response:\n{response}")

# フラグを抽出して表示
if "ALPACA{" in response:
    flag = response.split("ALPACA{")[1].split("}")[0]
    log.success(f"FLAG: ALPACA{{{flag}}}")

io.close()
