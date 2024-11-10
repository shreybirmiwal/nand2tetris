//d = stack[top]-stack[top-1]
@SP
A=M
A=A-1
D=M
A=A-1
D=D-M


//check if d == 0

@EQUAL
D;JEQ //jump if equal to zero (equal)

@NOTEQUAL
D;JMP //jump if not equal to zero 

(EQUAL)
@SP
A=M
A=A-2
M=-1 //set ram[SP-2] = -1 (bc equal)

@SP
M=M-1 //sp --;

@DONE
0;JMP //done now


(NOTEQUAL)
@SP
A=M
A=A-2
M=0

@SP
M=M-1

@DONE
0;JMP


(DONE)
@DONE
0;JMP