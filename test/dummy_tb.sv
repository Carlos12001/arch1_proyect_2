`timescale 1ns/1ps

module dummy_tb;

  // Señales de entrada
  logic a;
  logic b;
  logic c;

  // Señal de salida
  logic out;

  // Instancia del módulo and_top
  top_module uut (
    .a(a),
    .b(b),
    .c(c),
    .out(out)
  );

  // Estímulos de prueba
  initial begin
    // Caso de prueba 1
    a = 0;
    b = 0;
    c = 0;
    #10;
    $display("Caso 1: a=%b, b=%b, c=%b, out=%b", a, b, c, out);

    // Caso de prueba 2
    a = 1;
    b = 0;
    c = 1;
    #10;
    $display("Caso 2: a=%b, b=%b, c=%b, out=%b", a, b, c, out);

    // Caso de prueba 3
    a = 1;
    b = 1;
    c = 1;
    #10;
    $display("Caso 3: a=%b, b=%b, c=%b, out=%b", a, b, c, out);

    // Fin de la simulación
    $finish;
  end

endmodule