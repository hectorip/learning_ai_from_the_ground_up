# Pandas es una biblioteca que permite trabajar con datos de manera
# eficiente y sencilla.
# 
# Una opción más moderna es Polars, pero comparten muchos concepts,
# así que empezaremos con Pandas.

import pandas as pd
import numpy as np

# Pandas provee Series, DataFrames y Panel.
# Series: es un array unidimensional con etiquetas.

my_series = pd.Series([1, 2, 3, 4]) # sin etiquetas explícitas, se usan numeros
print(my_series)

# Son muy similares a los arrays de NumPy (ndarray) y se pueden
# usar en muchoas casos como argumentos de funciones de NumPy.

print(np.sum(my_series))

# El concepto principal de pandas es el DataFrame: una
# estructura de datos en forma de tabla con filas y columnas
# etiquetadas.
#
# Los elementos de un dataframe pueden ser de diferentes tipos,
# pero todas las filas deben tener la misma cantidad de columnas.

my_data_frame = pd.DataFrame({
    "a": [[1, 2, 3], [1, 2, 3],[1, 2, 3]],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
})

print(my_data_frame)

