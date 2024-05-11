module TopModule(
    input logic clk,
    input logic rst,
	 input  logic        reset,
    output logic vga_clk,
    output logic h_sync, v_sync,
    output logic sync_b, blank_b,
    output logic [7:0] red, green, blue,
	 output logic [31:0] WriteDataM, DataAdrM,
    output logic        MemWriteM
);


	  logic [31:0] PCF, InstrF, ReadDataM;

	  // instantiate processor and memories
	  arm arm(clk, reset, PCF, InstrF, MemWriteM, DataAdrM, WriteDataM, ReadDataM);
	  
	  imem imem(PCF, InstrF);

	  //dmem dmem(clk, MemWriteM, DataAdrM, WriteDataM, ReadDataM);

	  RAMMemory ram1(
		 .clock(clk),
		 .wren(MemWriteM),
		 .address(DataAdrM),
		 .data(WriteDataM),
		 .q(ReadDataM)
	  );



 logic [9:0] x, y;
    logic [31:0] pixel;
    logic [7:0] ram_pixel, ram2_pixel;
    logic [15:0] access; 

    pll vga_pll(.clk(clk), .vga_clk(vga_clk));

    // Instanciamos vga_controller con `access`
    vga_controller vgaCont(
        .vga_clk(vga_clk),
        .h_sync(h_sync),
        .v_sync(v_sync),
        .sync_b(sync_b),
        .blank_b(blank_b),
        .x(x),
        .y(y)
    );

    RAM ram(
        .clock(vga_clk),
        .rdaddress({y[7:0], x[7:0]}),
        .wraddress(16'h0000),
        .wren(1'b0),
        .q(ram_pixel)
    );

    RAM2 ram2(
        .clock(vga_clk),
        .address({y[7:0], x[7:0]}),
        .data(8'b0),
        .wren(1'b0),
        .q(ram2_pixel)
    );

    always_comb begin
        if (rst) begin
            pixel = {24'b0, ram2_pixel};
        end else begin
            pixel = {24'b0, ram_pixel};
        end
    end

    generate_graphic gen_grid(
        .x(x),
        .y(y),
        .ReadData(pixel[7:0]),
        .red(red),
        .green(green),
        .blue(blue)
    );

endmodule
