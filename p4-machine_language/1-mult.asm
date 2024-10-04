//a = ram[0]
//b = ram[1]
//return a*b in ram[2]


@R2
M=0


//make new variable, i
@1
D=M
@i
M=D



(LOOP)

//check if b<=0
@i
D=M  //d = i
@END //a = end
D;JLE //if D <=0, jump to a (end)



@R0
D=M
@R2
M=D+M

@i
M=M-1

@LOOP
0;JMP

(END)
@i
M=0