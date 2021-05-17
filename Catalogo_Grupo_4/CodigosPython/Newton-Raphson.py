###############################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
###############################################################################


def newton_raphson(func, x0, MAXIT, TOL):
    '''
    Metodo de Newton-Raphson
    :param func: es la funcion a analizar
    :param x0: valor inicial
    :param MAXIT: es la cantidad de iteraciones maximas a realizar
    :param TOL: es la tolerancia del algoritmo
    :return: xAprox: es la solucion, valor aproximado de x
    :return: error: pocentaje de error del resultado obtenido
    '''
    itera = 1
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones
    errl = []  # Lista que almacena el % de error de cada iteracion
    xAprox = x0

    while (itera < MAXIT):
        xk = xAprox
        fd = derivative(func, xk, dx=1e-6)
        xAprox = xk - (func(xk)) / (fd)
        err = (abs(xAprox - xk)) / (abs(xAprox))
        iterl.append(itera)
        errl.append(err)

        if(err < TOL):
            grafica(iterl, errl)
            return xAprox, err
        else:
            itera = itera + 1

    grafica(iterl, errl)
    return xAprox, err


def grafica(listaValoresX, listaValoresY):
    '''
    Grafica
    :param listaValoresX: valores que se graficaran en el eje 'x'
    :param listaValoresY: valores que se graficaran en el eje 'y'
    :return: Grafico con lo valores ingresados
    '''
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()


if __name__ == '__main__':
    # Valor inicial
    x0 = 1
    # Tolerancia
    TOL = 0.0001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    def func(x): return (math.e)**x - 1/x
    # Llamado de la funcion
    xAprox, err = newton_raphson(func, x0, MAXIT, TOL)
    print("######################################################")
    print("Metodo de Newton-Raphson \n")
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))
