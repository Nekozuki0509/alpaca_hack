from Crypto.Util.number import *
import base64
import os

long_value = 373502670300504551747111047082539140193958649718
hex_string = "346c5f6833785f6630726d61745f31735f636c33"
base64_string = "NG5fYjY0X3A0ZGQxbmdfaXNfY29vbH0="

print(long_to_bytes(long_value) + bytes.fromhex(hex_string) + base64.b64decode(base64_string))
