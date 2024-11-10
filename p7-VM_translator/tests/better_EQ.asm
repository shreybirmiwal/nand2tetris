// d = stack[top]-stack[top-1]
@SP
A=M-1
D=M
A=A-1
D=D-M

// check if d == 0
@EQUAL
D;JEQ // jump if equal to zero (equal)

// Not equal
@SP
A=M-2
M=0
@END
0;JMP

(EQUAL)
@SP
A=M-2
M=-1 // set ram[SP-2] = -1 (bc equal)

(END)
@SP
M=M-1 // sp--