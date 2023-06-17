#Se importa el módulo 'random'
import random
#Se define una función 'generar_numeros_random'
def veinte_numeros_random():
    numeros_aleatorios=[]
    for num in range(20):
        numero=random.randint(0,100)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios
#Se define una función con el parámetro 'lista'
def mostrar_lista(lista):
    for numero in lista:
        print(numero)
#Se define una función con el parámetro 'lista'
def ordenar_lista(lista):
    lista.sort()
    for numero in lista:
        print(numero)