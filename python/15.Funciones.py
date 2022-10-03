def suma(lista, parametro2, parametro3, parametros=4):
    x = 0 
    for elem in lista:
        x += elem
    return x 

sumatoria = suma([1,2,3,4,5])

print(sumatoria)