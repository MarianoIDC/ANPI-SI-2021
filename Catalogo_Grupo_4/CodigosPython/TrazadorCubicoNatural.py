###############################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy
import numpy as np
from math import *
from sympy import *
import sympy as sym
from sympy import symbols
from Jacobi import jacobi
###############################################################################


def traz_cubico(xk, yk):
    '''
    Metodo del Trazador Cubico
    :param xk: valores en x de los pares ordenados
    :param yk: valores en y de los pares ordenados
    :return: Sx: trazadores cubicos
    '''
    points = []
    n = len(xk)
    for i in range(0, n):
        points.append([xk[i], yk[i]])

    points = np.array([np.array(p) for p in points])
    delta_hk = points[1:, 0] - points[:-1, 0]
    delta_yk = points[1:, 1] - points[:-1, 1]
    A, u = [], []
    k = delta_hk.shape[0]
    for i in range(1, k):
        # Primer caso Ms[1] = 0
        if i == 1:
            A.append([2 * (delta_hk[i - 1] + delta_hk[i]),
                     delta_hk[i]] + [0] * (k - 3))
        # Segundo caso Ms[n+1] = 0
        elif i == k - 1:
            A.append([0] * (k - 3) + [delta_hk[i - 1],
                     2 * (delta_hk[i - 1] + delta_hk[i])])
        else:
            A.append([0] * (i - 2) + [delta_hk[i - 1], 
            2 * (delta_hk[i - 1] + delta_hk[i]), 
            delta_hk[i]] + [0] * (k - 2 - i))
        # Creando el vector u
        u.append(6 * (delta_yk[i] / delta_hk[i] -
                 delta_yk[i - 1] / delta_hk[i - 1]))

    A = np.array([np.array(a) for a in A])
    u = np.array(u)
    # Resolviendo el sistema mediante Jacobi
    x0 = np.zeros(u.shape)
    Ms = jacobi(A, u, u * 0, 0.0000001)
    # Append Ms[1] = 0 and Ms[n+1] = 0
    Ms = np.append(0, np.append(Ms, 0))
    a, b, c, d = [[], [], [], []]
    xk = points[:, 0]
    yk = points[:, 1]
    # Calculando los coeficientes
    for i in range(k):
        a.append((Ms[i + 1] - Ms[i]) / (6 * delta_hk[i]))
        b.append(Ms[i] / 2)
        c.append((yk[i + 1] - yk[i]) / delta_hk[i] -
                 (2 * delta_hk[i] * Ms[i] + delta_hk[i] * Ms[i + 1]) / 6)
        d.append(yk[i])
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)

    # Polinomio trazador
    x = sympy.Symbol('x')
    Sx_tabla = []
    for i in range(0, len(xk) - 1, 1):
        with evaluate(False):
            pxtramo = a[i] * (x - xk[i]) ** 3 + b[i] * \
                (x - xk[i]) ** 2 + c[i] * (x - xk[i]) + d[i]
            Sx_tabla.append(pxtramo)

    print('Trazadores cubicos por tramos \n')
    for tramo in range(1, len(xk), 1):
        print('Sx = [' + str(xk[tramo - 1]) + ',' + str(xk[tramo]) + ']')
        print(str(Sx_tabla[tramo - 1]))

    return a, b, c, d, Sx_tabla


if __name__ == '__main__':
    # Valores xk
    xk = [1, 1.05, 1.07, 1.1]
    # Valores yk
    yk = [2.718282, 3.286299, 3.527609, 3.905416]
    # Funcion
    def func(x): return 3*x*(math.pow(math.e, x)) - 2*(math.pow(math.e, x))
    # Llamado de la funcion
    print("######################################################")
    print("Metodo del Trazador Cubico \n")
    traz_cubico(xk, yk)
