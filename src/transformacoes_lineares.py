from estruturas import Vetor
from ferramentas_basicas import reflexao as reflexao_vetor

def reflexao_reta(vetor, vetorDiretor):
    return reflexao_vetor(vetor, vetorDiretor)

def reflexao(vetor):
    return Vetor(-1*vetor.x, -1*vetor.y, -1*vetor.z)

def deformacao(vetor, fatorX, fatorY, fatorZ):
    return Vetor(vetor.x * fatorX, vetor.y * fatorY, vetor.z * fatorZ)

def cisalhamento(vetor, eixos, fator):
    if (eixos == "XY")
        x = vetor.x + fator*vetor.y
        y = vetor.y
        z = vetor.z

    if (eixos == "XZ")
        x = vetor.x + fator*vetor.z
        y = vetor.y
        z = vetor.z

    if (eixos == "YX")
        y = vetor.y + fator*vetor.x
        x = vetor.x
        z = vetor.z

    if (eixos == "YZ")
        y = vetor.y + fator*vetor.z
        x = vetor.x
        z = vetor.z

    if (eixos == "ZX")
        z = vetor.z + fator*vetor.x
        y = vetor.y
        x = vetor.x

    if (eixos == "ZY")
        z = vetor.z + fator*vetor.y
        y = vetor.y
        x = vetor.x

    vetorCisalhado = Vetor(x, y, z)
    return vetorCisalhado

def cisalhamento(vetor, eixos, fator1, fator2):
    if (eixos == "XYZ")
        x = vetor.x + fator1*vetor.y + fator2*vetor.z
        y = vetor.y
        z = vetor.z

    if (eixos == "YZX")
        y = vetor.y + fator1*vetor.z + fator2*vetor.x
        x = vetor.x
        z = vetor.z

    if (eixos == "ZXY")
        z = vetor.z + fator1*vetor.x + fator2*vetor.y
        y = vetor.y
        x = vetor.x

    vetorCisalhado = Vetor(x, y, z)
    return vetorCisalhado
