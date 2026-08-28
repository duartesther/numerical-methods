# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

import numpy as np

def escalona(li, a, ui, b):
    n = len(a)

    if type(li) != np.ndarray:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if type(a) != np.ndarray:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if type(ui) != np.ndarray:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if type(b) != np.ndarray:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if len(li.shape) != 1:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if len(a.shape) != 1:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if len(ui.shape) != 1:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if len(b.shape) != 1:
        assert False, "escalona: Os parâmetros precisam ser ndarrays unidimensionais."
    if len(b) != n:
        assert False, "escalona: Os arrays não possuem tamanhos compatíveis."
    if len(li) != n-1:
        assert False, "escalona: Os arrays não possuem tamanhos compatíveis."
    if len(ui) != n-1:
        assert False, "escalona: Os arrays não possuem tamanhos compatíveis."
    for i in range(n):
        if a[i] == 0:
            assert False, "escalona: Diagonal principal nula, sistema requer pivotamento."

    u_novo = np.zeros_like(ui)
    resposta = np.zeros_like(b)
    u_novo[0] = ui[0]/a[0]
    resposta[0] = b[0]/a[0]

    for i in range(1,n):
        piv = a[i] - li[i-1]*u_novo[i-1]

        if piv == 0:
            assert False, "escalona: Diagonal principal nula, sistema requer pivotamento."
        if ( i < n-1 ):
            u_novo[i] = ui[i]/piv

        resposta[i] = (b[i] - li[i-1]*resposta[i-1])/piv
    return u_novo, resposta

def TDMA_subreg(u_novo, resposta):

    n = len(resposta)
    x = np.zeros_like(resposta)
    x[n-1] = resposta[n-1]

    for i in range(n-2,-1,-1):
        x[i] = resposta[i] - u_novo[i]*x[i+1]
    return x
