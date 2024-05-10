




# diccionario de registros
registers = {
    "v0": "0000",
    "v1": "0001",
    "v2": "0010",
    "v3": "0011",
    "v4": "0100",
    "v5": "0101",
    "v6": "0110",
    "v7": "0111",
    "v8": "1000",
    "v9": "1001",
    "v10": "1010",
    "v11": "1011",
    "v12": "1100",
    "sk": "1101",
    "lk": "1110",
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
data_instructions = {
    "sum": "0100",
    "com": "1010",
    "set": "1101",
    "dec": "0010",
    "divi": "1101",
    "xor": "0001",
    "aset": "1111",

}

# memory intrucctions
memory_instructions = {
    "stw": "00",
    "ldw": "01",
    "savepix": "10",
    "letter": "11"
}

# branch intrucctions
branch_instructions = {
    "b": "10",
    "bl": "11"
}

# special instrucctions
special_instructions = {
    "nop": "0000",
    "end": "1111"
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

            # Reemplaza el carácter " " por ""
            line = line.replace(" ", "")

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
    # Escribe las instrucciones en formato .mif
    with open(output_path, 'w') as output_file:
        # output_file.write("WIDTH=32;\n")
        # output_file.write(f"DEPTH={len(instructions)};\n")
        # output_file.write("ADDRESS_RADIX=HEX;\n")
        # output_file.write("DATA_RADIX=HEX;\n")
        # output_file.write("CONTENT BEGIN\n")

        for address, instruction in enumerate(instructions):
            bin_instr = compileLine(instruction, labels, address*4)
            hex_instr = f"{int(bin_instr, 2):08X}"
            # output_file.write(f"{address:X} : {hex_instr};\n")
            output_file.write(f"{hex_instr}\n")

        # output_file.write("END;\n")



  # Ajustar el inmediato a imm8 y rot
def calculate_imm8_and_rot(value):
    for rot in range(0, 32, 2):
        imm8 = (value >> rot) & 0xFF
        if value == ((imm8 << rot) | (imm8 >> (32 - rot))) & 0xFFFFFFFF:
            return f"{rot // 2:04b}", f"{imm8:08b}"
    raise ValueError(f"Immediato {value} fuera de rango")

# compila la linea de instruccion
def compileLine(line: str, labels: dict, address: int):
    instrc = line.split(",")
    bin_instr = ""
    cond_bin = cond.get("al", "1110")  # Default condicional
    try:
        # Data Processing Instructions
        if instrc[0] in data_instructions:
            opcode_bin = "00"
            has_flag = False

            # Verificar si hay un condicional explícito (flag)
            if instrc[1] in cond:
                cond_bin = cond[instrc[1]]
                has_flag = True
            
            num_registers = sum(1 for instr in instrc if instr in registers) 
            if num_registers == 3 or num_registers == 2:
                # Identificar los índices para los registros
                rd_index = 2 if has_flag else 1
                rn_index = 3 if has_flag else 2
                src2_index = 4 if has_flag else 3

                # Obtener los registros de destino (Rd) y fuente (Rn)
                rd_bin = registers[instrc[rd_index]]
                rn_bin = registers[instrc[rn_index]]
            elif num_registers == 1:
                if instrc[0] == "set" or instrc[0] == "aset" or instrc[0] == "com":
                    # Identificar los índices para los registros
                    rn_index = 2 if has_flag else 1
                    src2_index = 3 if has_flag else 2
                    # Obtener los registros de destino (Rd) y fuente (Rn)
                    rd_bin = "0000" 
                    rn_bin = registers[instrc[rn_index]]

                else:
                    raise ValueError("Solo las instrucciones 'set', 'com' y 'aset' pueden tener un solo registro de destino")
            else:
                raise ValueError("Numero de registros no valido = {num_registers}")

            # Identificar si Operand2 es inmediato o no (I-bit)
            is_immediate = instrc[src2_index].startswith("#") if len(instrc) > src2_index else False
            i_bit = "1" if is_immediate else "0"

            # Operand2
            if is_immediate:
                imm_value = instrc[src2_index].replace("#", "")
                immediate = int(imm_value)
                rot_bin, imm8_bin = calculate_imm8_and_rot(immediate)
                operand2_bin = f"{rot_bin}{imm8_bin}"
            else:
                rm_bin = registers[instrc[src2_index]] if num_registers == 3 else "0000"
                if instrc[0] == "divi":  # ASR
                    shift_type_bin = "10"  # ASR
                    shamt5_bin = "00000"  # Valor por defecto para shamt5
                    if instrc[src2_index].startswith("#"):
                        shamt5_value = int(instrc[src2_index].replace("#", ""))
                        shamt5_bin = f"{shamt5_value:05b}"
                        rm_bin = instrc[rm_bin]
                    else:
                        shamt5_bin = instrc[src2_index]
                    
                    operand2_bin = f"{shamt5_bin}{shift_type_bin}0{rm_bin}"
                else:
                    operand2_bin = f"00000000{rm_bin}"

            # Flags (S-bit)
            s_bit = "1" if instrc[0] in ["com"] else "0"

            # Construir la instrucción en binario
            bin_instr = f"{cond_bin}{opcode_bin}{i_bit}{data_instructions[instrc[0]]}{s_bit}{rn_bin}{rd_bin}{operand2_bin}"


        # Memory Instructions
        elif instrc[0] in memory_instructions:
            opcode_bin = "01"
            
            # Identificar el tipo de instrucción de memoria
            funct_bin = memory_instructions[instrc[0]]
            
            # Obtener los registros de destino (Rd) y base (Rn)
            rd_bin = registers[instrc[1]]
            rn_bin = registers[instrc[2]]
            
            # Establecer los bits P, W
            p_bit = "1"
            w_bit = "0"


            b_bit = funct_bin[0]
            l_bit = funct_bin[1]
            scr2 = "000000000000"
            
            # Verificar si hay un offset inmediato, un registro o ninguno
            if len(instrc) == 4:
                if instrc[3].startswith("#"):
                    # Offset inmediato
                    offset_str = instrc[3].replace("#", "")
                    offset = int(offset_str)
                    
                    # Verificar el rango del offset (0 a 4095)
                    if offset < 0 or offset > 4095:
                        raise ValueError(f"Offset {offset} fuera de rango para instrucción de memoria")
                    
                    # Convertir el offset a binario (12 bits)
                    scr2 = f"{offset:012b}"
                    
                    # Establecer los bits I, U, B
                    i_bit = "0"
                    u_bit = "1"  # Siempre positivo
  
                
                    
                else:
                    # Offset con registro
                    rm_bin = registers[instrc[3]]
                    
                    # Establecer los bits I, U, B
                    i_bit = "1"
                    u_bit = "1"
                    scr2 =f"00000000{rm_bin}"
        
            else:
                # Sin offset, solo 2 registros
                
                # Establecer los bits I, U, B
                i_bit = "0"
                u_bit = "1"
                
                # Construir la instrucción en binario con offset igual a 0
                scr2 = "000000000000"
            bin_instr = f"{cond_bin}{opcode_bin}{i_bit}{p_bit}{u_bit}{b_bit}{w_bit}{l_bit}{rn_bin}{rd_bin}{scr2}"

        # Branch Instructions
        elif instrc[0] in branch_instructions:
            opcode_bin = "10"
            l_bit = branch_instructions[instrc[0]]
            
            # Verificar si se especifica un código de condición
            if len(instrc) == 3 and instrc[1] in cond and instrc[0] != "bl":
                cond_bin = cond[instrc[1]]
                label_index = 2
            else:
                cond_bin = cond["al"]  # Condición por defecto (always)
                label_index = 1
            
            # Obtener la etiqueta de destino
            target_label = instrc[label_index]
            
            # Verificar si la etiqueta existe en el diccionario de etiquetas
            if target_label not in labels:
                raise ValueError(f"Etiqueta '{target_label}' no encontrada")
            
            # Calcular el offset relativo a la dirección actual
            target_address = labels[target_label]
            offset = (target_address - address - 8) // 4
            
            # Verificar el rango del offset (-2^23 a 2^23 - 1)
            if offset < -2**23 or offset >= 2**23:
                raise ValueError(f"Offset fuera de rango para la instrucción de branch")
            
            # Convertir el offset a binario (24 bits) con signo
            offset_bin = f"{offset & 0xFFFFFF:024b}"
            
            # Construir la instrucción en binario
            bin_instr = f"{cond_bin}{opcode_bin}{l_bit}{offset_bin}"


        # Special Instructions
        elif instrc[0] in special_instructions:
            opcode_bin = "11"
            # Obtener el código de función de la instrucción especial
            funct_bin = special_instructions[instrc[0]]
            
            # Construir la instrucción en binario con relleno de 1
            bin_instr = f"1111{opcode_bin}1111111111111111111111{funct_bin}"


        # Throw an error
        else:
            raise ValueError(f"Instruccion "+ line + f" no encontrada, address: {address}")

        assert len(bin_instr) == 32
        return bin_instr
    except Exception as e:
        print(e)
        raise ValueError(f"Instruccion '{instrc[0]}' no encontrada, address: {address:08x}")
        

    
def main():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    # Initialize the GUI window and hide it
    Tk().withdraw()
    # Open a file selection dialog and get the file path
    file_path = askopenfilename(title='Select assembly file')
    if file_path: # If a file was selected
        output_path = file_path.replace('.txt', '.dat')
        labels, instructions = identify_specific_labels_and_instructions(file_path)
        write_output(output_path, labels, instructions)
        # for address, instruction in enumerate(instructions):
        #     bin = compileLine(instruction, labels, address*4)
        #     print(bin) 
        #     print(f"{int(bin, 2):08x}")
            
    # lines = [
    #     "sum,v0,v1,v2",
    #     "com,v2,#12",
    #     "set,v1,#1024",
    #     "xor,v3,v2,v1",
    #     "divi,v1,v5,#31",
    #     "sum,eq,v1,v1,#18"
    # ]



if __name__ == "__main__":
    main()