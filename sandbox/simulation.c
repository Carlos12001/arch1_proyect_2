#include "stdio.h"
#include "stdlib.h"

// ASSEMBLY CODE
int my_abs(int r0) {
  int r1 = r0 >> 31;
  int r2 = (r0 + r1);
  int r3 = r2 ^ r1;
  return r3;
}
/**
 * bresenham
 * r0 = x1
 * r1 = y1
 * r2 = x2
 * r3 = y2
 * letter_memory (r4) no importa si es rescrito
 * porque al final se devuelve el puntero
 */
int *bresenham(int r0, int r1, int r2, int r3, void *letter_memory) {
  int r4 = 0, r5 = 0, r6 = 0, r7 = 0, r8 = 0, r9 = 0, r10 = 0, r11 = 0,
      *r12 = letter_memory;

  r4 = r0;  // x1
  r5 = r1;  // y1
  r6 = r2;  // x2
  r7 = r3;  // y2

  r0 = r6 - r4;
  r0 = my_abs(r0);
  r8 = r0;  // dx = abs(x2 - x1)
  r0 = r7 - r5;
  r0 = my_abs(r0);
  r9 = r0;  // dy = abs(y2 - y1)

  r10 = r4;  // x = x1
  r11 = r5;  // y = y1

if_x_compare:  // x1 > x2
  if (r4 <= r6) goto else_x_compare;
  r4 = -1;  // sx = -1
else_x_compare:
  r4 = 1;  // sx = 1

if_y_compare:  // y1 > y2
  if (r5 <= r7) goto else_y_compare;
  r5 = -1;  // sy = -1
else_y_compare:
  r5 = 1;  // sy = 1

if_differentials:  // dx > dy
  if (r8 <= r9) goto else_differentials;
  r0 = r8 >> 1;   // dx >> 1 === dx/2
while_dx_bigger:  // while (x != x2)
  if (r10 == r6) goto end_while_dx_bigger;

  *r12 = r10;  // save x
  r12 = r12 + 1;
  *r12 = r11;     // save y
  r12 = r12 + 1;  // increment counter

  r0 = r0 - r9;      // err -= dy
if_while_dx_bigger:  // if (err < 0)
  if (r0 >= 0) goto end_if_while_dx_bigger;

  r11 = r11 + r5;  // y += sy
  r0 = r0 + r8;    // err += dx
end_if_while_dx_bigger:
  r10 = r10 + r4;  // x += sx
  goto while_dx_bigger;
end_while_dx_bigger:
  goto end_if_differentials;

else_differentials:
  r0 = r9 >> 1;   // dy >> 1 === dy/2
while_dy_bigger:  // while (y != y2)
  if (r11 == r7) goto end_while_dy_bigger;

  *r12 = r10;  // save x
  r12 = r12 + 1;
  *r12 = r11;     // save y
  r12 = r12 + 1;  // increment counter

  r0 = r0 - r8;      // err -= dx
if_while_dy_bigger:  // if (err < 0)
  if (r0 >= 0) goto end_if_while_dy_bigger;

  r10 = r10 + r4;  // x += sx
  r0 = r0 + r9;    // err += dy
end_if_while_dy_bigger:
  r11 = r11 + r5;  // y += sy
  goto while_dy_bigger;
end_while_dy_bigger:
  goto end_if_differentials;

end_if_differentials:
  *r12 = r6;  // save x
  r12 = r12 + 1;
  *r12 = r7;      // save y
  r12 = r12 + 1;  // increment counter

  // pop all the registers
  return r12;
}

int start(void *ascii_mem, void *letter_mem, void *result_mem) { return 0; }
// FPGA CODE

// C Code for view simulation
void print_letter_mem(int *letter_mem) {
  printf("[\n");
  for (unsigned int i = 0; i < 50; i += 2) {
    if ((i) % 10 == 0 && i != 0) printf("\n");
    printf("(%d, %d), ", letter_mem[i], letter_mem[i + 1]);
  }
  printf("\n]\n");
}

int main() {
  int number_of_letters = 1;
  int num_elements = 25;
  int size_of_element = 4;  // 4 bytes = 32 bits

  void *letter_memory =
      malloc(number_of_letters * num_elements * size_of_element * 2);

  if (letter_memory == NULL) {
    // En caso de que malloc falle, imprimir error y salir
    printf("No se pudo asignar memoria.\n");
    return -1;
  }

  bresenham(0, 1, 0, 3, letter_memory);

  print_letter_mem(letter_memory);
  return 0;
}
