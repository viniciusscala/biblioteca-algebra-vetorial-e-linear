from estruturas import *
from ferramentas_basicas import produtoEscalar, produtoVetorial, norma2, saoParalelos
from math import sqrt

def intersecao(reta1, reta2):
    coordA = reta1.vetorDiretor
    coordB = reta2.vetorDiretor

    coordC_x = reta2.ponto.x - reta1.ponto.x
    coordC_y = reta2.ponto.y - reta1.ponto.y
    coordC_z = reta2.ponto.z - reta1.ponto.z

    coordC = Ponto(coordC_x, coordC_y, coordC_z)

    if(saoParalelos(coordA, coordB)):
        return None

    if (produtoEscalar(coordC, produtoVetorial(coordA,coordB)) != 0.0): # lines are not coplanar
        return None

    s = produtoEscalar(produtoVetorial(coordC,coordB), produtoVetorial(coordA, coordB)) \
        / norma2(produtoVetorial(coordA, coordB))

    if(s >= 0.0 and s <= 1.0):
        ipX = reta1.ponto.x + coordA.x * s
        ipY = reta1.ponto.y + coordA.y * s
        ipZ = reta1.ponto.z + coordA.z * s

        ip = Ponto(ipX, ipY, ipZ)
        return ip

    return None

def intersecao(reta, plano):
    escalar = produtoEscalar(reta.vetorDiretor, plano.vetorNormal)

    if(escalar == 0): #reta e plano sao paralelos
        return None

    w_x = reta.ponto.x - plano.ponto.x
    w_y = reta.ponto.y - plano.ponto.y
    w_z = reta.ponto.z - plano.ponto.z
    
    w = Ponto(w_x, w_y, w_z)
    si = -produtoEscalar(plano.vetorNormal, w) / escalar
    
    pontoIntersecao_x = w_x + si * reta.vetorDiretor.x + plano.ponto.x
    pontoIntersecao_y = w_y + si * reta.vetorDiretor.y + plano.ponto.y
    pontoIntersecao_z = w_z + si * reta.vetorDiretor.z + plano.ponto.z

    pontoIntersecao = Ponto(pontoIntersecao_x, pontoIntersecao_y, pontoIntersecao_z)
    return pontoIntersecao

def intersecao(plano1, plano2):
    u = produtoVetorial(plano1.vetorNormal, plano2.vetorNormal)
    ax = u.x if u.x >= 0 else -u.x
    ay = u.y if u.y >= 0 else -u.y
    az = u.z if u.z >= 0 else -u.z

    if ((ax+ay+az) < 0.00000001):       
        vx = plano2.ponto.x - plano1.ponto.x
        vy = plano2.ponto.y - plano1.ponto.y
        vz = plano2.ponto.z - plano1.ponto.z
        v = Ponto(vx, vy, vz)

        if (produtoEscalar(plano1.vetorNormal, v) == 0):       
            return plano1                  # Pn1 and Pn2 coincide
        else:
            return None                    # Pn1 and Pn2 are disjoint
    
    if (ax > ay):
        if (ax > az):
            maxc =  1
        else: maxc = 3
    
    else:
        if (ay > az):
            maxc =  2
        else: maxc = 3

    iP = Ponto(None, None, None)                    # intersect point            
    d1 = -produtoEscalar(plano1.vetorNormal,plano1.ponto);   
    d2 = -produtoEscalar(plano2.vetorNormal, plano2.ponto);   

    if maxc == 1:                   # intersect with y=0  
        iP.x = 0
        iP.y = (d2*plano1.vetorNormal.z - d1*plano2.vetorNormal.z) /  u.x
        iP.z = (d1*plano2.vetorNormal.y - d2*plano1.vetorNormal.y) /  u.x
    
    if maxc == 2:                   # intersect with y=0
        iP.x = (d1*plano2.vetorNormal.z - d2*plano1.vetorNormal.z) /  u.y
        iP.y = 0
        iP.z = (d2*plano1.vetorNormal.x - d1*plano2.vetorNormal.x) /  u.y

    if maxc == 3:                   # intersect with z=0
        iP.x = (d2*plano1.vetorNormal.y - d1*plano2.vetorNormal.y) /  u.z
        iP.y = (d1*plano2.vetorNormal.x - d2*plano1.vetorNormal.x) /  u.z
        iP.z = 0    

    return Reta(iP, u)

