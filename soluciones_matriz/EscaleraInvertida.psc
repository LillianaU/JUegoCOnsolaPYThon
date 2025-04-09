Algoritmo EscaleraInvertida
    // Declarar variables
    Definir altura Como Entero
    Definir i, j Como Entero
    Definir fila Como Caracter
    Definir num_asteriscos Como Entero
    
    // Leer la altura desde el usuario
    Escribir "Ingrese la altura de la escalera: "
    Leer altura
    
    // Crear la escalera invertida
    Para i <- 0 Hasta altura - 1 Hacer
        // Inicializar fila como cadena vacía
        fila <- ""
        
        // Calcular espacios izquierdos
        Para j <- 0 Hasta i - 1 Hacer
            fila <- fila + " "
        FinPara
        
        // Calcular número de asteriscos (disminuye en cada fila)
        num_asteriscos <- altura - i
        
        // Agregar los asteriscos
        Para j <- 0 Hasta num_asteriscos - 1 Hacer
            fila <- fila + "*"
        FinPara
        
        // Imprimir la fila
        Escribir fila
    FinPara
    
FinAlgoritmo