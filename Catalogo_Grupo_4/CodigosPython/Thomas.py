########################################################################################
import numpy as np
########################################################################################


def thomas(matrizC, vectorTI):
    '''
    Metodo de Thomas
    :param matrizC: matriz de coeficientes
    :param vectorTI: matriz de terminos independientes
    :return: X: solucion del sistema
    '''
    A = matrizC
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (i == j and (matrizC[i][j] == 0)):
                print("La matriz no es tridiagonal 1")
                return
            elif (j == (i + 1) and matrizC[i][j] == 0):
                print("La matriz no es tridiagonal 2")
                return
            elif (j == (i - 1) and matrizC[i][j] == 0):
                print("La matriz no es tridiagonal 3")
                return
            elif ((j > i + 1) and (matrizC[i][j] != 0)):
                print("La matriz no es tridiagonal 4")
                return
            elif (((j < i - 1) and (matrizC[i][j] != 0))):
                print("La matriz no es tridiagonal 5")
                return
    xn = []
    ci = 0
    di = 0
    qi = 0
    bi = 0
    pi = 0
    n = len(matrizC)
    if (len(matrizC) == len(vectorTI)):
        for i in range(0, n):
            if (i == 0):
                ci = matrizC[i][i + 1]
                bi = matrizC[i][i]
                di = vectorTI[i]
                pi = ci / bi
                qi = di / bi
                xn.append(qi)
            elif (i <= n - 2):
                ai = matrizC[i + 1][i]
                bi = matrizC[i][i]
                di = vectorTI[i]
                ci = matrizC[i][i + 1]
                pi = ci / (bi - pi * ai)
                qi = (di - qi * ai) / (bi - pi * ai)
                xn.append(qi - pi * xn[i - 1])
            else:
                ai = matrizC[i][i - 1]
                bi = matrizC[i][i]
                di = vectorTI[i]
                qi = (di - qi * ai) / (bi - pi * ai)
                xn.append(qi * xn[i - 1])
        return xn
    else:
        print("Error: el vector y la matriz deben ser del mismo tamano")


def creaTridiagonal(N, a, b, c):
    '''
    Funcion para crear la matriz tridiagonal
    :param N: tamano de la matriz
    :param a: valor debajo de la diagonal principal
    :param b: valor de la diagonal principal
    :param c: valor sobre la diagonal principal
    :return: matriz: matriz tridiagonal
    '''
    matriz = np.zeros((N, N))
    np.fill_diagonal(matriz, b)
    n = N
    for i in range(0, n - 1):
        matriz[i][i + 1] = c
        matriz[i + 1][i] = a
    return matriz


def creaD(N, ext, inte):
    '''
    Funcion para crear el vector d
    :param N: tamano del vector
    :param ext: valor en los extremos del vector
    :param inte: valor en el interior del vector
    :return: d: vector d
    '''
    n = N
    d = []
    for i in range(0, n):
        if ((i == 0) or (i == n - 2)):
            d.append(ext)
        else:
            d.append(inte)
    return d


if __name__ == '__main__':
    # Creacion de la matriz tridiagonal
    matrizC = creaTridiagonal(7, 1, 5, 1)
    # Creacion del vector D
    vectorTI = creaD(7, -12, -14)
    # Llamado del metodo
    print("######################################################")
    print("Metodo de Thomas\n")
    X = thomas(matrizC, vectorTI)
    print('X = {}\n'.format(X))
