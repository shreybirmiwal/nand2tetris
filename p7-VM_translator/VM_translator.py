def handle_push_pop(tokens):
    return 

def handle_arithmetic(tokens):
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
        if tokens[0] == 'push' | tokens[0] == 'pop':
            output += handle_push_pop(tokens)
        if tokens[0] == 'add' | tokens[0] == 'sub':
            output += handle_arithmetic(tokens)
        if tokens[0] == 'neg' | tokens[0] == 'eq' | tokens[0] == 'gt' | tokens[0] == 'lt' | tokens[0] == 'and' | tokens[0] == 'or' | tokens[0] == 'not':
            output += handle_logic(tokens)


    return vm_code_raw


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