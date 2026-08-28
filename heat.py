# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

import numpy as np
from tdma import escalona, TDMA_subreg

def novaTemperatura(T, L, alpha, xi, dt):

    assert alpha > 0, "novaTemperatura: Valor não positivo para a difusividade térmica"
    assert L > 0, "novaTemperatura: Comprimento da barra deve ser positivo"
    assert len(T) >= 3, "novaTemperatura: Array de temperatura deve possuir um mínimo de 3 elementos"

    N = len(T)
    passo = L/N
    fator = (1/alpha) * (passo**2/dt)
    gama = xi * passo**2
    li = np.zeros(N-1)
    a = np.zeros(N)
    ui = np.zeros(N-1)
    b = np.zeros(N)

    for i in range(N-1):
        li[i] = 1
        ui[i] = 1

    for i in range(N):
        if ( i == 0 ):
            a[i] = -(1+fator)
        elif ( i == N-1 ):
            a[i] = -(1+fator)
        else:
            a[i] = -(2+fator)

        b[i] = -fator*T[i] - gama

    u_novo, resposta = escalona(li, a, ui, b)
    Tnovo = TDMA_subreg(u_novo, resposta)

    return Tnovo
