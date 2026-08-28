# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

import math
from secante import secante

g = 9.81
beta = 0.05
TOL = 1E-2
MAX_ITER = 100
X0 = 0
TETA_PADRAO = math.pi/4
VA_PADRAO = 100
XI_PADRAO = 4000

def funcao(x, va, y, teta):
    a = math.tan(teta)
    b = g / (beta * va * math.cos(teta))
    c = (a + b) * x
    aux = 1 - (beta * x) / (va * math.cos(teta))
    d = (g / beta**2) * math.log(aux)
    resultado = c + d - y
    return resultado

def calculaAtraso(y, vI, teta=TETA_PADRAO, vA=VA_PADRAO, xI=XI_PADRAO):

    x1 = 0.3 * xI
    i, xC = secante(funcao, X0, x1, (vA, y, teta), TOL, MAX_ITER)
    tI = (xI - xC) / vI
    aux2 = 1 - (beta * xC) / (vA * math.cos(teta))
    tA = -(1/beta) * math.log(aux2)
    atraso = tI - tA

    if atraso < 0:
        assert False, "calculaAtraso: Míssil não pode ser abatido"
    return atraso, xC