def intersecao(reta, triangulo):
    zero = 0.00000001
    vetorZerado = Vetor(0, 0, 0)

    u = Vetor(triangulo.p2.x-triangulo.p1.x, triangulo.p2.y-triangulo.p1.y, triangulo.p2.z-triangulo.p1.z)
    v = Vetor(triangulo.p3.x-triangulo.p1.x, triangulo.p3.y-triangulo.p1.y, triangulo.p3.z-triangulo.p1.z)
    n = produtoVetorial(u, v)

    if(n == vetorZerado):            # Triangulo Deformado
        return None

    w0 = Vetor(reta.ponto.x-triangulo.p1.x, reta.ponto.y-triangulo.p1.y, reta.ponto.z-triangulo.p1.z) 
    a = -produtoEscalar(n, w0)
    b = produtoEscalar(n, reta.vetorDiretor)
    if (abs(b) < zero):             # reta é paralela ao triangulo
        if (a == 0):
            return reta             # reta esta no plano do triangulo
        else: 
            return None             # Não tem intercecção

    r = a/b
    if (r < 0.0):                    # Sem intercecção
        return None

    ipX = reta.ponto.x + (reta.vetorDiretor.xr)
    ipY = reta.ponto.y + (reta.vetorDiretor.yr)
    ipZ = reta.ponto.z + (reta.vetorDiretor.zr)
    ip = Ponto(ipX, ipY, ipZ)       # ponto de intercecção entre a reta e PLANO do triangulo

    # checar se o ponto esta no triangulo
    uu = produtoEscalar(u, u)
    uv = produtoEscalar(u, v)
    vv = produtoEscalar(u, v)
    w = Vetor(ip.x-triangulo.p1.x, ip.y-triangulo.p1.y, ip.z-triangulo.p1.z)
    wu = produtoEscalar(w, u)
    wv = produtoEscalar(w, v)
    D = (uv * uv) - (uu * vv)

    s = ((uv * wv) - (vv * wu)) / D
    if (s < 0.0 or s > 1.0):         # ponto esta fora do triangulo
        return None
    t = ((uv * wu) - (uu * wv)) / D
    if (t < 0.0 or (s + t) > 1.0):   # ponto esta fora do triangulo
        return None

    return ip                       # ponto esta no triangulo

def intersecao(reta, esfera):
    x = esfera.centro.x - reta.ponto.x
    y = esfera.centro.y - reta.ponto.y
    z = esfera.centro.z - reta.ponto.z
    centro_reta = Vetor(x, y, z)

    a = norma2(reta.vetorDiretor)
    b = -2 * produtoEscalar(reta.vetorDiretor, centro_reta)
    c = norma2(centro_reta) - (esfera.raio ** 2)
    delta = (b ** 2) - (4 * a * c)

    if delta == 0:
        t = (-b + sqrt(delta)) / 2 * a
        
        iPx = reta.ponto.x + reta.vetorDiretor.x * t
        iPy = reta.ponto.y + reta.vetorDiretor.y * t
        iPz = reta.ponto.z + reta.vetorDiretor.z * t

        return Ponto(iPx, iPy, iPz)

    if delta > 0:
        t1 = (-b + sqrt(delta)) / (2 * a)

        iPx = reta.ponto.x + (reta.vetorDiretor.x * t1)
        iPy = reta.ponto.y + (reta.vetorDiretor.y * t1)
        iPz = reta.ponto.z + (reta.vetorDiretor.z * t1)

        iP_one = Ponto(iPx, iPy, iPz)

        t2 = (-b - sqrt(delta)) / (2 * a)

        iPx = reta.ponto.x + (reta.vetorDiretor.x * t2)
        iPy = reta.ponto.y + (reta.vetorDiretor.y * t2)
        iPz = reta.ponto.z + (reta.vetorDiretor.z * t2)

        iP_two = Ponto(iPx, iPy, iPz)

        return [iP_one, iP_two]

    return None
