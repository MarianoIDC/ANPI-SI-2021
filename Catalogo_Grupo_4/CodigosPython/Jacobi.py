###############################################################################
import numpy as np
###############################################################################
def jacobi(A, b, x0, tol):
    '''
    Metodo de Jacobi
    :param A: matriz de coeficientes
    :param b: vector de terminos independientes
    :param x0: vector de valores iniciales
    :param tol: tolerancia de la respuesta
    :return: x: vector solucion
    '''
    n = len(A)
    A = np.array(A)
    b = np.array(b)
    L = np.zeros((n, n))
    D = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]
            else:
                D[i][j] = A[i][j]

    x = np.array(x0)
    error = np.linalg.norm(np.dot(A, x) - b)
    i = 0
    m_inv = np.linalg.inv(D)
    m_times_n = np.dot(m_inv, (-1 * (L + U)))
    m_times_b = np.dot(m_inv, b)

    while error >= tol:
        x = np.dot(m_times_n, x) + m_times_b
        error = np.linalg.norm(np.dot(A, x) - b)
        i += 1

    return x