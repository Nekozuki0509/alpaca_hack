import jwt
import time
JWT_EXP = 60 * 60
payload = {
        "sub": "admin",
        "iat": int(time.time()),
        "exp": int(time.time()) + JWT_EXP,
}
JWT_SECRET = "20e515c7d11a1cfd9b4f504dfbf05efadbcecf9c5a2b22bab223444aa2bbcb32"
print(jwt.encode(payload, JWT_SECRET, algorithm="HS256"))
