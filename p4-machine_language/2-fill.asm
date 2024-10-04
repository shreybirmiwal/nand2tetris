

(LOOP)
@KBD
D=M

@BLACK
D;JNE //if D!=0, jump to @BLACK

@WHITE
D;JEQ


@LOOP
0;JMP




(BLACK)
@BLACKPoint
M=0 //out of 8191

(LOOPBLACK)
@BLACKPoint
D=M
@SCREEN
A=D+A

M=-1
@BLACKPoint
M=M+1

//check if we did all pixels
@BLACKPoint
D=M
@8191
D=D-A
@LOOPBLACK
D;JLT

@LOOP
0;JMP







(WHITE)
@WHITEPOINT
M=0

(LOOPWHITE)
@WHITEPOINT
D=M
@SCREEN
A=D+A

M=0
@WHITEPOINT
M=M+1

@WHITEPOINT
D=M
@8191
D=D-A
@LOOPWHITE
D;JLT

//whitepont = 3
//d = 3
//a=8191
//d = 3-8191
//loop if d is negative or 0

@LOOP
0;JMP