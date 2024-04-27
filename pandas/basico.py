# Pandas es una biblioteca que permite trabajar con datos de manera
# eficiente y sencilla.
# 
# Una opción más moderna es Polars, pero comparten muchos concepts,
# así que empezaremos con Pandas.

import pandas as pd


# El concepto principal de pandas es el DataFrame: una
# estructura de datos en forma de tabla con filas y columnas, pero
# que puede tener más dimensiones.


my_data_frame = pd.DataFrame({
    "a": [[1, 2, 3], [1, 2, 3],[1, 2, 3]],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
})

print(my_data_frame)

