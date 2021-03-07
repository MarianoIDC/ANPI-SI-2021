#Metodo de la Biseccion
#Entradas:
            #f: es la funcion a analizar
            #a: es "a" valor inferior en el intervalo de la funcion en el rango [a, b]
            #b: es "b" valor superior en el intervalo de la funcion en el rango [a, b]
            #iterMax: es la cantidad de iteraciones máximas a realizar
            #tol: es la tolerancia del algoritmo
#Salidas:
            #xk: es la solucion, valor aproximado de x
            #k: es la cantidad de iteraciones
            #error: pocentaje de error del resultado obtenido

########################################################################################
import math
from scipy.misc import derivative
print("###############################################")
########################################################################################

def biseccion(f, a, b, iterMax, tol):

    if(f(a) * f(b) < 0):
        k = 1
        err = 1

        while(k < iterMax):
            xk = (a + b) / 2
            fx = f(xk)

            if(f(a) * fx  < 0):
                b = xk
            elif(f(b) * fx < 0):
                a = xk

            err = abs(f(xk))

            if(err < tol):
                return xk, k, err
            else:
                k = k + 1
        return xk, k, err
    else:
        raise ValueError("Las condiciones  no garantizan el cero de la funcion.")

if __name__ == '__main__':
    #Intervalos
    a = 0
    b = 2
    #Tolerancia
    tol = 0.0001
    #Maximo iteraciones
    iterMax = 100
    #Funcion
    f = lambda x: math.e**x - x - 2
    #Llamado de la funcion
    xk, k, err = biseccion(f, a, b, iterMax, tol)
    print("Metodo de la Biseccion \n")
    print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
    print("################################################")


# Metodo de la Falsa Posicion
# Entradas:
            #f: es la funcion a analizar
            #a: primer valor inicial
            #b: segundo valor inicial
            #iterMax: es la cantidad de iteraciones máximas a realizar
            #tol: es la tolerancia del algoritmo
# Salidas:
            #xk: es la solucion, valor aproximado de x
            #k: es la cantidad de iteraciones
            #error: pocentaje de error del resultado obtenido

def falsa_posicion(f, a, b, iterMax, tol):

    if (f(a) * f(b) < 0):
        k = 1
        err = 1
        xk = 0
        x2 = a - ((b - a) / (f(b) - f(a))) * f(b)

        if (f(a) * f(x2) < 0):

            while (k < iterMax):
                xk = x2 - ((x2 - a) / (f(x2) - f(a))) * f(x2)
                err = abs(f(xk))
                
                if (err < tol):
                    return xk, k, err
                else:
                    k = k + 1
                    a = x2
                    x2 = xk
            return xk, k, err

        elif (f(x2) * f(b) < 0):

            while (k < iterMax):
                xk = b - ((b - x2) / (f(b) - f(x2))) * f(b)
                err = abs(f(xk))
                
                if (err < tol):
                    return xk, k, err
                else:
                    k = k + 1
                    x2 = b
                    b = xk
            return xk, k, err
        else:
            raise ValueError("Las condiciones no garantizan el cero de la funcion")
    else:
        raise ValueError("Las condiciones no garantizan el cero de la funcion")

if __name__ == '__main__':
    # Intervalos
    a = 1/2
    b = (math.pi)/4
    # Tolerancia
    tol = 0.00001
    # Maximo iteraciones
    iterMax = 100
    # Funcion
    f = lambda x: math.cos(x) - x
    # Llamado de la funcion
    xk, k, err = falsa_posicion(f, a, b, iterMax, tol)
    print("Metodo de la Falsa Posicion \n")
    print('xAprox = {}\nk = {} \nerror = {}'.format(xk, k, err))
    print("######################################################")



# Metodo de Newton-Raphson
# Entradas:
            #f: es la funcion a analizar
            #x0: valor inicial
            #iterMax: es la cantidad de iteraciones maximas a realizar
            #tol: es la tolerancia del algoritmo
# Salidas:
            #xk: es la solucion, valor aproximado de x
            #k: es la cantidad de iteraciones
            #error: pocentaje de error del resultado obtenido

def newton_raphson(f, x0, iterMax, tol):
    k = 1
    err = 1
    xk = x0

    while (k < iterMax):
        xkm = xk
        fd = derivative(f, xkm, dx=1e-6)
        xk = xkm - (f(xkm)) / (fd)
        err = abs(f(xk))

        if(err < tol):
            return xk, k, err
        else:
            k = k + 1
    return xk, k, err

if __name__ == '__main__':
    # Valor inicial
    x0 = 1
    # Tolerancia
    tol = 0.0001
    # Maximo iteraciones
    iterMax = 100
    # Funcion
    f = lambda x: (math.e)**x - 1/x
    # Llamado de la funcion
    xk, k, err = newton_raphson(f, x0, iterMax, tol)
    print("Metodo de Newton-Raphson \n")
    print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
    print("################################################")

# Metodo de la Secante
# Entradas:
            #f: es la funcion a analizar
            #x0: valor inicial
            #x1: valor inicial
            #iterMax: es la cantidad de iteraciones máximas a realizar
            #tol: es la tolerancia del algoritmo
# Salidas:
            #xk: es la solucion, valor aproximado de x
            #k: cantidad de iteraciones
            #error: pocentaje de error del resultado obtenido

def secante(f, x0, x1, iterMax, tol):
    k = 2
    err = 1
    xk = x0

    while(k < iterMax):

        xk = x1 - ((x1 - x0) / (f(x1) - f(x0)))  * f(x1)
        err = abs(f(xk))

        if(err < tol):
            return xk, k, err
        else:
            k = k + 1
            x0 = x1
            x1 = xk
    return xk, k, err

if __name__ == '__main__':
    # Valores iniciales
    x0 = 0
    x1 = 1
    # Tolerancia
    tol = 0.01
    # Maximo iteraciones
    iterMax = 100
    # Funcion
    f = lambda x: (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xk, k, err = secante(f, x0, x1, iterMax, tol)
    print("Metodo de la Secante \n")
    print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
    print("###############################################")
