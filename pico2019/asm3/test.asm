
.global _start

.section .text
_start:
    push   %rbp
    movq    %rbp,%rsp
    xorl    %eax,%eax
    movb    0x9(%rbp),%ah
    shl     $0x10,%ax
    sub     0xd(%rbp),%al
    add     0xe(%rbp),%ah
    xor     0x10(%rbp),%ax
    nop
    pop     %rbp

exit:
   movq $60,%rax
   xorq %rsi,%rsi
   syscall

