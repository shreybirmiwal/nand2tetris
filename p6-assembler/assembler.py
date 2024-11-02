#table of values of 'compute' bits for C instruct
comp_dict = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000',
    '!D': '001101',
    '!A': '110001',
    '-D': '001111',
    '-A': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'D+A': '000010',
    'D-A': '010011',
    'A-D': '000111',
    'D&A': '000000',
    'D|A': '010101',

    'M': '110000',
    '!M': '110001',
    '-M': '110011',
    'M+1': '110111',
    'M-1': '110010',
    'D+M': '000010',
    'D-M': '010011',
    'M-D': '000111',
    'D&M': '000000',
    'D|M': '010101',

}

labels = {

    # predifined labels below

    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,


    'SCREEN': 16384,
    'KBD': 24576,   
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,

    ## end pre defined above 

        
}


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def preprocessLabels(assembly_code_raw):
    rom_address = 0
    for line in assembly_code_raw:
        line = line.strip()
        if line == '' or line.startswith('//'):
            continue
        if '//' in line:
            line = line.split('//')[0].strip()
        
        if line.startswith('('):
            label = line[1:-1]
            labels[label] = rom_address
        else:
            rom_address += 1
    
    print("Labels: ")   
    print(labels)
    return assembly_code_raw

    
def processAssemblyCode(assembly_code_raw):
    assembly_code_raw = preprocessLabels(assembly_code_raw)
    output = ""
    next_variable_address = 16

    for line in assembly_code_raw:
        line = line.strip()
        if line == '':
            continue
        
        if line.startswith('//'):
            continue

        if r'//' in line:
            line = line.split('//')[0] # Remove comments
        
        if line.startswith('('):
            continue
            

        if line.startswith('@'):
            num_or_symbol = line[1:]
            if num_or_symbol.isdigit():
                num_in_decimal = int(num_or_symbol)
            elif num_or_symbol in labels:
                num_in_decimal = labels[num_or_symbol]
            else:
                # It's a new variable
                if num_or_symbol not in labels:
                    labels[num_or_symbol] = next_variable_address
                    next_variable_address += 1
                num_in_decimal = labels[num_or_symbol]
            
            num_in_binary = bin(num_in_decimal)[2:].zfill(15)
            temp_out = '0' + num_in_binary + '\n'
            output += temp_out
        else:
            print("C instruction")
            val = '111' #c instruction start, first 3 bits


            
            #comp bits (5-12 bits)
            comp = line
            if '=' in line:
                comp = line.split('=')[1]
            if ';' in comp:
                comp = comp.split(';')[0]


            #a bit (4nd bit)
            if "M" in comp: #this means 'a' bit = 1
                val += '1'
            else:
                val += '0'

            #adding C bits here
            val += comp_dict[comp]

            #dest bits (13-15 bits)
            dest = ''
            if '=' in line:
                dest = line.split('=')[0]
            if dest == '':
                dest = 'null'
            if 'A' in dest:
                val += '1'
            else:
                val += '0'
            if 'D' in dest:
                val += '1'
            else:
                val += '0'
            if 'M' in dest:
                val += '1'
            else:
                val += '0'

            #jump bits (16-18 bits)
            jump = ''
            if ';' in line:
                jump = line.split(';')[1]
            if jump == '':
                jump = 'null'
            if jump == 'null':
                val += '000'
            if jump == 'JGT':
                val += '001'
            if jump == 'JEQ':
                val += '010'
            if jump == 'JGE':
                val += '011'
            if jump == 'JLT':
                val += '100'
            if jump == 'JNE':
                val += '101'
            if jump == 'JLE':
                val += '110'
            if jump == 'JMP':
                val += '111'

            temp_out = val + '\n'
            output += temp_out
            #print(val)
                        
            


        print(line)
    return output
    

def main():
    file_path = './in/max.asm'
    assembly_code_raw = read_file(file_path=file_path)
    out = processAssemblyCode(assembly_code_raw)
    
    print("################")
    print(out)
    with open('./out/max.hack', 'w') as file:
        file.write(out)


if __name__ == '__main__':
    main()