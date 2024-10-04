

(LOOP)

@KBD
D=M
@BLACK
D;JNE //if D!=0, jump to @BLACK (no keyboard input, show white)

@SCREEN
M=0

@LOOP
0;JMP


(BLACK)
@SCREEN
M=-1
@LOOP
0;JMP