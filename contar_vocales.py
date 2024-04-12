def replace(mystring):
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'Á':'a', 'É':'e', 'Í':'i', 'Ó':'o', 'Ú':'u'}
    claves = list(acentos.keys())
    valores = list(acentos.values())
    for i in range(0, len(mystring)):
        if mystring[i] in claves:
            indice = claves.index(mystring[i])
            mystring = mystring.replace(mystring[i], valores[indice])
    return(mystring)

def count_vocales(mystring):
    mystring = mystring.lower()
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado2 = {}
    for letra in mystring:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado2:
                resultado2[letra] = 0
            resultado2[letra] += 1
    return resultado2

mystring = input('ingrese palabra: ')
print(count_vocales(replace(mystring)))