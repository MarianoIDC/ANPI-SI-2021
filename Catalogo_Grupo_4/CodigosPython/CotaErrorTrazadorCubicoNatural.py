###############################################################################
import numpy as np
import sympy as sym
###############################################################################


def cota_tras_cubico(func, S):
    '''
    Metodo de Cota de Error del Trazador Cubico
    :param func: funcion con al menos 4ta derivada
    :param S: Lista de puntos
    :return: cota_error: Cota de error
    '''
    h = 0
    x = sym.symbols('x')
    f = sym.sympify(func)     # La funcion se castea en x
    f4 = sym.diff(f, x, 4)      # La 4ta derivada
    norm = 0
    for i in range(len(S)):           # Norma infinira
        if (f4.subs(x, S[i]) > norm):
            norm = f4.subs(x, S[i])
        else:
            pass

    for i in range(len(S) - 1):  # Valor h
        if (S[i+1] - S[i] > h):
            h = S[i+1] - S[i]
        else:
            pass
    cota_error = 5*h**4 * norm / 384    # Valor cota
    return float(cota_error)


if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6]
    func = 'x**4  - (1 / x)'
    cota_error = cota_tras_cubico(func, S)
    print("######################################################")
    print("Metodo de Cota de Error del Trazador Cubico\n")
    print('Cota de error = {}\n'.format(cota_error))
