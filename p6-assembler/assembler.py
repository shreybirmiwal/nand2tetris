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


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def processAssemblyCode(assembly_code_raw):
    output = ""
    assembly_code = assembly_code_raw.split('\n')
    for line in assembly_code:
        line = line.strip()
        if line == '':
            continue
        
        if line.startswith('//'):
            continue

        if r'//' in line:
            line = line.split('//')[0] # Remove comments

        if line.startswith('@'):
            #print('A instruction')
            num_in_decimal = line[1:]
            num_in_binary = bin(int(num_in_decimal))[2:].zfill(15)  # Padded to 15 total digits, [2:] to remove '0b'

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
    file_path = './in/rectl.asm'
    assembly_code_raw = read_file(file_path=file_path)

    #print(assembly_code_raw)
    out = processAssemblyCode(assembly_code_raw)
    print("################")
    print(out)
    with open('./out/rectl.hack', 'w') as file:
        file.write(out)


if __name__ == '__main__':
    main()