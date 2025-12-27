from pathlib import Path

code = Path("program").read_bytes()
ins = [tuple(code[i:i+3]) for i in range(0, len(code), 3)]

def show(i, op, a, b):
    opcode = ["read", "imov", "mov", "add", "mul", "xor", "not"]
    return f"{i:03d}: ({opcode[op]},{a},{b})"

for i,(op,a,b) in enumerate(ins):
    print(show(i,op,a,b))
