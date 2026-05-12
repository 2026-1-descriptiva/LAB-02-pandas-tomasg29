"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/|
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd

    # Cargar los archivos tbl0.tsv y tbl2.tsv
    dataframe_cero = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    dataframe_dos = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    # Fusionar los dos DataFrames usando la columna "c0" como clave
    dataframe_combinado = pd.merge(dataframe_cero, dataframe_dos, on='c0')

    # Sumar la columna "c5b" agrupado por la columna "c1"
    suma_por_grupo = dataframe_combinado.groupby('c1')['c5b'].sum()

    return suma_por_grupo

print(pregunta_13())