from typing import List


class CodeWriter:
    def __init__(self):
        self.output = open('output.asm', 'w')

    def __write_init(self):
        self.output.write(f'@256\n'
                          f'D=A\n'
                          f'@SP\n'
                          f'M=D\n')
        self.__write_call(['call', 'Sys.init'])

    def __write_label(self, command: List[str]):
        self.output.write(f'({command[1]})\n')

    def __write_goto(self, command: List[str]):
        self.output.write(f'@{command[1]}'
                          f'0;JMP\n')

    def __write_if(self, command: List[str]):
        self.output.write(f'@SP\n'
                          f'AM=M-1\n'
                          f'D=M\n'
                          f'@{command[1]}\n'
                          f'D;JNE\n')

    def __write_call(self, command: List[str]):
        if len(command) == 2:
            command.append('0')
        self.output.write(f'@RETURN_{command[1]}_LABEL\n'
                          f'D=A\n'
                          f'@SP\n'
                          f'A=M\n'
                          f'M=D\n'
                          f'@LCL\n'
                          f'D=M\n'
                          f'@SP\n'
                          f'AM=M+1\n'
                          f'M=D\n'
                          f'@ARG\n'
                          f'D=M\n'
                          f'@SP\n'
                          f'AM=M+1\n'
                          f'M=D\n'
                          f'@THIS\n'
                          f'D=M\n'
                          f'@SP\n'
                          f'AM=M+1\n'
                          f'M=D\n'
                          f'@THAT\n'
                          f'D=M\n'
                          f'@SP\n'
                          f'AM=M+1\n'
                          f'M=D\n'
                          f'@SP\n'
                          f'M=M+1\n'
                          f'@5\n'
                          f'D=A\n'
                          f'@{command[2]}\n'
                          f'D=D+A\n'
                          f'@ARG\n'
                          f'M=D\n'
                          f'@SP\n'
                          f'D=M\n'
                          f'@LCL\n'
                          f'M=D\n'
                          f'@{command[1]}\n'
                          f'0;JMP\n'
                          f'(RETURN_{command[1]}_LABEL)\n')

    def __write_function(self, command: List[str]):
        self.output.write(f'({command[1]})\n'
                          f'@{command[2]}\n'
                          f'D=A\n'
                          f'@{command[1]}_nVars\n'
                          f'M=D\n'
                          f'({command[1]}_LCL_INIT)\n'
                          f'@{command[1]}_nVars\n'
                          f'D=M\n'
                          f'@{command[1]}_LCL_INIT_END\n'
                          f'D;JEQ\n'
                          f'@SP\n'
                          f'A=M\n'
                          f'M=0\n'
                          f'@SP\n'
                          f'M=M+1\n'
                          f'@{command[1]}_nVars\n'
                          f'M=M-1\n'
                          f'@({command[1]}_LCL_INIT)\n'
                          f'0;JMP\n'
                          f'({command[1]}_LCL_INIT_END)\n')

    def __write_return(self, command: List[str]):
        self.output.write(f'@LCL\n'
                          f'D=M\n'
                          f'@END_FRAME\n'
                          f'M=D\n'
                          f'@RET_ADDR\n'
                          f'M=D\n'
                          f'@5\n'
                          f'D=A\n'
                          f'@RET_ADDR\n'
                          f'A=M-D\n'
                          f'D=M\n'
                          f'@RET_ADDR\n'
                          f'M=D\n'
                          f'@SP\n'
                          f'A=M-1\n'
                          f'D=M\n'
                          f'@ARG\n'
                          f'A=M\n'
                          f'M=D\n'
                          f'@ARG\n'
                          f'D=A+1\n'
                          f'@SP\n'
                          f'M=D\n'
                          f'@END_FRAME\n'
                          f'D=M-1\n'
                          f'A=D\n'
                          f'D=M\n'
                          f'@THAT\n'
                          f'M=D\n'
                          f'@2\n'
                          f'D=A\n'
                          f'@END_FRAME\n'
                          f'D=M-D\n'
                          f'A=D\n'
                          f'D=M\n'
                          f'@THIS\n'
                          f'M=D\n'
                          f'@3\n'
                          f'D=A\n'
                          f'@END_FRAME\n'
                          f'D=M-D\n'
                          f'A=D\n'
                          f'D=M\n'
                          f'@ARG\n'
                          f'M=D\n'
                          f'@4\n'
                          f'D=A\n'
                          f'@END_FRAME\n'
                          f'D=M-D\n'
                          f'A=D\n'
                          f'D=M\n'
                          f'@LCL\n'
                          f'M=D\n'
                          f'@RET_ADDR\n'
                          f'0;JMP\n')
