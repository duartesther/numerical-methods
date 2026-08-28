# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

from integral import simpson13c

densidade = 1.225
def forceDrag(v, A, Cd):
    if v < 0:
        assert False, "forceDrag: velocidade negativa."
    Fd = -densidade*A*Cd*v**2/2
    return Fd

def forceWheel(v, intervalos, coeficientes):
    if v < 0:
        assert False, "forceWheel: velocidade negativa."
    n = len(intervalos)
    Fw = 0
    encontrou = False

    for i in range(n-1):
        if v >= intervalos[i] and v < intervalos[i+1]:
            a0 = coeficientes[i,0]
            a1 = coeficientes[i,1]
            a2 = coeficientes[i,2]
            a3 = coeficientes[i,3]
            Fw = a0 + a1*v + a2*v**2 + a3*v**3
            encontrou = True

    if encontrou == False:
        Fw = 0
    return Fw

def integrando(v, A, Cd, intervalos, coeficientes):
    Fd = forceDrag(v, A, Cd)
    Fw = forceWheel(v, intervalos, coeficientes)
    return 1/(Fd + Fw)

def accelerationTime(vi, vf, m, A, Cd, intervalos, coeficientes):
    if vi < 0:
        assert False, "accelerationTime: velocidade inicial negativa."
    if vf < vi:
        assert False, "accelerationTime: intervalo de velocidades invalido."
    if m <= 0:
        assert False, "accelerationTime: massa invalida."
    integral = simpson13c(integrando, vi, vf, 50, args=(A, Cd, intervalos, coeficientes))
    duracao = m * integral
    return duracao
