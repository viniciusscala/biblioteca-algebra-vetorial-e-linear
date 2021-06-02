from estruturas import Vetor
from math import sqrt

def norma(vetor):
    a = vetor.x ** 2
    b = vetor.y ** 2
    c = vetor.z ** 2

    return sqrt(a+b+c)

def normalize(vetor):
    fator_de_correcao = norma(vetor)

    a = vetor.x / fator_de_correcao
    b = vetor.y / fator_de_correcao
    c = vetor.z / fator_de_correcao

    return Vetor(a, b, c)