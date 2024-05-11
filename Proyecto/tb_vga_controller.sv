`timescale 1ns / 1ps

module tb_vga_controller;

    // Definición de parámetros para el módulo
    parameter HACTIVE = 10'd256;
    parameter HFP = 10'd192;
    parameter HSYN = 10'd48;
    parameter HBP = 10'd192;
    parameter HMAX = HACTIVE + HFP + HSYN + HBP;
    parameter VBP = 10'd112;
    parameter VACTIVE = 10'd256;
    parameter VFP = 10'd112;
    parameter VSYN = 10'd2;
    parameter VMAX = VACTIVE + VFP + VSYN + VBP;

    // Señales para el módulo
    reg vga_clk;
    wire h_sync, v_sync, sync_b, blank_b;
    wire [9:0] x, y;
    wire [15:0] access;

    // Instancia del módulo VGA controller
    vga_controller #(
        .HACTIVE(HACTIVE),
        .HFP(HFP),
        .HSYN(HSYN),
        .HBP(HBP),
        .HMAX(HMAX),
        .VBP(VBP),
        .VACTIVE(VACTIVE),
        .VFP(VFP),
        .VSYN(VSYN),
        .VMAX(VMAX)
    ) uut (
        .vga_clk(vga_clk),
        .h_sync(h_sync),
        .v_sync(v_sync),
        .sync_b(sync_b),
        .blank_b(blank_b),
        .x(x),
        .y(y),
        .access(access)
    );

    // Generador de reloj VGA
    initial begin
        vga_clk = 0;
        forever #10 vga_clk = ~vga_clk; // Periodo de 20 ns (50 MHz)
    end

    // Proceso de simulación
    initial begin
        // Inicialización
        $display("Iniciando simulación...");

        // Simulación por un tiempo específico
        #500000;

        // Finaliza la simulación
        $stop;
    end

    // Monitor para observar los valores de interés
    initial begin
        $monitor("Tiempo: %0d | h_sync: %b, v_sync: %b, sync_b: %b, blank_b: %b, x: %d, y: %d, access: %d",
                 $time, h_sync, v_sync, sync_b, blank_b, x, y, access);
    end

endmodule
