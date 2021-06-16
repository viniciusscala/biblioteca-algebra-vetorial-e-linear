from math import cos, sin
from estruturas import Vetor, Base
from ferramentas_basicas import reflexao as reflexao_vetor, normalize, produtoVetorial

def rotacao(vetor, angulo, sentido, reta):
    v1 = normalize(reta.vetorDiretor)
    v2 = normalize(Vetor(0, 1, - (v1.x/v1.z)))
    v3 = normalize(produtoVetorial(v1, v2))
    novaBase = Base(v1, v2, v3)

    novoVetor = mudeBase(vetor, novaBase)

    coseno = cos(angulo)
    seno = sin(angulo)

    if(sentido == "AH"):
        return Vetor(novoVetor.x*coseno - seno*novoVetor.y, novoVetor.y*coseno + seno*novoVetor.x, novoVetor.z)
    return Vetor(novoVetor.x*coseno + seno*novoVetor.y, novoVetor.y*coseno - seno*novoVetor.x, novoVetor.z)

def reflexao_reta(vetor, vetorDiretor):
    return reflexao_vetor(vetor, vetorDiretor)

def reflexao(vetor):
    return Vetor(-1*vetor.x, -1*vetor.y, -1*vetor.z)

def deformacao(vetor, fatorX, fatorY, fatorZ):
    return Vetor(vetor.x * fatorX, vetor.y * fatorY, vetor.z * fatorZ)

def cisalhamento(vetor, eixos, fator):
    if (eixos == "XY"):
        x = vetor.x + fator*vetor.y
        y = vetor.y
        z = vetor.z

    if (eixos == "XZ"):
        x = vetor.x + fator*vetor.z
        y = vetor.y
        z = vetor.z

    if (eixos == "YX"):
        y = vetor.y + fator*vetor.x
        x = vetor.x
        z = vetor.z

    if (eixos == "YZ"):
        y = vetor.y + fator*vetor.z
        x = vetor.x
        z = vetor.z

    if (eixos == "ZX"):
        z = vetor.z + fator*vetor.x
        y = vetor.y
        x = vetor.x

    if (eixos == "ZY"):
        z = vetor.z + fator*vetor.y
        y = vetor.y
        x = vetor.x

    vetorCisalhado = Vetor(x, y, z)
    return vetorCisalhado

def cisalhamento(vetor, eixos, fator1, fator2):
    if (eixos == "XYZ"):
        x = vetor.x + fator1*vetor.y + fator2*vetor.z
        y = vetor.y
        z = vetor.z

    if (eixos == "YZX"):
        y = vetor.y + fator1*vetor.z + fator2*vetor.x
        x = vetor.x
        z = vetor.z

    if (eixos == "ZXY"):
        z = vetor.z + fator1*vetor.x + fator2*vetor.y
        y = vetor.y
        x = vetor.x

    vetorCisalhado = Vetor(x, y, z)
    return vetorCisalhado
