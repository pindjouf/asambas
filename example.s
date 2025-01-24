.global _start

.section .data
str_1: .ascii "what\n"
str_2: .ascii "is\n"
str_3: .ascii "love?\n"
len_1: .byte 0x05
len_2: .byte 0x03
len_3: .byte 0x06
exit_code: .byte 0x16

.section .text
_start:
    mov r0, #0x01
    ldr r1, =str_1
    ldr r2, =len_1
    ldrb r2, [r2]
    bl print
    ldr r1, =str_2
    ldr r2, =len_2
    ldrb r2, [r2]
    bl print
    ldr r1, =str_3
    ldr r2, =len_3
    ldrb r2, [r2]
    bl print
    ldr r1, =exit_code
    ldrb r0, [r1]
    mov r7, #0x01
    svc #0x00

print:
    mov r0, #0x01
    mov r7, #0x04
    svc #0x00
    mov pc, lr
