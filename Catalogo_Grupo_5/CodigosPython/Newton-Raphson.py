# Metodo de Newton-Raphson
# Entradas:
            # func: es la funcion a analizar
            # x0: valor inicial
            # MAXIT: es la cantidad de iteraciones maximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

###############################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import sys
###############################################################################

def newtonRaphson(func, x0, MAXIT, TOL):
    itera = 0
    err = 1
    iterl = []
    errl = []
    xAprox = x0

    while (err > TOL):
        xk = xAprox
        fd = derivative(func, xk, dx=1e-6)
        xAprox = xk - (func(xk)) / (fd)

        err = (abs(xAprox - xk)) / (abs(xAprox))

        iterl.append(itera)
        errl.append(err)

        itera = itera + 1

    plt.plot(iterl, errl)
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.title("Metodo de Newton-Raphson")
    plt.show()
    return xAprox, itera


if __name__ == '__main__':
    # Valor inicial
    x0 = 3 / 4
    # Tolerancia
    TOL = 0.0000000001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: (math.cos(2 * x)) ** 2 - x ** 2
    # Llamado de la funcion
    xAprox, itera = newtonRaphson(func, x0, MAXIT, TOL)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, itera))
