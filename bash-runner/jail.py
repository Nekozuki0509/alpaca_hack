import os

path = input("Example: hello.sh\n$ bash ")
if os.path.isfile(path):
    os.system(f"bash {path}")
else:
    print("File not found")
