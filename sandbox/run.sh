#!/bin/bash

# Asigna el primer argumento a la variable 'filename', si no se proporciona, usa 'main.s'
filename=${1:-main.s}

# Extrae el nombre base sin la extensión (asumiendo extensión .s)
base=${filename%.*}

# Compila, enlaza y genera la salida del desensamblador usando el nombre base
#!/bin/bash

# Asigna el primer argumento a la variable 'filename', si no se proporciona, usa 'main.s'
filename=${1:-main.s}

port=${2:-12345}

# Extrae el nombre base sin la extensión (asumiendo extensión .s)
base=${filename%.*}


# Detiene el script en caso de errores
set -e
# Asegura que los errores en pipelines sean capturados
set -o pipefail

# Ensambla el archivo fuente
arm-linux-gnueabi-as $base.s -o $base.o

# Enlaza el objeto para crear el ejecutable
arm-linux-gnueabi-ld $base.o -o $base

# Crea un dump de desensamblado
arm-linux-gnueabi-objdump -d $base &> $base.disassembly

# Ejecuta el binario en QEMU y espera a la conexión del debugger
qemu-arm -g $port ./$base &

# Espera un poco a que QEMU se inicie correctamente
sleep 2

# Inicia GDB
gdb-multiarch -q -ex "target remote localhost:$port" $base