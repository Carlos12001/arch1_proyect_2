




# diccionario de registros
registers = {
    "r0": "0000",
    "r1": "0001",
    "r2": "0010",
    "r3": "0011",
    "r4": "0100",
    "r5": "0101",
    "r6": "0110",
    "r7": "0111",
    "r8": "1000",
    "r9": "1001",
    "r10": "1010",
    "r11": "1011",
    "r12": "1100",
    "sp": "1101",
    "lr": "1110",
    "pc": "1111"
}

# conditional flags
cond = {
    "eq": "0000",
    "ne": "0001",
    "ge": "1010",
    "lt": "1011",
    "le": "1101",
    "al": "1110",
}

# data processing intrucctions
data_intrucctions = {
    "sum": "1000",
    "com": "1010",
    "set": "1101",
    "dec": "0010",
    "divi": "1101",
    "xor": "0001",
    "aset": "1111",

}

# memory intrucctions
memory_intrucctions = {
    "stw": "00",
    "ldw": "01",
    "savepix": "10",
    "letter": "11"
}

# branch intrucctions
branch_intrucctions = {
    "b": "0",
    "bl": "1"
}

# special instrucctions
special_intrucctions = {
    "nop": "0000",
    "end": "1111"
}

# address values
address = {
    "text":     0x000,
    "puntos":   0x400,
    "my_data":  0x800,
}


def identify_specific_labels_and_instructions(file_path):
    # Inicializa las variables
    labels = {}
    instructions = []
    address = 0

    # Lee el archivo línea por línea
    with open(file_path, 'r') as asm_file:
        for line in asm_file:
            line = line.strip()
            # Ignora líneas en blanco
            if not line:
                continue

            # Si es un label (termina con ":")
            if line.endswith(':'):
                label = line[:-1]
                labels[label] = address
            else:
                # Si es una instrucción, agrégala y aumenta la dirección
                instructions.append(line)
                address += 4

    return labels, instructions

def write_output(output_path, labels, instructions):
    # Escribe las instrucciones sin los labels en el archivo de salida
    with open(output_path, 'w') as output_file:
        for instruction in instructions:
            output_file.write(f'{instruction}\n')

    # Opción: muestra los labels en la consola
    print("Labels encontrados:")
    for label, address in labels.items():
        print(f'{label}: {address:08x}')


# revisa si existe el registro en el diccionario
def translateReg(reg):
    pass
# revisa si existe la instruccion en el diccionario
def translateLabel(strLabel):
    pass

# revisa si existe el label en el diccionario
def translateImm8(strImm, lineCounter):
    pass

def translateImm12(strImm, lineCounter):
    pass

# compila la linea de instruccion
def compileLine(line:str):
    instrc = line.rsplit(",")
    bin = 0 # instruccion en binario 32 bits


    return bin
    

    
def main():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    # Initialize the GUI window and hide it
    Tk().withdraw()
    # Open a file selection dialog and get the file path
    file_path = askopenfilename(title='Select assembly file')
    if file_path: # If a file was selected
        output_path = file_path.replace('.txt', '.example')
        labels, instructions = identify_specific_labels_and_instructions(file_path)
        write_output(output_path, labels, instructions)
    

if __name__ == "__main__":
    main()