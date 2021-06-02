class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Segmento:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Reta:
    def __init__(self, ponto, vetorDiretor):
        self.ponto = ponto
        self.vetorDiretor = vetorDiretor

class Plano:
    def __init__(self, ponto, vetorNormal):
        self.ponto = ponto
        self.vetorNormal = vetorNormal

class Esfera:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class Base:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3