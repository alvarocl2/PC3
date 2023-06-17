#Se define una función teniendo como parámetro el número de filas que tendrá nuestro triángulo de Pascal
def triangulo_pascal(num=int):
    #En caso de que sea n=0 o n=1, retorna 0 o 1 respetivamente
    if num == 0:
        return[]
    if num == 1:
        return [[1]]
    #Si el numero fuera mayor a 1, se usará una función recursiva
    triangulo = triangulo_pascal(num - 1)
    ultima_fila = triangulo[-1]
    fila_actual = [1]
    #Se calculan los nuevos elementos de la fila actual
    for i in range(len(ultima_fila) - 1):
        fila_actual.append(ultima_fila[i] + ultima_fila[i + 1])
    #Se agrega el '1' como último elemento de la fila actual
    fila_actual.append(1)
    #Se agrega la fila completa a 'triangulo'
    triangulo.append(fila_actual)
    return triangulo