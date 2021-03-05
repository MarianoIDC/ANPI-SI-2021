#Metodo de la Biseccion
#Entradas:
            #func: es la funcion a analizar
            #a: es "a" valor inferior en el intervalo de la funcion en el rango [a, b]
            #b: es "b" valor superior en el intervalo de la funcion en el rango [a, b]
            #MAXIT: es la cantidad de iteraciones máximas a realizar
            #TOL: es la tolerancia del algoritmo
#Salidas:
            #xAprox: es la solucion, valor aproximado de x
            #error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
########################################################################################

def biseccion(func, a, b, MAXIT, TOL):

    if(func(a) * func(b) < 0):
        itera = 0
        err = 0
        iterl = []
        errl = []

        while(itera < MAXIT):
            xAprox = (a + b) / 2
            fx = func(xAprox)

            if(func(a) * fx  < 0):
                b = xAprox
            elif(func(b) * fx < 0):
                a = xAprox
            elif(abs(fx) < TOL):
                plt.plot(iterl, errl)
                plt.xlabel("Iteraciones")
                plt.ylabel("% Error")
                plt.title("Metodo de la Biseccion")
                plt.show()
                return xAprox, itera

            iterl.append(itera)
            errl.append(err)

            itera = itera + 1
            err = (b - a) / (2)
    else:
        print("Las condiciones  no garantizan el cero de la funcion")


if __name__ == '__main__':
    #Limites
    a = 0
    b = 2
    #Tolerancia
    TOL = 0.000001
    #Maximo iteraciones
    MAXIT = 100
    #Funcion
    func = lambda x: math.e**x - x - 2
    #Llamado de la funcion
    xAprox, iter = biseccion(func, a, b, MAXIT, TOL)
    #print(xAprox)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, iter))


# Metodo de la Falsa Posicion
# Entradas:
            # func: es la funcion a analizar
            # x0: primer valor inicial
            #x1: segundo valor inicial
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import sys
########################################################################################


def falsa_posicion(func, x0, x1, MAXIT, TOL):
    a = x0
    b = x1

    if (func(a) * func(b) < 0):
        itera = 0
        err = 1
        iterl = []
        errl = []
        x2 = 0
        xAprox = 0

        x2 = x1 - ((x1 - x0) / (func(x1) - func(x0))) * func(x1)

        if(func(a) * func(x2) < 0):
            itera = 2
            while(err > TOL):
                xAprox = x2 - ((x2 - a)/(func(x2) - func(a))) * func(x2)

                err = (abs(xAprox - x2)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)
                itera = itera + 1

                a = x2
                x2 = xAprox

            plt.plot(iterl, errl)
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.title("Metodo de la Falsa Posicion")
            plt.show()
            return xAprox, itera

        elif(func(x2) * func(b) < 0):
            itera = 2
            while (err > TOL):
                xAprox = b - ((b - x2) / (func(b) - func(x2))) * func(b)

                err = (abs(xAprox - b)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)
                itera = itera + 1

                x2 = b
                b = xAprox

            plt.plot(iterl, errl)
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.title("Metodo de la Falsa Posicion")
            plt.show()
            return xAprox, itera

        else:
            raise ValueError("Las condiciones no garantizan el cero de la funcion")
    else:
        raise ValueError("Las condiciones no garantizan el cero de la funcion")

if __name__ == '__main__':
    # Valor inicial
    x0 = 1/2
    x1 = (math.pi)/4
    # Tolerancia
    TOL = 0.00001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: math.cos(x) - x
    # Llamado de la funcion
    xAprox, itera = falsa_posicion(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, itera))



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
import numpy as np
import sys
########################################################################################

def newton_raphson(func, x0, MAXIT, TOL):
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
    xAprox, itera = newton_raphson(func, x0, MAXIT, TOL)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, itera))

# Metodo de la Secante
# Entradas:
            # func: es la funcion a analizar
            # x0: valor iniciar
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import sys
########################################################################################

def secante(func, x0, x1, MAXIT, TOL):
    itera = 0
    err = 1
    iterl = []
    errl = []
    xAprox = x0;

    while(err > TOL):

        xAprox = x1 - ((x1 - x0)/(func(x1) - func(x0)))  * func(x1)

        err = abs(xAprox - x1)/abs(xAprox)
        iterl.append(itera)
        errl.append(err)
        itera = itera + 1

        x0 = x1
        x1 = xAprox

    plt.plot(iterl, errl)
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.title("Metodo de la Secante")
    plt.show()
    return xAprox, itera

if __name__ == '__main__':
    # Valor inicial
    x0 = 0
    x1 = 1
    # Tolerancia
    TOL = 0.0001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xAprox, itera = secante(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, itera))