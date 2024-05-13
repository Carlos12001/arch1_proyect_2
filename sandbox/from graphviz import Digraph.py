from graphviz import Digraph

# Crear un objeto Digraph y configurar la orientación vertical
dot = Digraph(comment='Requisitos de Microarquitectura y Software')
dot.attr(rankdir='TB')  # Top to Bottom para dirección vertical

# Agregar nodos para Requisitos de Microarquitectura
dot.node('A', '2.2. Requisitos de Microarquitectura')
dot.node('B', '1. La implementación diseñada debe ser correcta respecto a las reglas definidas por la arquitectura.')
dot.node('C', '2. El procesador diseñado debe emplear pipelining.')
dot.node('D', '3. Debe ser implementado usando SystemVerilog.')
dot.node('E', '4. No se permite realizar módulos especializados de hardware.')
dot.node('F', '5. El procesador debe tener capacidad de segmentación de memoria en datos e instrucciones.')
dot.node('G', '6. Cada unidad funcional del sistema debe ser debidamente probada en simulación.')
dot.node('H', '7. Los productos finales de esta etapa son:')
dot.node('I', 'a) El código fuente (SystemVerilog) y el bitstream para programar la tarjeta de desarrollo mediante simulación.')
dot.node('J', 'b) Un diagrama de bloques de la microarquitectura y descripción de las interacciones entre ellos.')
dot.node('K', 'c) Simulaciones de las pruebas unitarias y de integración.')
dot.node('L', 'd) Reporte de consumo de recursos del FPGA para el modelo.')

# Agregar nodos para Requisitos de Software
dot.node('M', 'Requisitos de Software:')
dot.node('N', '1. Crear una aplicación (software) empleando la arquitectura diseñada.')
dot.node('O', '2. Debe realizar un programa compilador que permita traducir las instrucciones del ISA a binario.')
dot.node('P', '3. Los productos finales de esta etapa son:')
dot.node('Q', 'a) Programa compilador internamente documentado.')
dot.node('R', 'b) Código ensamblador para la arquitectura diseñada.')

# Agregar aristas para establecer un flujo vertical
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'JK', 'KL'])
dot.edges(['LM', 'MN', 'NO', 'OP', 'PQ', 'QR'])

# Renderizar el gráfico
dot.render('requisitos_microarquitectura_software_vertical', format='png', view=True)