###############################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sym
from sympy import symbols
from Jacobi import jacobi
###############################################################################

def trazador_cubico(func, S):
    '''
    Metodo del Trazador Cubico
    :param func: funcion sobre la que se realizara el calculo
    :param S: rango de puntos en los que se divide el trazador cubico
    :return: Sx: trazadores cubicos
    '''
    # Procedemos a evaluar los puntos 'x'
    # para encontrar su valor 'y'
    valoresY = []
    k = len(S)
    for i in range(0, k):
        valoresY.append(func(S[i]))
    # Procedemos a agrupar los valores 'xi'
    # y 'yi' en una lista de tuplas
    points = []
    n = len(S)
    for i in range(0, n):
        points.append([S[i], valoresY[i]])

    points = np.array([np.array(p) for p in points])
    # Calculando los delta_hk
    delta_hk = points[1:, 0] - points[:-1, 0]
    # Calculando los delta_yk
    delta_yk = points[1:, 1] - points[:-1, 1]
    # La matriz y el vector para resolver el sistema
    A, u = [], []
    # Cantidad de puntos -1 (n)
    k = delta_hk.shape[0]

    for i in range(1, k):
        # Primer caso Ms[1] = 0
        if i == 1:
            A.append([2 * (delta_hk[i - 1] + delta_hk[i]), delta_hk[i]] + [0] * (k - 3))
        # Segundo caso Ms[n+1] = 0
        elif i == k - 1:
            A.append([0] * (k - 3) + [delta_hk[i - 1], 2 * (delta_hk[i - 1] + delta_hk[i])])
        else:
            A.append(
                [0] * (i - 2) + [delta_hk[i - 1], 2 * (delta_hk[i - 1] + delta_hk[i]), delta_hk[i]] + [0] * (k - 2 - i))
        # Creando el vector u
        u.append(6 * (delta_yk[i] / delta_hk[i] - delta_yk[i - 1] / delta_hk[i - 1]))
    # Convirtiendolo a numpy array
    A = np.array([np.array(a) for a in A])
    u = np.array(u)
    # Resolviendo el sistema mediante Thomas, LU o Jacobi
    x0 = np.zeros(u.shape)
    Ms = jacobi(A, u, u * 0, 0.0000001)
    # Append Ms[1] = 0 and Ms[n+1] = 0
    Ms = np.append(0, np.append(Ms, 0))
    # Coeficientes
    a, b, c, d = [[], [], [], []]
    # Puntos iniciales
    xk = points[:, 0]
    yk = points[:, 1]
    # Calculando los coeficientes
    for i in range(k):
        a.append((Ms[i + 1] - Ms[i]) / (6 * delta_hk[i]))
        b.append(Ms[i] / 2)
        c.append((yk[i + 1] - yk[i]) / delta_hk[i] - (2 * delta_hk[i] * Ms[i] + delta_hk[i] * Ms[i + 1]) / 6)
        d.append(yk[i])

    # Convirtiendo
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)

    Sx = []
    Sxi = []
    x, x0 = symbols('x x0')
    for i in range(len(a)):
        Sx.append(
            a[i] * (math.pow(S[i + 1] - S[i], 3)) + b[i] * (math.pow(S[i + 1] - S[i], 2)) + c[i] * (S[i + 1] - S[i]) + d[i])
        Sxi.append(a[i] * ((x - x0) ** 3) + b[i] * ((x - x0) ** 2) + c[i] * (x - x0) + d[i])

    # Polinomio trazador
    x = sympy.Symbol('x')
    px_tabla = []
    for i in range(0, len(S) - 1, 1):
        pxtramo = a[i] * (x - S[i]) ** 3 + b[i] * (x - S[i]) ** 2
        pxtramo = pxtramo + c[i] * (x - S[i]) + d[i]
        pxtramo = pxtramo.expand()
        px_tabla.append(pxtramo)

    # Polinomios por tramos
    print("######################################################")
    print('Trazadores cubicos por tramos \n')
    for tramo in range(1, len(S)-1, 1):
        print(' Sxi = [' + str(S[tramo - 1]) + ',' + str(S[tramo]) + ']')
        print(str(px_tabla[tramo - 1]))

    xtraza = np.array([])
    ytraza = np.array([])
    tramo = 1

    while not (tramo >= len(S)):
        x0 = S[tramo - 1]
        x1 = S[tramo]
        xtramo = np.linspace(x0, x1, 100)
        # Evalua polinomio del tramo
        pxtramo = px_tabla[tramo - 1]
        pxt = sym.lambdify('x', pxtramo)
        ytramo = pxt(xtramo)
        # Vectores de trazador en x,y
        xtraza = np.concatenate((xtraza, xtramo))
        ytraza = np.concatenate((ytraza, ytramo))
        tramo = tramo + 1

    # Grafica
    grafica(S, valoresY, xtraza, ytraza);
    return a, b, c, d, Sx

def grafica(listaPuntosX, listaPuntosY, trazaX, trazaY):
    '''
    Grafica
    :param listaPuntosX: valores que se graficaran en el eje 'x' 
    :param listaPuntosY: valores que se graficaran en el eje 'y' 
    :param trazaX: traza de los valores en x 
    :param trazaY:  traza de los valores en y
    :return: Grafico con los valores ingresados 
    '''
    plt.plot(listaPuntosX, listaPuntosY, 'ro', label='puntos')
    plt.plot(trazaX, trazaY, label='trazador', color='blue')
    plt.title('Trazadores Cubicos Naturales')
    plt.xlabel('xi')
    plt.ylabel('S(xi)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # Intervalo
    intervalo = [1, 6]
    # Conjunto soporte
    S = [1, 2, 3, 4, 5, 6]
    # S = [1, 1.05, 1.07, 1.1]
    # Funcion
    func = lambda x: x * (math.cos(x)) + math.pow(x, 2) - (1 / x)
    # func = lambda x: 3*x*(math.pow(math.e, x)) - 2*(math.pow(math.e, x))
    # Llamado de la funcion
    a, b, c, d, Sx = trazador_cubico(func, S)
    print("######################################################")
    print("Metodo del Trazador Cubico \n")
    print('a = {}\nb = {}\nc = {}\nd = {}\nSx = {}'.format(a, b, c, d, Sx))