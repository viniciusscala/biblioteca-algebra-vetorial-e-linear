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

def cosseno(v1, v2):
    return produtoEscalar(v1, v2) / (norma(v1) * norma(v2))

def projecao(v1, v2):
    escalar = produtoEscalar(v1, v2) / produtoEscalar(v2, v2)

    return Vetor(escalar * v2.x, escalar * v2.y, escalar * v2.z)

def produtoVetorial(v1, v2):
    x = (v1.y * v2.z) - (v1.z * v2.y)
    y = (v1.z * v2.x) - (v1.x * v2.z)
    z = (v1.x * v2.y) - (v1.y * v2.x)

    return Vetor(x, y, z)

def eLI(v1, v2, v3):
    return produtoEscalar(v1, produtoVetorial(v2, v3)) != 0
