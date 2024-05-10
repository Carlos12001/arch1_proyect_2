#!/bin/bash

# Asigna el primer argumento a la variable 'filename', si no se proporciona, usa 'main.s'
filename=${1:-main.s}

# Extrae el nombre base sin la extensión (asumiendo extensión .s)
base=${filename%.*}

# Especifica el puerto para la conexión de depuración
port=8585

# Ensambla el archivo fuente
arm-linux-gnueabi-as -g $filename -o $base.o

# Enlaza el objeto para crear el ejecutable
arm-linux-gnueabi-ld -g $base.o -o $base

# Crea un dump de desensamblado
arm-linux-gnueabi-objdump -d $base &> $base.disassembly

# Ejecuta el binario en QEMU y espera a la conexión del debugger
qemu-arm -g $port ./$base &

# Espera un poco a que QEMU se inicie correctamente
sleep 2

# Inicia GDB
gdb-multiarch -q -ex "target remote localhost:$port" $base
