# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

TOL = 1E-3
MAX_ITER = 100

def secante(f, x0, x1, args=(), tolerancia=TOL, max_iteracoes=MAX_ITER):
    if x0 == x1:
        assert False, "Secante: As estimativas iniciais são iguais"
    i = 1
    convergiu = False

    while i < max_iteracoes:
        y0 = f(x0, *args)
        y1 = f(x1, *args)
        a = y1 * (x1 - x0)
        b = y1 - y0
        x2 = x1 - a/b
        dif = x2 - x1

        if dif < 0:
            dif = -dif

        if dif < tolerancia:
            convergiu = True
            break
        x0 = x1
        x1 = x2
        i = i + 1

    if convergiu == False:
        assert False, "Secante: Número máximo de iterações alcançado"
    return i + 1, x2
