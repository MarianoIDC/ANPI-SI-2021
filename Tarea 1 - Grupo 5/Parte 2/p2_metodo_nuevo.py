import math
import numpy as np

def metodoNuevo(f, x0, iterMax, tol):
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
            return xk, k, err, iteraciones, errores
        else:
            k = k + 1
            iteraciones.append(k)
            errores.append(err)
    return xk, k, err, iteraciones, errores
