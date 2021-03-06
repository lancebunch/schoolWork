`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/23/2020 11:08:37 AM
// Design Name: 
// Module Name: clk_gen
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module clk_gen(input clk, input rst, output clk_div);
    
    // Our 26 bit counter
    reg [26:0] cnt; 
    
    // Clock output port
    assign clk_div = cnt[18];
    // Setting our cnt to 0;
    initial begin cnt <= 27'b000000000000000000000000000; end
    
    // Creating a loop that is activated at each clk
    // cycle or reset btn push. If the reset button
    // is pushed it will set cnt back to 0. Otherwise
    // cnt is going to continually increment itself
    // by 1 bit each cycle.
    always @ (posedge clk or negedge rst) begin
        if (rst) cnt <= 27'b000000000000000000000000000;
        else cnt <= cnt + 27'b000000000000000000000000001;
    end
    
endmodule
