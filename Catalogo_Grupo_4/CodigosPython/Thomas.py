# Metodo de Thomas
    # Entradas:
        # matrizC: matriz de coeficientes
        # matrizTI: matriz de terminos independientes
    # Salidas:
        # X: solucion del sistema

########################################################################################
import numpy as np
########################################################################################

def thomas(matrizC, vectorTI):
    A = matrizC
    for i in range(len(A)):
        for j in range(len(A[0])):
            i0= j-1
            i1= j+1
            if (i==j):
                if i0<0 or i0>=len(A[0]):
                    if A[i][j]<0 or A[i1][j]<0:
                        print(1)
                        print("La matriz no es tridiagonal")
                        return
                elif i1<0 or i1>=len(A[0]):
                    if A[i][j]<0 or A[i0][j]<0:
                        print(2)
                        print("La matriz no es tridiagonal")
                        return
                else:
                    if A[i][j]<0 or A[i0][j]<0 or A[i1][j]<0 :
                        print(3)
                        print("La matriz no es tridiagonal")
                        return
            else:
                if abs(i-j)>1:
                    if A[i][j]!=0:
                        print(i)
                        print(j)
                        print("La matriz no es tridiagonal")
                        return
    xn = []
    ci = 0
    di = 0
    qi = 0
    bi = 0
    pi = 0
    n = len(matrizC)

    if(len(matrizC) == len(vectorTI)):
        for i in range(0, n):
            if(i == 0):
                ci = matrizC[i+1][i]
                bi = matrizC[i][i]
                di = vectorTI[i]
                pi = ci/bi
                qi = di/bi
                xn.append(qi)
            elif(i < n-1):
                ai = matrizC[i][i+1]
                bi = matrizC[i][i]
                di = vectorTI[i]
                ci = matrizC[i+1][i]
                pi = ci/(bi-pi*ai)
                qi = (di-qi*ai)/(bi-pi*ai)
                xn.append(qi-pi*xn[i-1])
            else:
                ai = matrizC[i][i]
                bi = matrizC[i][i]
                ci = matrizC[i][i]
                di = vectorTI[i]
                pi = ci / (bi - pi * ai)
                qi = (di - qi * ai) / (bi - pi * ai)
                xn.append(qi - pi * xn[i - 1])
        return xn
    else:
        print("Error: el vector y la matriz deben ser del mismo tamano")

# Funcion para crear la matriz tridiagonal
    # Entradas:
        # N: tamano de la matriz
        # a: valor debajo de la diagonal principal
        # b: valor de la diagonal principal
        # c: valor sobre la diagonal principal
    # Salidas:
        # matriz: matriz tridiagonal
def creaTridiagonal(N, a, b, c):
    if (N % 2 != 0):
        print("El valor N debe ser un numero par")
    else:
        matriz = np.zeros((N,N))
        np.fill_diagonal(matriz, b)
        n = N
        print(matriz[0][5])
        for i in range(0,n-1):
            matriz[i][i + 1] = c
            matriz[i + 1][i] = a
        return matriz

# Funcion para crear el vector d
    # Entradas:
        # N: tamano de la matriz
        # ext: valor en los extremos del vector
        # inte: valor en el interior del vector
    # Salidas:
        # d: vector d
def creaD(N, ext, inte):
    if(N%2 != 0):
        print("El valor N debe ser un numero par")
    else:
        n = N
        d = []
        for i in range(0, n):
            if ((i == 0) or (i == n - 2)):
                d.append(ext)
            else:
                d.append(inte)
        return d

if __name__ == '__main__':
    #Creacion de la matriz tridiagonal
    matrizC = creaTridiagonal(10, 1, 5, 1)
    #Creacion del vector D
    vectorTI = creaD(10, -12, -14)
    #Llamado del metodo
    X = thomas(matrizC, vectorTI)
    print("######################################################")
    print("Metodo de Thomas\n")
    print('X = {}\n'.format(X))
