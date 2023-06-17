#Se define una función con 2 parámetros
def sumar_num(a,b):
    #Se intenta realizar la operación
    try:
        suma=a+b
        return suma
    #De no ejecutarse debido a un error, se imprime 'Dato inválido'
    except TypeError:
        print('Dato inválido')
#Se define una función con 2 parámetros
def restar_num(a,b):
    #Se intenta realizar la operación
    try:
        resta=a-b
        return resta
    #De no ejecutarse debido a un error, se imprime 'Dato inválido'
    except TypeError:
        print('Dato inválido')
#Se define una función con 2 parámetros
def producto_num(a,b):
    #Se intenta realizar la operación
    try:
        producto=a*b
        return producto
    #De no ejecutarse debido a un error, se imprime 'Dato inválido'
    except TypeError:
        print('Dato inválido')
#Se define una función con 2 parámetros
def dividir_num(a,b):
    #Se intenta realizar la operación
    try:
        division=a/b
        return division
    #De no ejecutarse debido a un error, se imprime 'Dato inválido'
    except TypeError:
        print('Dato inválido')
    except ZeroDivisionError:
        print('No es posible dividir entre cero')