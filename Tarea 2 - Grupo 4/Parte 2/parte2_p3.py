from parte2_p2 import *

def funcionA(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionB(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionC(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionD(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionE(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionD(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

x0 = np.array([0.8, 0.8])
iterMax = 10
tol = 0.0001
xAprox, k, err, iter1, err1 = funcionA(x0, iterMax, tol)
print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
grafica(iter1, err1)
