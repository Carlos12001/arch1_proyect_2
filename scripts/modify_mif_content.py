def modify_mif_content(mif_lines, text):
    # Encuentra el índice de inicio y fin del bloque CONTENT
    start_index = mif_lines.index('CONTENT BEGIN\n') + 1
    end_index = mif_lines.index('END;\n')

    # Eliminar las líneas actuales de contenido
    del mif_lines[start_index:end_index]

    # Convertir cada carácter del texto en su valor ASCII y formatear la salida
    for i, char in enumerate(text):
        mif_lines.insert(start_index + i, f"\t{i}    :   {ord(char)};\n")
    
    # Completar las direcciones de memoria restantes hasta 255 con 0
    for i in range(len(text), 2**16-1):
        mif_lines.insert(start_index + i, f"\t{i}    :   0;\n")
    
    mif_lines.insert(start_index + 2**16-1, "END;\n")

    return mif_lines

# Leer el contenido del archivo .mif
mif_file_path = './Proyecto/RAM.mif'
with open(mif_file_path, 'r') as file:
    mif_content = file.readlines()

# Leer el contenido del archivo de texto para obtener los valores a escribir en el archivo .mif
lectura_file_path = './scripts/Lectura.txt'
with open(lectura_file_path, 'r') as file:
    text_content = file.read()

# Modificar el contenido del archivo .mif
modified_mif_content = modify_mif_content(mif_content, text_content)

# Guardar el contenido modificado en un nuevo archivo .mif
with open(mif_file_path, 'w') as file:
    file.writelines(modified_mif_content)

print("Archivo .mif modificado y guardado exitosamente:", mif_file_path)
