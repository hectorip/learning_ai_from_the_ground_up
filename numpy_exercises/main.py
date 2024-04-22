import numpy as np

# En este arvhivo vamos a trabajar con Numpy para aprender lo suficiente.
#
# Entendiendo los conceptos básicos de Numpy
# Primero ¿Qué es Numpy?
# NumPy es una biblioteca de Python que permite la manipulación de arreglos y matrices de manera eficiente.
# 1. Crear un array de 10 ceros

mi_array = np.zeros(1)
ceros = np.zeros(10)

print(mi_array)
print(ceros)


# Es la biblioteca para computación científica en Python. Tiene como centro 
# un objeto array de dimensiones arbitrarias (imagino que se puede considerar un tensor)
# También tiene operaciones de álgebra lineal, funciones para genrar números aleatorios y
# otras utilidades de cálculo.

print(np.ones(10))
print(np.ones(10) * 5) # Esta operación es un broadcast

# Generando un array con distribución normal

print(np.random.randn(10))

# Generando datos de ua distribución uniforme
#
print(np.random.uniform(0, 1, (2, 2)))

