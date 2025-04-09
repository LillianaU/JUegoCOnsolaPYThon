# Leer la altura desde el usuario
altura = int(input("Ingrese la altura de la escalera: "))  # Solicita un número al usuario y lo convierte a entero, almacenándolo en 'altura'

# Crear una matriz dinámica (lista de listas) 
# con altura filas y (altura * 2 - 1) columnas para centrar los asteriscos
matriz = []                                               # Crea una lista vacía 'matriz' que contendrá todas las filas de la escalera

for i in range(altura):                                   # Inicia un bucle que recorre desde 0 hasta altura-1 para crear cada fila
    # Cada fila tendrá espacios y asteriscos
    fila = []                                             # Crea una lista vacía 'fila' para almacenar los caracteres (espacios y asteriscos) de la fila actual
    
    # Calcular espacios izquierdos
    for j in range(i):                                    # Bucle que itera 'i' veces para agregar espacios a la izquierda
        fila.append(" ")                                  # Agrega un espacio (" ") a la lista 'fila' en cada iteración
    
    # Calcular asteriscos (disminuyen en cada fila)
    for j in range(altura * 2 - 1 - 2 * i):              # Bucle que calcula y agrega asteriscos; la fórmula determina cuántos asteriscos van en la fila
        fila.append("*")                                  # Agrega un asterisco ("*") a la lista 'fila' en cada iteración
    
    matriz.append(fila)                                   # Agrega la fila completa (lista con espacios y asteriscos) a la 'matriz'

# Imprimir la matriz fila por fila
for fila in matriz:                                       # Itera sobre cada fila almacenada en la 'matriz'
    print("".join(fila))                                  # Convierte la lista 'fila' en una cadena uniendo todos sus elementos y la imprime
    
"""

Contexto:
Esta línea está dentro de un bucle que construye cada fila de la escalera invertida de asteriscos. El objetivo es determinar cuántos asteriscos (*) se añaden a cada fila de la matriz, y ese número disminuye a medida que avanzamos en las filas (de arriba hacia abajo).

altura: Es el número entero ingresado por el usuario (en tu ejemplo, 5).
i: Es el índice de la fila actual en el bucle exterior (for i in range(altura)), que va de 0 a altura - 1 (es decir, de 0 a 4 si altura = 5).
fila: Es una lista que representa una fila de la escalera y se llena con espacios y asteriscos.
Qué hace el for:
range(altura * 2 - 1 - 2 * i):
Calcula cuántas veces se ejecutará el bucle interno, es decir, cuántos asteriscos se añadirán a la fila actual.
La expresión altura * 2 - 1 - 2 * i determina el número de asteriscos en función de la fila (i).
Veamos cómo funciona con altura = 5:
Fila 0 (i = 0): 5 * 2 - 1 - 2 * 0 = 10 - 1 - 0 = 9
Fila 1 (i = 1): 5 * 2 - 1 - 2 * 1 = 10 - 1 - 2 = 7
Fila 2 (i = 2): 5 * 2 - 1 - 2 * 2 = 10 - 1 - 4 = 5
Fila 3 (i = 3): 5 * 2 - 1 - 2 * 3 = 10 - 1 - 6 = 3
Fila 4 (i = 4): 5 * 2 - 1 - 2 * 4 = 10 - 1 - 8 = 1
for j in range(...):
Itera desde 0 hasta el valor calculado menos 1. Por ejemplo, si el resultado es 9, j va de 0 a 8, ejecutando el cuerpo del bucle 9 veces.
fila.append("*"):
En cada iteración, agrega un asterisco (*) a la lista fila. Como el bucle se ejecuta el número de veces calculado por range, se añaden exactamente esa cantidad de asteriscos a la fila.
Propósito:
La fórmula altura * 2 - 1 - 2 * i asegura que:
La primera fila (i = 0) tenga el máximo número de asteriscos (9 si altura = 5).
Cada fila siguiente tenga 2 asteriscos menos que la anterior, creando la forma de escalera invertida.
Esto se deriva de que:
altura * 2 - 1 da el ancho máximo de la base (en una pirámide simétrica).
- 2 * i reduce progresivamente los asteriscos (2 por fila) para formar la escalera.
Resultado en el ejemplo (altura = 5):
Fila 0: 9 asteriscos (pero en el código final se ajusta con los espacios).
Fila 1: 7 asteriscos.
Fila 2: 5 asteriscos.
Fila 3: 3 asteriscos.
Fila 4: 1 asterisco.

"""