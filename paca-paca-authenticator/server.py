from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os
import json

aes_key = os.urandom(16)
flag = os.environ.get("FLAG", "Alpaca{dummy}")

def register(username, message):
    data = json.dumps({"name": username, "message": message}).encode()
    cipher = AES.new(aes_key, AES.MODE_CBC)
    token = cipher.encrypt(pad(data, 16))
    print("[debug]", cipher.iv.hex())
    return token

def login(iv, token):
    data = unpad(AES.new(aes_key, AES.MODE_CBC, iv=iv).decrypt(token), 16)
    data = json.loads(data)
    return data["name"], data["message"]


token = register("alpaca", "paca paca!")
print("This is your login token:", token.hex())

print("Oops! I forgot to save the iv, so I can't decrypt the token! Do you know it?")
iv = bytes.fromhex(input("help me> "))

try:
    username, message = login(iv, token)
except Exception as e:
    print("something wrong:", e)
    exit(1)

if username == "alpaca":
    print("paca paca!")
    print("Thanks! That really helped!")
elif username == "llama":
    print("llama!?!!?", flag)
    print("Oh no, I accidentally leaked the flag...")
else:
    print(f"{username}... who are you?")
