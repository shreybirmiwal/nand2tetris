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

        print(line)
    return output
    

def main():
    file_path = './in/add.asm'
    assembly_code_raw = read_file(file_path=file_path)

    #print(assembly_code_raw)
    out = processAssemblyCode(assembly_code_raw)
    print("################")
    print(out)


if __name__ == '__main__':
    main()