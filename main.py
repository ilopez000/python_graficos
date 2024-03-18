import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
X = np.arange(1, 101)  # 100 puntos en X
Y = 2 * X + np.random.normal(size=X.size)  # Y es aproximadamente el doble de X con algo de ruido

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

grafico_puntos(X,Y)
