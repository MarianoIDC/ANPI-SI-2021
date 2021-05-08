from parte2_p2 import *

def funcionA(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['exp(x1**2) - exp(sqrt(2)*x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionB(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['x1 + exp(x2) - cos(x2)', '3*x1 - x2 - sin(x2)'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionC(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['x1**2 - 2*x1 - x2 + 0.5', 'x1**2 + 4*x2**2 -4'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionD(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['x1**2 + x2**2 - 1', 'x1**2 - x2**2 + 0.5'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionE(x0, iterMax, tol):
    x = np.array(['x1', 'x2'], dtype = object)
    f = np.array(['sin(x1) + x2*cos(x1)', 'x1 - x2'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

def funcionG(x0, iterMax, tol):
    x = np.array(['x1', 'x2', 'x3', 'x4'], dtype = object)
    f = np.array(['x2*x3 + x4*(x2 + x3)', 'x1*x3 + x4*(x1 + x3)', 'x1*x2 + x4*(x2 + x1)', 'x2*x1 + x1*x3 + x2*x3 - 1'], dtype = object)
    xk, itera, error, listaIter, listaError = newton_raphson(x, f, x0, tol, iterMax)
    return xk, itera, error, listaIter, listaError

select = int(input('Escoja un número del 1 al 6: '))
if (select == 1):
    x0 = np.array([2.3, 2.3])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionA(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
elif (select == 2):
    x0 = np.array([1.5, 2])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionB(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
elif (select == 3):
    x0 = np.array([3, 2])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionC(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
elif (select == 4):
    x0 = np.array([-1, -2])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionD(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
elif (select == 5):
    x0 = np.array([1.2, -1.5])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionE(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
elif (select == 6):
    x0 = np.array([2, 2, 2, 0])
    iterMax = 10
    tol = 0.0001
    xAprox, k, err, iter1, err1 = funcionG(x0, iterMax, tol)
    print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
    grafica(iter1, err1)
else:
    print('Por favor digite un número correcto')
