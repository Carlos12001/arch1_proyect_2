from graphviz import Digraph

# Crear un objeto Digraph
dot = Digraph()

# Agregar nodos para representar los requisitos de arquitectura ISA
dot.node('A', 'Conjunto de Instrucciones')
dot.node('B', 'Justificación del Diseño')
dot.node('C', 'Desarrollo de Instrucciones')
dot.node('D', 'Productos Finales')

# Agregar relaciones entre los nodos
dot.edge('A', 'B', label='1. Diseño')
dot.edge('B', 'C', label='2. Análisis')
dot.edge('C', 'D', label='3. Implementación')

# Guardar el diagrama en un archivo
dot.render('arquitectura_ISA_diagrama', format='png', cleanup=True)
