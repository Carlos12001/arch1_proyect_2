.global _start
.section .data
text: .ascii "LOREM IPSUM DOLOR SIT AMET, CONSECTETUER ADIPISCING ELIT. AENEAN COMMODO LIGULA EGET DOLOR. AENEAN MASSA. CUM SOCIIS NATOQUE PENATIBUS ET MAGNIS DIS PARTURIENT MONTES, NASCETUR RIDICULUS MUS. DONEC QUAM FELIS, ULTRICIES NEC, PELLENTESQUE EU, PRETIUM QUIS, SEM. NULLA CONSEQUAT MASSA QUIS ENIM. DONEC PEDE JUSTO, FRINGILLA VEL, ALIQUET NEC, VULPUTATE EGET, ARCU. IN ENIM JUSTO, RHONCUS UT, IMPERDIET A, VENENATIS VITAE, JUSTO. NULLAM DICTUM FELIS EU PEDE MOLLIS PRETIUM. INTEGER TINCIDUNT. CRAS DAPIBUS. VIVAMUS ELEMENTUM SEMPER NISI. AENEAN VULPUTATE ELEIFEND TELLUS. AENEAN LEO LIGULA, PORTTITOR EU, CONSEQUAT VITAE, ELEIFEND AC, ENIM. ALIQUAM LOREM ANTE, DAPIBUS IN, VIVERRA QUIS, FEUGIAT A. "

.align 2
puntos: .space 200

my_data: .space 36000

.section .text
_start:
ldr r0, =puntos
bl set_pixel    // Usa 36 bytes osea 9 words
ldr r0, =puntos
mov r1, r0
add r0, #40    // El puntero queda en la 10 word
bl clear_points
ldr r12, =puntos
mov r0, #1
mov r1, #0
mov r2, #4
mov r3, #0
bl bresenham
breaking:

// Salir del programa
mov %r0, #0  // return val
mov %r7, #1   // exit system call magic number   
swi      #0   // Interupt / syscall
// b .


