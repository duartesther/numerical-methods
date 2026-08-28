# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 2026

@author: 24250464
"""

def simpson13c(f, a, b, n, args=()):

    if type(n) != int:
        assert False, "simpson13: numero de subintervalos invalido."
    if n <= 0:
        assert False, "simpson13: numero de subintervalos invalido."
    if n % 2 != 0:
        assert False, "simpson13: numero de subintervalos invalido."

    h = (b - a)/n
    acumulado = 0

    for i in range(1, n):
        x = a + i*h

        if i % 2 != 0:
            acumulado = acumulado + 4*f(x, *args)
        else:
            acumulado = acumulado + 2*f(x, *args)

    acumulado = acumulado + f(a, *args) + f(b, *args)
    integral = (h/3) * acumulado
    return integral
