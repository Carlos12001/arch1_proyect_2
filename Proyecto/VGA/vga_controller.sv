module vga_controller #(
    parameter HACTIVE = 10'd256,
    parameter HFP = 10'd192,
    parameter HSYN = 10'd48,
    parameter HBP = 10'd192,
    parameter HMAX = HACTIVE + HFP + HSYN + HBP,
    parameter VBP = 10'd112,
    parameter VACTIVE = 10'd256,
    parameter VFP = 10'd112,
    parameter VSYN = 10'd2,
    parameter VMAX = VACTIVE + VFP + VSYN + VBP
)
(
    input logic vga_clk,
    output logic h_sync, v_sync, sync_b, blank_b,
    output logic [9:0] x, y,
	 output logic [15:0] access
);


    initial begin
        x = 0;
        y = 0;
        access = 0;
    end

    // Counters for horizontal and vertical positions
    always @(posedge vga_clk) begin
        x++;
		  access++;
        if (x % 6 == 0) begin
            access += 35;
        end

        if (x == HMAX) begin
            x = 0;
            y++;
				access = {y[7:0], x[7:0]};
            if (y == VMAX) y = 0;
        end
		  
		  if (access%65536==0) access = {y[7:0], x[7:0]};

    end

    // Compute sync signals (active low)
    assign h_sync = ~(x >= HACTIVE + HFP & x < HACTIVE + HFP + HSYN);
    assign v_sync = ~(y >= VACTIVE + VFP & y < VACTIVE + VFP + VSYN);
    assign sync_b = h_sync & v_sync;

    // Force outputs to black when outside the legal display area
    assign blank_b = (x < HACTIVE) & (y < VACTIVE);

endmodule