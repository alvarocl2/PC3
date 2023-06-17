#Problema 2
#Solicitar al usuario que ingrese valores separados por comas
notas_str=input('Ingrese una lista de notas (separadas por comas): ')
#Se separan las notas con el comando 'split'
notas=notas_str.split(',')
#Se crea una lista vacía donde se almacenarán las notas validadas (enteros)
notas_lista_valida=list()
for nota in notas:
    try:
        notas_entero=int(nota.strip())
        notas_lista_valida.append(notas_entero)
    except:
        print(f"La nota '{nota}' no es válida")
if len(notas_lista_valida)>=1:
    print(f'\tLas notas validadas son: {notas_lista_valida}')
else:
    print('\tNo se registraron notas válidas')