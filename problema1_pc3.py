#Problema 1
#Importar el módulo 'fractions'
from fractions import Fraction
#Crear un bucle para forzar a que el usuario ingrese un número correcto
#'x' e 'y' deben ser enteros, 'y' debe ser diferente de 0, 'x' <= 'y'
while (True):
    try:
        #Soliitar al usuario que ingrese una fracción 'x/y'
        fraccion_str=input('Inserte una fracción (x/y) que indique la cantidad de combustible, donde x>y: ')
        #Se convierte la fraccion ingresada de cadena de texto a valores numéricos
        fraccion=Fraction(fraccion_str)
        x=fraccion.numerator
        y=fraccion.denominator
        #Se analiza si es menor a 1%, mayor a 99% o está entre ese rango
        if x<=y:
            if (x/y)*100<=1:
                print('E')
                break
            elif (x/y)*100>99:
                print('F')
                break
            else:
                print(f'{(x/y)*100}%')
                break 
    #Mensaje de respuesta ante posibles errores
    except ZeroDivisionError:
        print('Error, no es válida la divión entre 0, vuelva a intentarlo...')
    except ValueError:
        print('Error, solo se permite que x e y tomen valores de números enteros, vuelva a intentarlo...')