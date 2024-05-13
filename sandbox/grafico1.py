from graphviz import Digraph

dot = Digraph(comment='Requisitos de Microarquitectura y Software')

# Nodos de Microarquitectura
dot.node('A1', 'Implementación Correcta\n(Ejecución de instrucciones, manejo de errores y excepciones)')
dot.node('A2', 'Empleo de Pipelining\n(Riesgos, registros, unidades de ejecución)')
dot.node('A3', 'Implementación en SystemVerilog')
dot.node('A4', 'No Uso de Módulos Especializados\n(Enfoque en Arquitectura de Computadores)')
dot.node('A5', 'Segmentación de Memoria\n(Datos e instrucciones, acceso a E/S)')
dot.node('A6', 'Pruebas Unitarias e Integración\n(Plan de pruebas, objetivos, resultados)')
dot.node('A7', 'Productos Finales de Microarquitectura\n(Código fuente, bitstream, diagramas, simulaciones, reporte)')

# Nodos de Software
dot.node('B1', 'Aplicación Usando la Arquitectura\n(Implementar funcionalidades solicitadas)')
dot.node('B2', 'Programa Compilador\n(Traducir ISA a binario)')
dot.node('B3', 'Productos Finales de Software\n(Compilador documentado, código ensamblador)')

# Aristas de Microarquitectura
dot.edge('A1', 'A2', label='Considerar pipelining')
dot.edge('A2', 'A3', label='Implementar en SystemVerilog')
dot.edge('A3', 'A4', label='Sin módulos especializados')
dot.edge('A4', 'A5', label='Segmentación de memoria')
dot.edge('A5', 'A6', label='Realizar pruebas')
dot.edge('A6', 'A7', label='Generar productos finales')

# Aristas de Software
dot.edge('B1', 'B2', label='Desarrollar compilador')
dot.edge('B2', 'B3', label='Generar productos finales')

# Mostrar el gráfico
print(dot.source)

# Guardar y mostrar el gráfico
dot.render('requisitos_de_microarquitectura_y_software', view=True)