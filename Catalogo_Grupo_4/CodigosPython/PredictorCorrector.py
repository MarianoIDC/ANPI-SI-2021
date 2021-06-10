###############################################################################
import numpy as np
import sympy as sp
###############################################################################


def predictor_corrector(f, a, b, y0, N):
    '''
    Metodo de Predictor-Corrector
    :param f: es la funcion a analizar
    :param a: inicio del intervalo
    :param b: final del intervalo
    :param y0: valor inicial del problema
    :param N: cantidad de puntos a evaluar en el metodo
    :return: xv: es el conjunto de puntos del eje de las abscisas
    :return: yv: es el conjunto de puntos del eje de las ordenadas
    :return: p: polinomio de interpolacion del metodo
    '''
    x = sp.symbols('x')
    y = sp.symbols('y')
    f1 = sp.lambdify([x, y], f, modules = ['numpy'])
    h = (b - a)/(N - 1)
    xv = np.linspace(a, b, N)
    yv = np.zeros(N, dtype = float)
    yv[0] = y0
    for k in range(N - 1):
        euler = yv[k] + h * f1(xv[k], yv[k])
        yv[k + 1] = yv[k] + (h / 2) * (f1(xv[k], yv[k]) + f1(xv[k + 1], euler))
    polinomio_inter =0
    '''
    Metodo de Lagrange
    :param xv: es el conjunto de puntos del eje de las abscisas
    :param yv: es el conjunto de puntos del eje de las ordenadas
    :return: Polinomio de interpolacion
    '''
    for i in range(len(yv)):
        Lk = 1
        for j in range(len(xv)):
            if i==j:
                pass
            else:
                Lk = sp.Mul(Lk, sp.Mul((x - xv[j]), sp.Pow((xv[i] - xv[j]), -1)))
        polinomio_inter = polinomio_inter + yv[i] * Lk
    polinomio_inter = sp.simplify(polinomio_inter)
    return xv, yv, polinomio_inter

#Funcion a evaluar con sus variables simbolicas
x = sp.symbols('x')
y = sp.symbols('y')
f = y - x**2 + 1
#Valor inicial
y0 = 0.5
#Intervalo de la funcion
a = 0
b = 2
#Cantidad de puntos a evaluar
N = 11
#Llamado de la funcion
xv, yv, p = predictor_corrector(f, a, b, y0, N)
print('Eje de las abscisas = {}\nEje de las ordenadas = {}\nPolinomio de interpolacion = {}'.format(xv, yv, p))
#Grafica de la funcion
sp.plot(p, (x, 0, 2))

    
