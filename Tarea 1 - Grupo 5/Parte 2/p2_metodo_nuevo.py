import math
import numpy as np
import p2_aux as pa


# Metodo de Ren
# Entradas:
            #f: es la funcion a analizar
            #x0: valor inicial
            #iterMax: es la cantidad de iteraciones maximas a realizar
            #tol: es la tolerancia del algoritmo
# Salidas:
            #xk: es la solucion, valor aproximado de x
            #k: es la cantidad de iteraciones
            #error: pocentaje de error del resultado obtenido
def metodo_nuevo(f, x0, iterMax, tol):
    k = 1
    err = 1
    xk = x0
    iteraciones = []
    errores = []
    while(k < iterMax):
        wk = xk + f(xk)
        yk = xk - f(xk)/(f(xk)*f(wk))
        xk = yk - f(yk)/(f(xk)*f(yk) + f(yk)*f(xk) - f(xk)*f(wk))
        err = abs(xk)
        if (err < tol):
            print("Metodo de Ren \n")
            print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
            pa.grafica(iteraciones, errores)
            return xk, k, err, iteraciones, errores
        else:
            k = k + 1
            iteraciones.append(k)
            errores.append(err)
    print("Metodo de Newton-Raphson \n")
    print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
    pa.grafica(iteraciones, errores)
    return xk, k, err, iteraciones, errores
