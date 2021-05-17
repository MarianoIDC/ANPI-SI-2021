import math
import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sym

'''
Cota de error para Trazador Cubico Natural
param func: funcion con al menos 4ta deriva
param S: Lista de puntos
return cota_error: Cota de error
'''

def cota_tras_cubico(func, S):
    h=0
    x = sym.symbols('x')      
    f = sym.sympify(func)     # La funcion se castea en x
    f4 = sym.diff(f,x,4)      # La 4ta derivada
    norm = 0
    for i in range(len(S)):           # Norma infinira
        if (f4.subs(x,S[i])>norm):
            norm = f4.subs(x,S[i])
        else:
            pass
    
    for i in range(len(S)-1):     #Valor h
       if (S[i+1]-S[i]>h):
           h = S[i+1]-S[i]
       else:
           pass
    cota_error = 5*h**4 * norm /384    # Valor cota
    print(float(cota_error))
    return cota_error

if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6]
    func = 'x**4  - (1 / x)'
    cota_tras_cubico(func,S)
