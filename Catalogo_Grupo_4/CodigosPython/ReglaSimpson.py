###############################################################################
from numpy import double
from sympy import symbols, sympify, diff
###############################################################################


def simpson(funcion, a, b):
    '''
    Metodo de la Regla de Simpson
    :param funcion: funcion a la cual se le calculara el area
    :param a: intervalo inferior
    :param b: intervalo superior
    :return: xAprox: aproximacion del area
    :return: error: error de la solucion
    '''
    x = symbols('x')
    f = sympify(funcion)
    m = (a + b)/2
    xAprox = double(((b - a)/6)*(f.subs(x, a) + 4*f.subs(x, m) + f.subs(x, b)))
    fdddd = diff(f, x, x, x, x)
    lista = []
    lista.append(abs(double(fdddd.subs(x, a))))
    lista.append(abs(double(fdddd.subs(x, b))))
    vmax = max(lista)
    error = double(((((b - a)/2)**5)/(90))*(vmax))
    return xAprox, error


if __name__ == '__main__':
    # Intervalo inferior
    a = 2
    # Intervalo superior
    b = 5
    # Funcion
    funcion = "ln(x)"
    # Llamado de la funcion
    print("######################################################")
    print("Metodo de la Regla de Simpson \n")
    xAprox, error = simpson(funcion, a, b)
    print('xAprox = {}\n%Error = {}'.format(xAprox, error))