// FUNCTION set_pixels
set_pixel:
sub sp, sp, #12    // Adjust the stack pointer to make space for 3 registers (4 bytes each)
str lr, [sp, #8]   // Store lr on the stack
str r2, [sp, #4]   // Store r2 on the stack
str r1, [sp]       // Store r1 on the stack

mov r1, #255
mov r2, #0

set_pixel_for:
strb r1, [r0, r2]  // Store the value of r1 at memory address r0 + r2
add r2, r2, #1
cmp r2, #36        // Compare r2 with the immediate value 36
bne set_pixel_for

ldr r1, [sp]       // Load r1 from the stack
ldr r2, [sp, #4]   // Load r2 from the stack
ldr lr, [sp, #8]   // Load lr from the stack
add sp, sp, #12    // Adjust the stack pointer to release the space used by the registers

mov pc, lr         // Return from the function


// FUNCTION clear_points
clear_points:
sub r0, r0, #4      // Decrement r0 by 4 to point to the last element
mov r2, #0          // Load the value 0 into r2 to clear the words

for_clear_points:
str r2, [r0]        // Store the value 0 at the current position
sub r0, r0, #4      // Decrement r0 by 4 to point to the previous position
cmp r0, r1          // Compare r0 with r1
bge for_clear_points // Jump to the 'for_clear_points' label if r0 is greater than or equal to r1

add r0, r0, #4      // Increment r0 by 4 to point to the last cleared position
mov pc, lr          // Return from the function


// FUNCTION bresenham
bresenham:
sub sp, sp, #40  // Ajusta el puntero de pila para hacer espacio para 10 registros (4 bytes cada uno)
str lr, [sp, #36]  // Almacena lr en la pila
str r4, [sp, #32]  // Almacena r4 en la pila
str r5, [sp, #28]  // Almacena r5 en la pila
str r6, [sp, #24]  // Almacena r6 en la pila
str r7, [sp, #20]  // Almacena r7 en la pila
str r8, [sp, #16]  // Almacena r8 en la pila
str r9, [sp, #12]  // Almacena r9 en la pila
str r10, [sp, #8]  // Almacena r10 en la pila
str r11, [sp, #4]  // Almacena r11 en la pila

mov r4, r0
mov r5, r1
mov r6, r2
mov r7, r3

sub r0, r6, r4
bl abs
mov r8, r0 // dx = abs(x2 - x1)

sub r0, r7, r5
bl abs
mov r9, r0 // dy = abs(y2 - y1)
mov r10, r4   // x = x1
mov r11, r5 // y = y1


if_x_compare:  // x1 > x2
cmp r4, r6
ble else_x_compare 
ldr r4, =0xffffffff // sx = -1
b end_if_x_compare

else_x_compare:
mov r4, #0x1 // sx = 1

end_if_x_compare:

if_y_compare:  // y1 > y2
cmp r5, r7
ble else_y_compare
ldr r5, =0xffffffff // sy = -1
b end_if_y_compare
else_y_compare:
mov r5, #01 // sy = 1

end_if_y_compare:

if_differentials:  // dx > dy
cmp r8, r9
ble else_differentials
asr r0, r8, #0x01  // dx >> 1 === dx/2

while_dx_bigger:  // while (x != x2)
cmp r10, r6
beq end_while_dx_bigger
str r10, [r12]  // save x
add r12, r12, #0x04
str r11, [r12]  // save y
add r12, r12, #0x04
sub r0, r0, r9  // err -= dy

if_while_dx_bigger:  // if (err < 0)
cmp r0, #0x00
bge end_if_while_dx_bigger
add r11, r11, r5  // y += sy
add r0, r0, r8    // err += dx

end_if_while_dx_bigger:
add r10, r10, r4  // x += sx
b while_dx_bigger

end_while_dx_bigger:
b end_if_differentials

else_differentials:
lsr r0, r9, #0x01  // dy >> 1 === dy/2

while_dy_bigger:  // while (y != y2)
cmp r11, r7
beq end_while_dy_bigger
str r10, [r12]  // save x
add r12, r12, #0x04
str r11, [r12]  // save y
add r12, r12, #0x04
sub r0, r0, r8  // err -= dx

if_while_dy_bigger:  // if (err < 0)
cmp r0, #0x00
bge end_if_while_dy_bigger
add r10, r10, r4  // x += sx
add r0, r0, r9    // err += dy

end_if_while_dy_bigger:
add r11, r11, r5  // y += sy
b while_dy_bigger

end_while_dy_bigger:
b end_if_differentials

end_if_differentials:

str r6, [r12]  // save x
add r12, r12, #0x04
str r7, [r12]  // save y
add r12, r12, #0x04

mov r0, r12
ldr r11, [sp, #4]  // Carga r11 desde la pila
ldr r10, [sp, #8]  // Carga r10 desde la pila
ldr r9, [sp, #12]  // Carga r9 desde la pila
ldr r8, [sp, #16]  // Carga r8 desde la pila
ldr r7, [sp, #20]  // Carga r7 desde la pila
ldr r6, [sp, #24]  // Carga r6 desde la pila
ldr r5, [sp, #28]  // Carga r5 desde la pila
ldr r4, [sp, #32]  // Carga r4 desde la pila
ldr lr, [sp, #36]  // Carga lr desde la pila
add sp, sp, #40  // Ajusta el puntero de pila para liberar el espacio utilizado por los registros
mov pc, lr

ldr r11, [sp, #4]  // Carga r11 desde la pila
ldr r10, [sp, #8]  // Carga r10 desde la pila
ldr r9, [sp, #12]  // Carga r9 desde la pila
ldr r8, [sp, #16]  // Carga r8 desde la pila
ldr r7, [sp, #20]  // Carga r7 desde la pila
ldr r6, [sp, #24]  // Carga r6 desde la pila
ldr r5, [sp, #28]  // Carga r5 desde la pila
ldr r4, [sp, #32]  // Carga r4 desde la pila
ldr lr, [sp, #36]  // Carga lr desde la pila
add sp, sp, #40  // Ajusta el puntero de pila para liberar el espacio utilizado por los registros
mov pc, lr


// FUNCTION ABS
abs:
asr r1, r0, #0x1f // r1 = r0 >> 31
add r2, r0, r1 // r2 = (r0 + r1)
eor r3, r2, r1 // r3 = r2 ^ r1
mov r0, r3     
mov pc, lr        // return