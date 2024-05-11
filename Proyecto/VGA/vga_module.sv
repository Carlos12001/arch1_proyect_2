module vga_module(
    input logic [7:0] pixel, 
    input logic clk,
    output logic vga_clk, 
    output logic h_sync, 
    output logic v_sync, 
    output logic sync_b, 
    output logic blank_b,  
    output logic [7:0] red, 
    output logic [7:0] green, 
    output logic [7:0] blue,
    output logic [9:0] x,
    output logic [9:0] y
);

    pll vga_pll(.clk(clk), .vga_clk(vga_clk));
    
    vga_controller vgaCont(
        .vga_clk(vga_clk),
        .h_sync(h_sync),
        .v_sync(v_sync),
        .sync_b(sync_b),
        .blank_b(blank_b),
        .x(x),
        .y(y)
    );
    
    generate_graphic gen_grid(
        .x(x),
        .y(y),
        .ReadData(pixel),
        .red(red),
        .green(green),
        .blue(blue)
    );

endmodule
