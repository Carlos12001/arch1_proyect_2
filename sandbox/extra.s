.global _start
.section .data
text: .ascii "LOREM IPSUM DOLOR SIT AMET, CONSECTETUER ADIPISCING ELIT. AENEAN COMMODO LIGULA EGET DOLOR. AENEAN MASSA. CUM SOCIIS NATOQUE PENATIBUS ET MAGNIS DIS PARTURIENT MONTES, NASCETUR RIDICULUS MUS. DONEC QUAM FELIS, ULTRICIES NEC, PELLENTESQUE EU, PRETIUM QUIS, SEM. NULLA CONSEQUAT MASSA QUIS ENIM. DONEC PEDE JUSTO, FRINGILLA VEL, ALIQUET NEC, VULPUTATE EGET, ARCU. IN ENIM JUSTO, RHONCUS UT, IMPERDIET A, VENENATIS VITAE, JUSTO. NULLAM DICTUM FELIS EU PEDE MOLLIS PRETIUM. INTEGER TINCIDUNT. CRAS DAPIBUS. VIVAMUS ELEMENTUM SEMPER NISI. AENEAN VULPUTATE ELEIFEND TELLUS. AENEAN LEO LIGULA, PORTTITOR EU, CONSEQUAT VITAE, ELEIFEND AC, ENIM. ALIQUAM LOREM ANTE, DAPIBUS IN, VIVERRA QUIS, FEUGIAT A. "

.align 2
puntos: .space 200

my_data: .space 36000

.section .text


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

_start:

ldr r12, =puntos

mov r0, r12
ldr r1, =puntos
bl clear_points

breaking:

// Salir del programa
mov %r0, #0  // return val
mov %r7, #1   // exit system call magic number   
swi      #0   // Interupt / syscall
// b .

