import unittest

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

class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        sinacentos = replace('zzz')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {})

    def test_cas(self):
        sinacentos = replace('cas')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1})

    def test_casa(self):
        sinacentos = replace('casa')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 2})

    def test_bese(self):
        sinacentos = replace('bese')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'e': 2})

    def test_besa(self):
        sinacentos = replace('besa')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1, 'e': 1})

    def test_casanova(self):
        sinacentos = replace('casanova')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 3, 'o': 1})

    def test_mUrciElago(self):
        sinacentos = replace('mUrciElago')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test_RELAMPAGO(self):
        sinacentos = replace('RELAMPAGO')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 2, 'e': 1, 'o': 1})

    def test_matEmática(self):
        sinacentos = replace('matEmática')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 3, 'e': 1, 'i': 1})

    def test_ÁRBITRO(self):
        sinacentos = replace('ÁRBITRO')
        resultado2 = count_vocales(sinacentos)
        self.assertEqual(resultado2, {'a': 1, 'i': 1, 'o': 1})

unittest.main()

# while(True):
#     palabra = input('Ingrese palabra: ')
#     print(contar_vocales(palabra))
