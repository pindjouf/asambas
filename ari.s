.global _start

.section .data
random_val: .byte 4

.section .text
_start:
    @ make pointer and dereference
    ldr r5, =random_val
    ldrb r0, [r5]

    @ random arithmetic
    add r1, r0, #3
    add r2, r1, r1
    sub r3, r2, #4

    lsl r4, r3, r2

    @ exit
    mov r0, #42
    mov r7, #1
    svc #0
