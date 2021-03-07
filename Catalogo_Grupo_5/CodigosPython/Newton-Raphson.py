# Metodo de Newton-Raphson
# Entradas:
            # func: es la funcion a analizar
            # x0: valor inicial
            # MAXIT: es la cantidad de iteraciones maximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
########################################################################################

def newtonRaphson(func, x0, MAXIT, TOL):
    itera = 1
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
    errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
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
    func = lambda x: (math.e)**x - 1/x
    # Llamado de la funcion
    xAprox, err = newtonRaphson(func, x0, MAXIT, TOL)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))