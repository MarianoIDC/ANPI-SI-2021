import numpy as np


from parte2_p2 import *

x = np.array(['x1','x2','x3','x4'], dtype = object)
x0 = np.array([1,-1,1,-1], dtype = float)
f = np.array([
    '((sin(x2))/(5.08))-((sin(x1))/(3.59))',
    '((sin(x3))/(6.22))-((sin(x2))/(5.08))',
    '((sin(x4))/(7.18))-((sin(x3))/(6.22))',
    '(0.2*(tan(x1)+tan(x2)+tan(x3)+tan(x4))-2)'
    ], 
    dtype = object)
"""

x = np.array(['x1','x2','x3'], dtype = object)
x0 = np.array([0.7,0.2,0.1], dtype = float)
f = np.array([
    '98066.5*((x1+x2)*(x1-x3))-(5.97*(1-x1-x2)*(1+x1+x2))',
    '98066.5*((x2+x3)*x2)-(0.27*(1+x1+x2)*(1+x1+x2))',
    '((x1+x3)*x3)-(2.8*(x1-x3)*(x2-x3))'
    ], 
    dtype = object)
"""
tol = 0.0001
iterMax = 10
print("Método de Newton-Raphson para el problema ingenieril \n")
xAprox, k, err, iter1, err1 = newton_raphson(x, f, x0, tol, iterMax)
print('xAprox = {}\nError = {}\nIteraciones = {}'.format(xAprox, err, k))
grafica(iter1, err1)

