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
########################################################################################

def biseccion(func, a, b, MAXIT, TOL):

    if(func(a) * func(b) < 0):
        itera = 1
        err = 1
        iterl = [] # Lista que almacena el numero de iteraciones para despues graficar
        errl = [] # Lista que almacena el % de error de cada iteracion para despues graficar

        while(itera < MAXIT):
            xAprox = (a + b) / 2
            fx = func(xAprox)

            if(func(a) * fx  < 0):
                b = xAprox
            elif(func(b) * fx < 0):
                a = xAprox

            iterl.append(itera)
            errl.append(err)
            itera = itera + 1
            err = (b - a) / (2)**(itera-1)

            if(err < TOL):
                plt.plot(iterl, errl, 'bx')
                plt.title("Metodo de la Biseccion")
                plt.xlabel("Iteraciones")
                plt.ylabel("% Error")
                plt.show()
                return xAprox, err

        plt.plot(iterl, errl, 'bx')
        plt.title("Metodo de la Biseccion")
        plt.xlabel("Iteraciones")
        plt.ylabel("% Error")
        plt.show()
        return xAprox, err
    else:
        raise ValueError("Las condiciones  no garantizan el cero de la funcion.")

if __name__ == '__main__':
    #Intervalos
    a = 0
    b = 2
    #Tolerancia
    TOL = 0.0001
    #Maximo iteraciones
    MAXIT = 100
    #Funcion
    func = lambda x: math.e**x - x - 2
    #Llamado de la funcion
    xAprox, err = biseccion(func, a, b, MAXIT, TOL)
    #print(xAprox)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))


# Metodo de la Falsa Posicion
# Entradas:
            # func: es la funcion a analizar
            # x0: primer valor inicial
            # x1: segundo valor inicial
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
########################################################################################

def falsa_posicion(func, x0, x1, MAXIT, TOL):
    a = x0
    b = x1

    if (func(a) * func(b) < 0):
        itera = 0
        err = 1
        iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
        errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
        xAprox = 0

        x2 = x1 - ((x1 - x0) / (func(x1) - func(x0))) * func(x1)

        if (func(a) * func(x2) < 0):

            while (itera < MAXIT):
                xAprox = x2 - ((x2 - a) / (func(x2) - func(a))) * func(x2)
                err = (abs(xAprox - x2)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)

                if (err < TOL):
                    plt.plot(iterl, errl, 'bx')
                    plt.title("Metodo de la Falsa Posicion")
                    plt.xlabel("Iteraciones")
                    plt.ylabel("% Error")
                    plt.show()
                    return xAprox, err
                else:
                    itera = itera + 1
                    a = x2
                    x2 = xAprox

            plt.plot(iterl, errl, 'bx')
            plt.title("Metodo de la Falsa Posicion")
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.show()
            return xAprox, err

        elif (func(x2) * func(b) < 0):

            while (itera < MAXIT):
                xAprox = b - ((b - x2) / (func(b) - func(x2))) * func(b)
                err = (abs(xAprox - b)) / (abs(xAprox))
                iterl.append(itera)
                errl.append(err)

                if (err < TOL):
                    plt.plot(iterl, errl, 'bx')
                    plt.title("Metodo de la Falsa Posicion")
                    plt.xlabel("Iteraciones")
                    plt.ylabel("% Error")
                    plt.show()
                    return xAprox, err
                else:
                    itera = itera + 1
                    x2 = b
                    b = xAprox
                    
            plt.plot(iterl, errl, 'bx')
            plt.title("Metodo de la Falsa Posicion")
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.show()
            return xAprox, err
        else:
            raise ValueError("Las condiciones no garantizan el cero de la funcion")
    else:
        raise ValueError("Las condiciones no garantizan el cero de la funcion")

if __name__ == '__main__':
    # Intervalos
    x0 = 1 / 2
    x1 = (math.pi) / 4
    # Tolerancia
    TOL = 0.00001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: math.cos(x) - x
    # Llamado de la funcion
    xAprox, err = falsaPosicion(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))



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

def newton_raphson(func, x0, MAXIT, TOL):
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
            plt.plot(iterl, errl, 'bx')
            plt.title("Metodo de Newton-Raphson")
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.show()
            return xAprox, err
        else:
            itera = itera + 1

    plt.plot(iterl, errl, 'bx')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()
    return xAprox, err

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
########################################################################################

def secante(func, x0, x1, MAXIT, TOL):
    itera = 2
    err = 1
    iterl = []  # Lista que almacena el numero de iteraciones para despues graficar
    errl = []  # Lista que almacena el % de error de cada iteracion para despues graficar
    xAprox = x0

    while(itera < MAXIT):

        xAprox = x1 - ((x1 - x0) / (func(x1) - func(x0)))  * func(x1)
        err = abs(xAprox - x1) / abs(xAprox)
        iterl.append(itera)
        errl.append(err)

        if(err < TOL):
            plt.plot(iterl, errl, 'bx')
            plt.title("Metodo de la Secante")
            plt.xlabel("Iteraciones")
            plt.ylabel("% Error")
            plt.show()
            return xAprox, err
        else:
            itera = itera + 1
            x0 = x1
            x1 = xAprox

    plt.plot(iterl, errl, 'bx')
    plt.title("Metodo de la Secante")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()
    return xAprox, err

if __name__ == '__main__':
    # Valores iniciales
    x0 = 0
    x1 = 1
    # Tolerancia
    TOL = 0.01
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xAprox, err = secante(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\n%Error = {}'.format(xAprox, err))
