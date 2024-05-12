from graphviz import Digraph

def crear_grafico():
    # Crear un objeto Digraph
    grafico = Digraph()

    # Configuración del estilo del gráfico
    grafico.attr(rankdir='LR', size='8,5')
    grafico.attr('node', shape='rectangle', style='filled', color='lightblue2')
    grafico.attr('edge', fontsize='10', fontname='helvetica')

    # Agregar nodos y arcos
    grafico.node('A', 'Propuestas y\nViabilidad')
    grafico.node('B', 'Diseño de\nMicroarquitectura')
    grafico.node('C', 'Implementación de\nSoftware')

    grafico.edge('A', 'B', label='Propuestas de diseño\nComparación de viabilidad', color='blue', style='dashed')
    grafico.edge('B', 'C', label='Código fuente (SystemVerilog)\nDiagrama de bloques\nSimulaciones de pruebas\nReporte de consumo de recursos del FPGA', color='green')
    grafico.edge('C', 'B', label='Aplicación implementada con funcionalidades solicitadas\nPrograma compilador documentado\nCódigo ensamblador para la arquitectura', color='red')

    # Agregar un título al gráfico
    grafico.attr(label='Proceso de Diseño', fontsize='20', fontname='helvetica', fontcolor='blue')

    # Mostrar el gráfico
    return grafico

if __name__ == "__main__":
    grafico = crear_grafico()
    grafico.render('proceso_de_diseno', format='png', cleanup=True, view=True)
