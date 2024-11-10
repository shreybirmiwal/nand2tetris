def handle_push_pop(tokens):
    if tokens[0] == 'push':
        if tokens[1] == 'constant':
            return f'//PUSH_CONSTANT\n@{tokens[2]}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
    
    return 

def handle_arithmetic(tokens):
    if tokens[0] == 'add':
        return f'//ADD\n@SP\nA=M\nA=A-1\nD=M\nA=A-1\nD=D+M\nM=D\n@SP\nM=M-1\n'
    return

def handle_logic(tokens):
    return


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

def processVM(vm_code_raw):

    vm_code_raw = vm_code_raw.split('\n')
    output = ""

    for line in vm_code_raw:

        # //Get Rid of Garabage stuff
        line = line.strip()
        if line == '':
            continue
        
        if line.startswith('//'):
            continue

        if r'//' in line:
            line = line.split('//')[0]
        # //////////////////////////
        

        tokens = line.split(' ')
        if tokens[0] == 'push' or tokens[0] == 'pop':
            output += handle_push_pop(tokens)
        if tokens[0] == 'add' or tokens[0] == 'sub':
            output += handle_arithmetic(tokens)
        if tokens[0] == 'neg' or tokens[0] == 'eq' or tokens[0] == 'gt' or tokens[0] == 'lt' or tokens[0] == 'and' or tokens[0] == 'or' or tokens[0] == 'not':
            output += handle_logic(tokens)


    return output


def main():
    file_path = './in/SimpleAdd.vm'
    vm_code_raw = read_file(file_path=file_path)
    out = processVM(vm_code_raw)
    
    print("################")
    print(out)
    with open('./out/SimpleAdd.asm', 'w') as file:
        file.write(out)


if __name__ == '__main__':
    main()