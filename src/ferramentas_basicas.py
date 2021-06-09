from estruturas import Vetor
from math import sqrt

def produtoEscalar(v1, v2):
    return (v1.x*v2.x) + (v1.y*v2.y) + (v1.z*v2.z)

def norma2(vetor):
    return produtoEscalar(vetor, vetor)

def norma(vetor):
    return sqrt(produtoEscalar(vetor, vetor))

def normalize(vetor):
    norma = norma(vetor)
    return Vetor(vetor.x / norma, vetor.y / norma, vetor.z / norma)

def cosseno(v1, v2):
    return produtoEscalar(v1, v2) / (norma(v1) * norma(v2))

def projecao(v1, v2):
    escalar = produtoEscalar(v1, v2) / produtoEscalar(v2, v2)

    return Vetor(escalar * v2.x, escalar * v2.y, escalar * v2.z)

def dist_reta_a_reta(reta1, reta2):

    u = reta1.vetorDiretor
    v = reta2.vetorDiretor
    w = Vetor(reta1.ponto.x-reta2.ponto.x, reta1.ponto.y-reta2.ponto.y, reta1.ponto.z-reta2.ponto.z)
    a = produtoEscalar(u,u)        
    b = produtoEscalar(u,v)
    c = produtoEscalar(v,v)         
    d = produtoEscalar(u,w)
    e = produtoEscalar(v,w)
    D = (a*c) - (b*b)        

    if (D < 0.000001):     
        sc = 0.0
        tc = d/b if b>c else e/c   
    
    else:
        sc = (b*e - c*d) / D
        tc = (a*e - b*d) / D
    
    dPx = w.x + (sc * u.x) - (tc * v.x) 
    dPy = w.y + (sc * u.y) - (tc * v.y) 
    dPz = w.z + (sc * u.z) - (tc * v.z)

    return norma(Vetor(dPx, dPy, dPz))   # return the closest distance

def produtoVetorial(v1, v2):
    x = (v1.y * v2.z) - (v1.z * v2.y)
    y = (v1.z * v2.x) - (v1.x * v2.z)
    z = (v1.x * v2.y) - (v1.y * v2.x)

    return Vetor(x, y, z)

def reflexao(v1, v2):
    v3 = projecao(v1, v2)
    aux = Vetor(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z)

    return Vetor(v3.x + aux.x, v3.y + aux.y, v3.z + aux.z)

def saoParalelos(v1, v2):
    pV = produtoVetorial(v1, v2)
    return pV.x == 0 and pV.y == 0 and pV.z == 0

def saoOrtogonais(v1, v2):
    return produtoEscalar(v1, v2) == 0

def eLI(v1, v2, v3):
    return produtoEscalar(v1, produtoVetorial(v2, v3)) != 0
