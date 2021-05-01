# Metodo de la Factorizacion LU
    # Entradas:
        # matrizD: matriz de coeficientes
        # matrizI: matriz de terminos independientes
    # Salidas:
        # X: solucion del sistema

###############################################################################
import numpy as np
import scipy.linalg as la
###############################################################################

def fact_lu(matrizD, matrizI):
    if(np.linalg.det(matrizD) == 0):
        print("La matriz no es singular")
        return
    else:
        pass
    n = len(matrizD)
    L = np.eye(n)
    U = matrizD

    for i in range(1, n):
        pivot = U[i - 1][i - 1]
        pivotRow = U[i - 1]
        M = np.zeros((1, n - i))
        m = M.size + 1

        for k in range(1, m):
            try:
                M[i - 1][k - 1] = (U[i + k - 1][i - 1]) / pivot
            except:
                M = (U[i + k - 1][i - 1]) / pivot

        for k in range(1, m):
            try:
                U[i + k - 1] = U[i + k - 1] - (np.multiply(pivotRow, M[i - 1][k - 1]))
                L[i + k - 1][i - 1] = M[i - 1][k - 1]
            except:
                U[i + k - 1] = U[i + k - 1] - (np.multiply(pivotRow, M))
                L[i + k - 1][i - 1] = M

    Y = ((np.linalg.inv(L)).dot(np.transpose(matrizI)))
    X = (np.linalg.inv(U)).dot(Y)
    return X

if __name__ == '__main__':
    # Matriz de coeficientes
    A = [[4, -2, 1], [20, -7, 12], [-8, 13, 17]]
    # Vector de terminos independientes
    B = [11, 70, 17]
    # Llamado de la funcion
    X = fact_lu(A, B)
    print("######################################################")
    print("Metodo de la Factorizacion LU\n")
    print('X = {}\n'.format(X))
