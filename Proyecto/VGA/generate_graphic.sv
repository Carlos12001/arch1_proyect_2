module generate_graphic (
    input logic [9:0] x, y,
    input logic [7:0] ReadData,
    output logic [7:0] red, green, blue
);

    logic inrectImage;
    
    generate_rectangle rectImage(
        .x(x),
        .y(y),
        .left(10'd0),
        .top(10'd0),
        .right(10'd256),
        .bottom(10'd256),
        .in_rectangle(inrectImage)
    );
    
    always_comb begin
        red   = (inrectImage ? ReadData : 2'b00);
        green = (inrectImage ? ReadData : 2'b00);
        blue  = (inrectImage ? ReadData : 2'b00);
    end

endmodule
