import matplotlib.pyplot as plt
import numpy as np



# Crear gráfico de puntos
def grafico_puntos(X,Y):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, c='blue', label='Datos')
    plt.title('Gráfico de Puntos de X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Generar datos de ejemplo
X = np.arange(1, 101)  # 100 puntos en X
Y = 2 * X
#grafico_puntos(X,Y)


#Gráfico de barras
def grafico_barras():
    # Generar datos de ejemplo
    import matplotlib.pyplot as plt
    import numpy as np

    # Datos de ejemplo
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
             'Noviembre', 'Diciembre']
    ventas = np.random.randint(100, 1000, size=12)  # Generar ventas aleatorias entre 100 y 999 para cada mes

    # Crear gráfico de barras
    plt.figure(figsize=(12, 7))  # Tamaño del gráfico
    plt.bar(meses, ventas, color='skyblue')  # Crear barras con los datos
    plt.title('Ventas Mensuales - 2023')  # Título del gráfico
    plt.xlabel('Mes')  # Etiqueta eje X
    plt.ylabel('Ventas')  # Etiqueta eje Y
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mejor lectura
    plt.grid(axis='y')  # Mostrar cuadrícula solo en eje Y

    # Mostrar el gráfico
    plt.show()

#grafico_barras()

#grafico de líneas
def grafico_lineas():
    # Datos de ejemplo
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
             'Noviembre', 'Diciembre']
    temperaturas = np.random.randint(10, 30, size=12)  # Temperaturas aleatorias entre 10 y 29 grados para cada mes

    # Crear gráfico de líneas
    plt.figure(figsize=(12, 7))  # Tamaño del gráfico
    plt.plot(meses, temperaturas, marker='o', linestyle='-', color='red')  # Conectar puntos con líneas
    plt.title('Temperatura Media Mensual - 2023')  # Título del gráfico
    plt.xlabel('Mes')  # Etiqueta eje X
    plt.ylabel('Temperatura (°C)')  # Etiqueta eje Y
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mejor lectura
    plt.grid(True)  # Mostrar cuadrícula

    # Mostrar el gráfico
    plt.show()

#grafico_lineas()
