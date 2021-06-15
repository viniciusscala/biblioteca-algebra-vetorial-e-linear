from estruturas import *
from ferramentas_basicas import saoParalelos, saoOrtogonais, projecao

def diretor(reta):
    return reta.vetorDiretor

def normal(plano):
    return plano.vetorNormal

def eParalelo (vetor,reta):
    return saoParalelos(vetor, reta.vetorDiretor)

def eOrtogonal (vetor, plano):
    return saoParalelos(vetor, plano.vetorNormal)

def projecao(vetor, reta):
    return projecao(vetor, reta.vetorDiretor)

def projecao(vetor, plano):
    
def componenteOrtogonais(vetor, plano):
    return projecao(vetor, plano.vetorNormal)

def saoComplementosOrtogonais(reta, plano):
    return saoParalelos(reta.vetorDiretor, plano.vetorNormal)

def saoComplementosOrtogonais(plano, reta):
    return saoParalelos(reta.vetorDiretor, plano.vetorNormal)

def formaCartesiana(plano): 
    a = plano.vetorNormal.x
    b = plano.vetorNormal.y
    c = plano.vetorNormal.z
    d = -((a * plano.ponto.x) + (b * plano.ponto.y) + (c * plano.ponto.z))

    coeficientes = [a,b,c,d]
    return coeficientes     

def formaCartesiana(reta):
