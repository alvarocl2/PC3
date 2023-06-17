#Se importan las funciones de 'modulo'
import modulo
#Se ejecutan las funciones importadas
num_lista=modulo.veinte_numeros_random()
print(f'La lista de números aleatorios es: {num_lista}')
print('A continuación se muestran los números:')
modulo.mostrar_lista(num_lista)
print('A continuación se muestran los números ordenados:')
modulo.ordenar_lista(num_lista)