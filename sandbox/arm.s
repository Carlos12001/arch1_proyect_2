.global _start
.section .data
text: .ascii "LOREM IPSUM DOLOR SIT AMET, CONSECTETUER ADIPISCING ELIT. AENEAN COMMODO LIGULA EGET DOLOR. AENEAN MASSA. CUM SOCIIS NATOQUE PENATIBUS ET MAGNIS DIS PARTURIENT MONTES, NASCETUR RIDICULUS MUS. DONEC QUAM FELIS, ULTRICIES NEC, PELLENTESQUE EU, PRETIUM QUIS, SEM. NULLA CONSEQUAT MASSA QUIS ENIM. DONEC PEDE JUSTO, FRINGILLA VEL, ALIQUET NEC, VULPUTATE EGET, ARCU. IN ENIM JUSTO, RHONCUS UT, IMPERDIET A, VENENATIS VITAE, JUSTO. NULLAM DICTUM FELIS EU PEDE MOLLIS PRETIUM. INTEGER TINCIDUNT. CRAS DAPIBUS. VIVAMUS ELEMENTUM SEMPER NISI. AENEAN VULPUTATE ELEIFEND TELLUS. AENEAN LEO LIGULA, PORTTITOR EU, CONSEQUAT VITAE, ELEIFEND AC, ENIM. ALIQUAM LOREM ANTE, DAPIBUS IN, VIVERRA QUIS, FEUGIAT A. "

.align 2
puntos: .space 200

my_data: .space 36000











.section .text
_start:
  ldr r1, =my_data
  mov r0, #44 // ,
  bl generate_letter
  mov r1, r0
  mov r0, #65 // A
  bl generate_letter
  mov r1, r0
  mov r0, #32 // space
  bl generate_letter
  mov r1, r0
  mov r0, #46 // .
  bl generate_letter

  breaking:

  // Salir del programa
  mov %r0, #0  // return val
  mov %r7, #1   // exit system call magic number   
  swi      #0   // Interupt / syscall
  // b .











// FUNCTION generate_letter
// r0: char
// r1: posicion de memoria de la letra
generate_letter:
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



  // Inicializar la lista 'letter' con 255
  mov r4, r0
  mov r5, r1
  mov r0, r5
  bl set_pixel    // Usa 36 bytes osea 9 words
  ldr r12, =puntos

  // Switch CASE
  cmp r4, #32
  beq case_space
  
  // 44 (coma) ;
  cmp r4, #44
  beq case_comma

  // 46 (punto) .
  cmp r4, #46
  beq case_punto

  // 65 A
  cmp r4, #65
  beq case_a

  // Case Default
  b case_default
    
  case_space:
    b end_generate_letter

  case_comma:
    mov r0, #4
    mov r1, #1
    mov r2, #3
    mov r3, #2
    bl bresenham        
    
    b end_generate_letter

  case_punto:
    mov r0, #3
    mov r1, #2
    mov r2, #3
    mov r3, #2
    bl bresenham
    
    b end_generate_letter

  case_a:

    mov r0, #0
    mov r1, #1
    mov r2, #0
    mov r3, #3
    bl bresenham

    mov r0, #1
    mov r1, #0
    mov r2, #4
    mov r3, #0
    bl bresenham

    mov r0, #1
    mov r1, #4
    mov r2, #4
    mov r3, #4
    bl bresenham

    mov r0, #3
    mov r1, #1
    mov r2, #3
    mov r3, #3
    bl bresenham

    b end_generate_letter


  case_default:
    b end_generate_letter
      
  end_generate_letter:

  mov r0, r5
  mov r1, r12
  ldr r2, =puntos
  bl points2pixel
  add r0, r5, #36


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











// FUNCTION points2pixel
points2pixel:
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

  mov r4, r0          // r4 = letter
  mov r5, r1          // r5 = points_count
  mov r6, r2          // r6 = points
  mov r7, #0

  loop_points2pixel:
    ldr r0, [r6]        // Cargar x (word) desde points[i]
    ldr r1, [r6, #4]    // Cargar y (word) desde points[i+1]

    cmp r0, #0          // Comparar x con 0
    beq store_y         // Si x == 0, saltar a store_y

    cmp r0, #1          // Comparar x con 1
    addeq r1, r1, #6    // Si x == 1, sumar 6 a y
    beq store_y         // Saltar a store_y

    cmp r0, #2          // Comparar x con 2
    addeq r1, r1, #12   // Si x == 2, sumar 12 a y
    beq store_y         // Saltar a store_y

    cmp r0, #3          // Comparar x con 3
    addeq r1, r1, #18   // Si x == 3, sumar 18 a y
    beq store_y         // Saltar a store_y

    cmp r0, #4          // Comparar x con 4
    addeq r1, r1, #24   // Si x == 4, sumar 24 a y
    beq store_y         // Saltar a store_y

    b end_loop_points2pixel          // Si x no es válido, saltar al final del bucle

  store_y:
    strb r7, [r4, r1]   // Almacenar 1 en letter[y] (byte)

  end_loop_points2pixel:
    add r6, r6, #8      // Avanzar al siguiente par de puntos (x, y)
	  cmp r6, r5 // Comparar points con points_count
	  blt loop_points2pixel // Saltar si points < points_count

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











// FUNCTION ABS
abs:
asr r1, r0, #0x1f // r1 = r0 >> 31
add r2, r0, r1 // r2 = (r0 + r1)
eor r3, r2, r1 // r3 = r2 ^ r1
mov r0, r3     
mov pc, lr        // return










