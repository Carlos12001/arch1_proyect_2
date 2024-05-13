from graphviz import Digraph

dot = Digraph(comment='Proceso de Generación de Texto')

# Agregar nodos detallados
dot.node('A', 'Carga del Texto desde Memoria\n(>100 palabras, poema o estrofa de canción)')
dot.node('B', 'Procesamiento de Texto con Algoritmo de Bresenham\n(Convertir texto en vectores gráficos)')
dot.node('C', 'Almacenamiento de Imagen Binaria\n(Resolución 250x250, fondo blanco, texto negro)')
dot.node('D', 'Carga del Código de Ensamblador\n(Implementación de letras y firma)')
dot.node('E', 'Interacción del Usuario\n(Observar flujo del programa ensamblador)')
dot.node('F', 'Inicio de Transformación de Texto a Imagen\n(Usar periféricos)')
dot.node('G', 'Visualización del Resultado en VGA\n(Imagen de salida almacenada en memoria)')

# Agregar aristas detalladas
dot.edge('A', 'B', label='Líneas rectas para representar texto\n(Alfabeto definido, coordenadas para letras)')
dot.edge('B', 'C', label='Guardar imagen binarizada en memoria\n(250x250, letras 5x5, espacio 1 píxel)')
dot.edge('C', 'D', label='Permitir carga del código ensamblador\n(Letras y firma programática)')
dot.edge('D', 'E', label='Interacción del usuario\n(Observar y ajustar)')
dot.edge('E', 'F', label='Transformación del texto a imagen\n(Parametrización con switches)')
dot.edge('F', 'G', label='Mostrar resultado en VGA\n(Resolución de salida en memoria)')

# Mostrar el gráfico
print(dot.source)

# Guardar y mostrar el gráfico
dot.render('proceso_de_generacion_de_texto_detallado', view=True)