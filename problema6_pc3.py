#Se importan las funciones de 'operaciones'
import operaciones
#Se solicita al usuario que ingrese dos números
print('Se debe insertar dos números')

while True:
    try:
        #Se convierte a float el dato ingresado
        a=float(input('Inserte el primer número: '))
        b=float(input('Inserte el segundo número: '))
        break
    except ValueError:
        #Si el dato ingresado es un str, devuelve "Dato inválido, intentelo de nuevo"
        print('Dato inválido, inserte un número')
#Se ejecutan las funciones
result_suma=operaciones.sumar_num(a,b)
print(f'{a}+{b}={result_suma}')
result_resta=operaciones.restar_num(a,b)
print(f'{a}-{b}={result_suma}')
result_producto=operaciones.producto_num(a,b)
print(f'{a}*{b}={result_producto}')
result_division=operaciones.dividir_num(a,b)
if b!=0:
    print(f'{a}/{b}={result_division}')