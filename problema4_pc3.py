#Se define una función teniendo como parámetro 'cadena' 
def longitud_ult_palabra(cadena=str):
    #Se eliminan los espacios y se divide por palabras
    palabras=cadena.strip().split()
    if len(palabras)>0:
        ultima_palabra=palabras[-1]
        return len(ultima_palabra)
    else:
        return 0