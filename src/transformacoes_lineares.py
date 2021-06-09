from estruturas import Vetor
from ferramentas_basicas import reflexao as reflexao_vetor

def reflexao_reta(vetor, vetorDiretor):
    return reflexao_vetor(vetor, vetorDiretor)

def reflexao(vetor):
    return Vetor(-1*vetor.x, -1*vetor.y, -1*vetor.z)

def deformacao(vetor, fatorX, fatorY, fatorZ):
    return Vetor(vetor.x * fatorX, vetor.y * fatorY, vetor.z * fatorZ)