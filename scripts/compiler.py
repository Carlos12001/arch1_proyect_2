
specific_labels = {
    "_start",
    "main_loop",
    "generate_letter",
    "end_program",
    "case_space",
    "case_comma",
    "case_punto",
    "case_a",
    "case_b",
    "case_c",
    "case_d",
    "case_e",
    "case_f",
    "case_g",
    "case_h",
    "case_i",
    "case_j",
    "case_k",
    "case_l",
    "case_m",
    "case_n",
    "case_o",
    "case_p",
    "case_q",
    "case_r",
    "case_s",
    "case_t",
    "case_u",
    "case_v",
    "case_w",
    "case_x",
    "case_y",
    "case_z",
    "set_pixel",
    "set_pixel_for",
    
    
    "bresenham",
    
    "if_x_compare",
    "else_x_compare",
    "end_if_x_compare",
    "if_y_compare",
    "else_y_compare",
    "end_if_y_compare",
    "if_differentials",
    "while_dx_bigger",
    "if_while_dx_bigger",
    "end_if_while_dx_bigger",
    "end_while_dx_bigger",
    "else_differentials",
    "while_dy_bigger",
    "if_while_dy_bigger",
    "end_if_while_dy_bigger",
    "end_while_dy_bigger",
    "end_if_differentials",
    "abs"
}





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
    "add": "1000",
    "cmp": "1010",
    "mov": "1101",
    "sub": "0010",
    "asr": "1101",
    "eor": "0001",
    "mvn": "1111",

}

# memory intrucctions
memory_intrucctions = {
    "str": "0100",
    "ldr": "0101",
    "strb": "0110",
    "ldrb": "0111"
}

# branch intrucctions
branch_intrucctions = {
    "b": "10",
    "bl": "11"
}

# special instrucctions
special_intrucctions = {
    "nop": "0000",
    "end": "1111"
}

# address values
address = {
    "text": "0000",
    "puntos": "0001",
    "my_data": "0010",
}


# labels
labels = {
 
}


def count_instruction(stripped_line):
    """
    Función auxiliar para determinar el tamaño de cada instrucción.
    No se jaja, a cada instrucción se le da :) mmm 4 bytes.
    """
    return 4


def identify_specific_labels(raw_txt):
    """Identifica etiquetas con su posición de memoria correspondiente"""
    memory_counter = 0x00
    for line in raw_txt:
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#"):
            continue
        # Separa la primera palabra (instrucción o etiqueta)
        first_word = stripped_line.split(",")[0].split()[0]
        # Si es una etiqueta específica
        if stripped_line.endswith(":") and first_word.replace(":", "") in specific_labels:
            label_name = first_word.replace(":", "")
            labels[label_name] = memory_counter
        else:
            memory_counter += count_instruction(stripped_line)
    return labels


# Leer el archivo y limpia los saltos de linea
def read_txt(path):
    with open(path, "r") as file:
        rawInstrc = [line.rstrip("\n").replace(",", "") for line in file]
    return rawInstrc

# revisa si existe el registro en el diccionario
def translateReg(reg):
    if reg not in registers:
        print(f"Error: {reg} no es un registo valido")
        exit()
    else:
        return registers[reg]

# revisa si existe la instruccion en el diccionario
def translateLabel(strLabel):
    if strLabel not in labels:
        print(f"Error: {strLabel} no es un label valido")
        exit()
    else:
        return labels[strLabel]

# revisa si existe el label en el diccionario
def checkImmLabel(strImm, lineCounter):
    cleanLabel = strImm.replace(":", "")
    exists = labels.get(cleanLabel)
    if not exists:
        # por que es 15 bits?
        labels[cleanLabel] = format(int(lineCounter), "013b") 
    else:
        print("label ya existe")

# compila la linea de instruccion
def compileLine(line:str):
    instrc = line.rsplit(",")
    bin = 0 # instruccion en binario 32 bits
 
    # tipo immediate
    if instrc[0] == "CPI":
        regDes = translateReg(instrc[1])
        # instrc[3] es un numero entero a binario pero limitando a 13 bits
        imm = format(int(instrc[2]), "013b")
        func3 = "000" # definir que hacer
        opcode = data_intrucctions[instrc[0]]
        # retornar binInstrc con el formato imm Func3 regDes opcode
        bin = imm + func3 + regDes + opcode
        return bin
    # tipo I
    elif instrc[0] == "NP":
        regDes = translateReg("z0")
        rs1 = translateReg("z0")
        # instrc[3] es un numero entero a binario pero limitando a 13 bits
        imm = format(int(0), "013b")
        func3 = "000" # definir que hacer
        opcode = data_intrucctions[instrc[0]]
        bin = imm + func3 + rs1 + regDes + opcode
        return bin
    
    elif instrc[0] == "DME":
        regDes = translateReg(instrc[1])
        rs = translateReg(instrc[2])
        rs2 = "000000"
        func3 = "000"
        func7 = "0000000"
        opcode = data_intrucctions[instrc[0]]
        bin = func7 + func3 + rs2 + rs + regDes + opcode
        return bin
def getLabels():
    pass

def checkImmLabel(label, memoryAddress, labels):
    labelName = label.strip().replace(":", "")
    labels[labelName] = memoryAddress
    
def main():
   
    file_path = "C:/Users/Felipe vargas/Downloads/arch1_proyect_2-1/scripts/arm.txt"
    with open(file_path, "r") as file:
        raw_txt = file.readlines()

    # Identifica las etiquetas específicas
    identify_specific_labels(raw_txt)

    # Imprime las etiquetas y su dirección
    print("labels = {")
    for label, address in sorted(labels.items(), key=lambda x: x[1]):
        print(f'    "{label}": 0x{address:02X},')
    print("}")

if __name__ == "__main__":
    main()