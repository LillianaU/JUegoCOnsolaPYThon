# Leer la altura desde el usuario
altura = int(input("Ingrese la altura de la escalera: "))

# Crear la escalera invertida
for i in range(altura):           # Bucle para cada fila, de 0 a altura-1
    fila = ""                     # Inicializa la fila como cadena vacía
    
    # Calcular espacios izquierdos
    for j in range(i):            # Agrega 'i' espacios a la izquierda
        fila = fila + " "
    
    # Calcular número de asteriscos (disminuye en cada fila)
    num_asteriscos = altura - i   # Cantidad de asteriscos en la fila actual
    
    # Agregar los asteriscos
    for j in range(num_asteriscos): # Agrega los asteriscos calculados
        fila = fila + "*"
    
    # Imprimir la fila
    print(fila)