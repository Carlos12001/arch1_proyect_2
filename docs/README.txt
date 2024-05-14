# Diseño e Implementación de un ASIP para la Generación de Gráficos y Texto

## Descripción del Proyecto
Este proyecto consiste en el diseño e implementación de un Application Specific Instruction Set Processor (ASIP) para la generación de gráficos y texto. El ASIP está diseñado para ejecutar instrucciones específicas que permiten la creación de imágenes a partir de estructuras geométricas simples y la representación de texto en una imagen binarizada.

## Herramientas Utilizadas
### Hardware
- **FPGA**: Terasic DE1-SoC-M TL2

### Software
- **Quartus Prime**: Utilizado para la síntesis y simulación del diseño en FPGA.
- **ModelSim**: Utilizado para la simulación y verificación del diseño en HDL.
- **SystemVerilog**: Lenguaje de descripción de hardware utilizado para implementar el ASIP.
- **Git**: Sistema de control de versiones utilizado para gestionar el código fuente del proyecto.
- **Markdown**: Utilizado para la documentación del proyecto.
- **VGA**: Interfaz utilizada para mostrar el resultado en pantalla.

## Instrucciones de Uso
### Configuración del Entorno de Desarrollo
1. **Instalación de Quartus Prime**:
   - Descargue e instale Quartus Prime desde el sitio web oficial de Intel FPGA.
   - Configure el entorno de desarrollo para trabajar con la tarjeta Terasic DE1-SoC-M TL2.

2. **Instalación de ModelSim**:
   - Descargue e instale ModelSim desde el sitio web oficial de Intel FPGA.
   - Configure ModelSim para trabajar con proyectos de SystemVerilog.

### Clonación del Repositorio
1. **Clonar el Repositorio**:
   - Use el siguiente comando para clonar el repositorio del proyecto:
     ```bash
     git clone https://github.com/Carlos12001/arch1_proyect_2
     ```
   - Navegue al directorio del proyecto:
     ```bash
     cd arch1_proyect_2
     ```

### Compilación y Síntesis del Proyecto
1. **Abrir Quartus Prime**:
   - Abra Quartus Prime y cargue el proyecto desde el archivo `.qpf` ubicado en el directorio del proyecto.

2. **Compilar el Proyecto**:
   - En Quartus Prime, compile el proyecto seleccionando `Processing > Start Compilation`.
   - Espere a que la compilación finalice sin errores.

### Simulación del Diseño
1. **Abrir ModelSim**:
   - Abra ModelSim y cargue el proyecto desde el archivo `.do` ubicado en el directorio `sim`.

2. **Ejecutar la Simulación**:
   - En ModelSim, ejecute la simulación seleccionando `Run > Run -All`.
   - Verifique los resultados de la simulación para asegurar el funcionamiento correcto del diseño.

### Programación del FPGA
1. **Cargar el Bitstream en la Tarjeta DE1-SoC**:
   - Conecte la tarjeta DE1-SoC a su computadora.
   - Use Quartus Prime para cargar el bitstream generado (`.sof`) en la tarjeta seleccionando `Tools > Programmer`.

### Visualización de Resultados
1. **Conectar VGA**:
   - Conecte la salida VGA de la tarjeta DE1-SoC a un monitor.
   - Verifique que los gráficos y el texto generados se muestran correctamente en la pantalla.

