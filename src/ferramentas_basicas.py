from estruturas import Vetor
from math import sqrt

def produtoEscalar(v1, v2):
    return (v1.x*v2.x) + (v1.y*v2.y) + (v1.z*v2.z)

def norma(vetor):
    a = vetor.x ** 2
    b = vetor.y ** 2
    c = vetor.z ** 2

    return sqrt(a+b+c)

def normalize(vetor):
    norma = norma(vetor)

    a = vetor.x / norma
    b = vetor.y / norma
    c = vetor.z / norma

    return Vetor(a, b, c)