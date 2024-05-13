from graphviz import Digraph

# Crear un objeto Digraph y configurar la orientación vertical
dot = Digraph(comment='Requisitos de Arquitectura ISA')
dot.attr(rankdir='TB')  # Top to Bottom para dirección vertical

# Agregar nodos
dot.node('A', '2.1. Requisitos de Arquitectura ISA')
dot.node('B', '1. Debe diseñar un conjunto de instrucciones y arquitectura')
dot.node('C', 'a) Modos de direccionamiento')
dot.node('D', 'b) Tamaño y tipo de datos')
dot.node('E', 'c) Tipo y sintaxis de las instrucciones')
dot.node('F', 'd) Registros disponibles y sus nombres')
dot.node('G', 'e) Codificación y descripción funcional de las instrucciones')
dot.node('H', 'Justificación de detalles desde el punto de vista de diseño')
dot.node('I', 'Análisis en software de alto nivel para valores idóneos')
dot.node('J', '2. Instrucciones a desarrollar son libres')
dot.node('K', 'Proveer al menos:')
dot.node('L', 'Instrucciones para control de flujo')
dot.node('M', 'Operaciones aritméticas-lógicas')
dot.node('N', 'Acceso a memoria')
dot.node('O', '3. ISA debe ser personalizado y realizado por los estudiantes')
dot.node('P', 'No se aceptarán ISAs ya diseñados (e.g., ARM, x86, RISC-V, otros)')
dot.node('Q', 'Justificar cada característica del ISA')
dot.node('R', '4. Productos finales de esta etapa')
dot.node('S', 'a) Instruction reference sheet o green card')
dot.node('T', 'b) Scripts usados para justificar las características del ISA')

# Agregar aristas para establecer un flujo vertical
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'JK', 'KL', 'LM', 'MN', 'NO', 'OP', 'PQ', 'QR', 'RS', 'ST'])

# Renderizar el gráfico
dot.render('requisitos_isa_vertical', format='png', view=True)