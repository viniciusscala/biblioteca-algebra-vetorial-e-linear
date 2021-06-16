from ferramentas_basicas import produtoEscalar
from estruturas import Base, Vetor

def somaVetorial(vetor1, vetor2):
  return Vetor( vetor1.x + vetor2.x, vetor1.y + vetor2.y, vetor1.z + vetor2.z)

def subtracaoVetorial(vetor1, vetor2):
  return Vetor( vetor1.x - vetor2.x, vetor1.y - vetor2.y, vetor1.z - vetor2.z)

def subtracaoVetorial3(vetor1, vetor2, vetor3):
  return Vetor( vetor1.x - vetor2.x - vetor3.x, vetor1.y - vetor2.y - vetor3.y, vetor1.z - vetor2.z - vetor3.z)

def multiplicacaoPorEscalar(escalar, vetor):
  return Vetor( vetor.x * escalar, vetor.y * escalar, vetor.z * escalar)

def ortogonalize(base):
  v1 = base.v1
  v2 = base.v2
  v3 = base.v3

  w1 = v1
  w2 = subtracaoVetorial(v2, multiplicacaoPorEscalar((produtoEscalar(v2, w1)/produtoEscalar(w1, w1)), w1))
  w3 = subtracaoVetorial3(v3, multiplicacaoPorEscalar((produtoEscalar(v3, w2)/produtoEscalar(w2, w2)), w2), multiplicacaoPorEscalar((produtoEscalar(v3, w1)/produtoEscalar(w1, w1)), w1))

  return Base(w1, w2, w3)

def mudeBase(vetor, base):
  equacao1 = False
  equacao2 = False
  equacao3 = False

  margin = 100

  keep_going = True
  a = -margin
  while a <= margin and keep_going:
    a += 1
    b = -margin
    while b <= margin and keep_going:
      b += 1
      c = -margin
      while c <= margin and keep_going:
        c += 1

        equacao1 = vetor.x == (a * base.v1.x) + (b * base.v2.x) + (c * base.v3.x)
        equacao2 = vetor.y == (a * base.v1.y) + (b * base.v2.y) + (c * base.v3.y)
        equacao3 = vetor.z == (a * base.v1.z) + (b * base.v2.z) + (c * base.v3.z)

        keep_going = not(equacao1 and equacao2 and equacao3)
  

  return [a, b, c]
  
