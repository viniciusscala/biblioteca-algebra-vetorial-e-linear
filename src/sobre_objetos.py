from estruturas import Plano, Reta, Vetor
from ferramentas_basicas import normalize, saoOrtogonais, projecao

#vetorDiretorReta
def diretor(reta):
    reta = Reta(reta)
    return Vetor(reta)

#normalPlano
def normal(plano):
    plano = Plano(plano)
    return normalize(Vetor)

#verificaParalelo
def eParalelo (vetor,reta):
    reta = Reta(reta)
    vetor = Vetor(vetor)

    if (vetor % reta) == 0:
        return True
    else:
        return False

#ortogonalPlano
def eOrtogonal (vetor, plano):
    vetor = Vetor(vetor)
    plano = Plano(plano)

    if (normalize(plano)) == 0:
        return True
    else:
        return False

#vetorProjetado
def projecaoVR(vetor, reta):
    vetor = Vetor(vetor)
    reta = Reta(reta)

    return projecao(vetor, reta)

#projecaoVetorReta
def projecaoVR(vetor, plano):
    vetor = Vetor(vetor)
    plano = Plano(plano)

    return projecao(vetor,plano)

#componenteOrt
def componenteOrtogonais(vetor, plano):
    plano = Plano(plano)
    vetor = Vetor(vetor)

    if (saoOrtogonais(vetor, plano)) == 0:
        return True
    else:
        return False

#complementoRetaPlano
def saoComplementosOrtogonais(reta, plano):
    plano = Plano(plano)
    reta = Reta(reta)

    if (saoOrtogonais(reta, plano)) == 0:
        return True
    else:
        return False

#complementoPlanoReta
def saoComplementosOrtogonais(plano, reta):
    plano = Plano(plano)
    reta = Reta(reta)

    if (saoOrtogonais(plano, reta)) == 0:
        return True
    else:
        return False

#????
def formaCartesiana(plano):
    plano = Plano(plano)

#????
def formaCartesiana(reta):
    reta = Reta(reta)
