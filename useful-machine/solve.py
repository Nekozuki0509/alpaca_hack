import io, sys
from vm import VM

program = open("program", "rb").read()

n = sum(1 for i in range(0, len(program), 3) if program[i] == 0)

def run_until(input_bytes: bytes, steps: int) -> VM:
    vm = VM(program)
    old = sys.stdin
    sys.stdin = io.StringIO(input_bytes.decode("latin1"))
    try:
        for _ in range(steps):
            if not vm.step():
                break
    finally:
        sys.stdin = old
    return vm

flag = bytearray()

for i in range(n):
    steps = 1 + 9 * (i + 1)
    for x in range(256):
        vm = run_until(bytes(flag + bytes([x])), steps)
        if vm.mem[0] == 1:
            flag.append(x)
            print(flag)
            break
