###############################################################################
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
###############################################################################


def relajacion(A, b, maxI, tol, w):
    '''
    Metodo de Relajacion
    :param A: matriz de cofactores
    :param b: matriz de respuestas
    :param maxI: maxima cantidad de iteraciones
    :param tol: tolerancia para calcular error
    :param w: constante por usar en el metodo
    :return:
    '''
    # Se debe verificar que la matriz sea definida positiva
    if (np.all(np.linalg.eigvals(A) > 0)):
        pass
    else:
        print("La matriz no es definida positiva")
        return
    # Se debe verificar que la matriz sea tridiagonal
    for i in range(len(A)):
        for j in range(len(A[0])):
            i0 = j - 1
            i1 = j + 1
            if (i == j):
                if i0 < 0 or i0 >= len(A[0]):
                    if A[i][j] == 0 or A[i1][j] == 0:
                        print(1)
                        print("La matriz no es tridiagonal")
                        return
                elif i1 < 0 or i1 >= len(A[0]):
                    if A[i][j] == 0 or A[i0][j] == 0:
                        print(2)
                        print("La matriz no es tridiagonal")
                        return
                else:
                    if A[i][j] == 0 or A[i0][j] == 0 or A[i1][j] == 0:
                        print(3)
                        print("La matriz no es tridiagonal")
                        return
            else:
                if abs(i - j) > 1:
                    if A[i][j] != 0:
                        print(i)
                        print(j)
                        print("La matriz no es tridiagonal")
                        return

    # Calculo de D, L y U
    (P, L, U) = la.lu(A)
    D = np.diag(np.diag(U))
    # k es la iteracion actual
    k = 0
    # Un requisito es que la matriz D+wL sea invertible
    x = D + w * L
    try:
        inverse = np.linalg.inv(x)
    except np.linalg.LinAlgError:
        print("D+wL no es invertible")
        return
    else:
        # lista de errores para graficar
        lista_error = []
        x = []
        for i in A:
            x.append(0)
        x = np.transpose(x)
        # iteraciones, esperando que se cumplan las iteraciones
        while k < maxI:
            x0 = np.transpose(x)
            M = w ** -1 * (w * L + D)
            N = w ** -1 * ((1 - w) * D - w * U)
            x = np.matmul(np.matmul(np.linalg.inv(M), N), x0) + \
                np.matmul(np.linalg.inv(M), b)
            errorM = b - np.matmul(A, np.transpose(x))
            errorM = np.transpose(errorM)
            error = 0
            # Revisar si el error se cumple, sino se sigue iterando
            for i in errorM:
                error = error + i ** 2
            lista_error.append(error ** 0.5)
            if (error ** 0.5 < tol):
                break
            k = k + 1

        # Construccion de tabla
        plt.plot(lista_error, label='errores por interacion')
        plt.ylabel('Error')
        plt.xlabel('Iteracion')
        # Los ejes estan limitados por las iteraciones y el error maximo
        plt.axis([0, maxI, 0, max(lista_error)])
        plt.title('Relajacion')
        plt.legend()
        plt.show()
        print('x: ' + str(x) + ', error: ' + str(error))
        return x, error


if __name__ == '__main__':
    # Constante w
    w = 1.24
    # Maximo iteraciones
    MAXIT = 5
    # Tolerancia
    TOL = 0.0001
    # Matriz de cofactores
    A = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]
    # Vector de respuestas
    b = [7, 7, 7]
    # Llamado de la funcion
    print("######################################################")
    print("Metodo del Punto Fijo \n")
    relajacion(A, b, MAXIT, TOL, w)
