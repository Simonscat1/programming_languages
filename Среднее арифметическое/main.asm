%macro pushd 0
    push edx 
    push ecx
    push ebx
    push eax
%endmacro

%macro popd 0
    pop eax
    pop ebx
    pop ecx
    pop edx
%endmacro

%macro print 2
    pushd
    mov edx, %1
    mov ecx, %2
    mov ebx, 1
    mov eax, 4
    int 0x80
    popd
%endmacro

%macro mean 2
    pushd
    
    mov eax, 0
    mov bx, 0
    
    %%_loop:
        add eax, [%1+ebx]
        add bx, 4
    cmp bx, alen
    jne %%_loop

    mov [%2], eax
    
    mov eax, alen
    mov ecx, 4
    mov edx, 0
    div ecx
    
    mov ecx, eax
    mov eax, [%2]
    mov edx, 0
    div ecx
    
    mov [%2], eax
    
    popd
%endmacro

%macro dprint 0
    pushd
    mov ecx, 10
    mov bx, 0

%%_divide:
    mov edx, 0
    div ecx
    push dx
    inc bx
    test eax, eax
    jnz %%_divide

%%_digit:
    pop ax
    add ax, '0'
    mov [result], ax
    print 1, result
    dec bx
    cmp bx, 0
    jnz %%_digit
    popd
%endmacro

section .text

global _start

_start:
    mean x, value1
    mov eax, [value1]
    dprint
 
    print nlen, newline
    
    mean y, value2
    mov eax, [value2]
    dprint

    
    print nlen, newline
    
    mov eax, [value1]
    mov ecx, [value2]
    
    sub eax, ecx
    
    cmp eax, 0
    jge _not_negative
    
    _negative:
        mov ecx, [value1]
        mov eax, [value2]
        sub eax, ecx
        print len, message 
        
    _not_negative:
        dprint
    
    mov eax, 1
    int 0x80

section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    alen equ $ - x
    y dd 0, 10, 1, 9, 2, 8, 5
    
    
    message db "-"
    len equ $ - message
    newline db 0xA, 0xD
    nlen equ $ - newline

section .bss
    result resd 1
    value1 resd 1
    value2 resd 1
    
