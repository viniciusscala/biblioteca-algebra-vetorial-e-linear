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

    n_norma2 = norma2(plano.vetorNormal)
    proj_u_em_nX = (produtoEscalar(vetor, plano.vetorNormal)/n_norma2) * plano.vetorNormal.x
    proj_u_em_nY = (produtoEscalar(vetor, plano.vetorNormal)/n_norma2) * plano.vetorNormal.y
    proj_u_em_nZ = (produtoEscalar(vetor, plano.vetorNormal)/n_norma2) * plano.vetorNormal.z

    vectorProjectionX = vetor.x - proj_u_em_nX
    vectorProjectionY = vetor.y - proj_u_em_nY
    vectorProjectionZ = vetor.z - proj_u_em_nZ

    return Vetor(vectorProjectionX, vectorProjectionY, vectorProjectionZ)
    
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
    a = reta.vetorDiretor.y/reta.vetorDiretor.x
    b = -1
    c = 0
    d = reta.ponto.y - ((reta.vetorDiretor.y/reta.vetorDiretor.x) * reta.ponto.x)   

    e = reta.vetorDiretor.z/reta.vetorDiretor.x
    f = 0
    g = -1
    h = reta.ponto.z - ((reta.vetorDiretor.z/reta.vetorDiretor.x) * reta.ponto.x)

    coeficientes = [[a,b,c,d],[e,f,g,h]]
    return coeficientes    
