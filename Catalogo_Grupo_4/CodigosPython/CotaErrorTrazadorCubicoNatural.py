import math
import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sym


def cota_tras_cubico(func, S):
    h=0
    x = sym.symbols('x')
    f = sym.sympify(func)
    f4 = sym.diff(f,x,4)
    norm = 0
    for i in range(len(S)):
        if (f4.subs(x,S[i])>0):
            norm = f4.subs(x,S[i])
        else:
            pass
    
    for i in range(len(S)-1):
       if (S[i+1]-S[i]>h):
           h = S[i+1]-S[i]
       else:
           pass
    cota_error = 5*h**4 * norm /384
    print(float(cota_error))
    return cota_error

if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6]
    func = 'x**4  - (1 / x)'
    cota_tras_cubico(func,S)
