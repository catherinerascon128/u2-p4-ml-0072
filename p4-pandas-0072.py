# catherine eileen huerta rascon NC = 0072
import pandas as pd
import numpy as np

n_filas = 5
n_columnas = 5
tag_columnas = tuple("ABCDE") # etiquetas para las columnas a partir de una tupla
print(tag_columnas)
matriz = np.random.randint(1, 7, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos del 1 al 10")
print(matriz)
# la variable df es data frame
df = pd.DataFrame(matriz, columns=tag_columnas)
print("----- La tabla o dataframe -----> 0072")
print(df)
print("----- catherine eileen huerta rascon NC = 0072 -----")