from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
from sympy import sympify, Symbol, diff

#Cálculo del Jacobiano
#Entradas:
    #func: string con la funcion a evaluar
    #var: lista con las variables de la ecuación
    #val: lista con los valores de la ecuación
# Salidas:
    #jacobiano: matriz jacobiana de la solución
def jacobiano(func, var, val):
    jacobiano = np.zeros((func.size, var.size), dtype = float) #Crea la matriz jacobiana de la solución
    for i in range(func.size): #Itera sobre las filas de la matriz jacobiana
        func[i] = sympify(func[i])
        for j in range(var.size): #Itera sobre las columnas de la matriz jacobiana
            jacobiano[i][j] = diff(func[i], var[j]).subs(Symbol(var[j]), val[j]) #Realiza la derivada parcial y sustituye
    return jacobiano

#Simétrica Positiva Definida
##Entradas:
###A: Matriz a evaluar
##Salidas:
###Verdadero o falso
def es_pos_def(A):
    #Esta comparación garantiza que la matriz es simétrica mediante el método array_equal
    if np.array_equal(A, np.transpose(A)):
        #El método linalg.eigvals(matriz) es un método propio de Numpy que escoge los valores propios de la matriz, en este caso revisa que todos sean positivos
        #Si un valor propio de una matriz es positivo, entonces esta cumple que es positiva definida
        return np.all(np.linalg.eigvals(A) > 0)
    else:
        return False

#Factorización de Cholesky
##Entradas:
###A: Matriz a factorizar
###n: Tamaño de la matriz
###L: Matriz realizada
def fact_cholesky(A, n):
    L = np.zeros(shape = (A.shape[0], A.shape[1]), dtype = object)
    for i in range(n):
        for j in range(i + 1):
            suma = 0
            if (j == i):
                for k in range(j):
                    suma += L[j][k]**2
                print(suma)
                L[j][j] = sqrt(A[j][j] - suma)
            else:
                for k in range(j):
                    suma += L[j][k]*L[i][k]
                L[i][j] = (A[j][j] - suma)/L[i][i]
    return L

#Sustitución hacia atrás
##Entradas:
###L: Matriz a factorizar
###d: Tamaño de la matriz
##Salidas
###y: Sustitución de las ecuaciones
def sust_atras(L, b):
    #Se escoge el tamaño de la matriz
    N = L.shape[0]
    #Se genera una matriz vacía 
    y = np.zeros(N, dtype = float)
    for i in range(N - 1, -1, -1):
        suma = 0
        for j in range(i, N):
            suma += L[i, j] * y[j]
        y[i] = (b[i] - suma)/L[i, i]
    return y

#Sustitución hacia adelante
##Entradas:
###L: Matriz a factorizar
###d: Tamaño de la matriz
###L: Sustitución de las ecuaciones
##Salidas:
###x: Sustitución de las ecuaciones
def sust_adelante(L, b):
    #Se escoge el tamaño de la matriz
    N = L.shape[0]
    #Se genera una matriz vacía
    x = np.zeros(N, dtype = float)
    #Se realiza la sustitución hacia adelante
    for i in range(N):
        suma = 0
        for j in range(0, i):
            #Se debe realizar una sumatoria con los siguientes valores como se vio en clases
            suma += L[i, j] * x[j]
        #Se utiliza la fórmula como se vio en clases
        x[i] = (b[i] - suma)/L[i, i]
    return x

#Método de factorización de Cholesky
##Entradas:
###A: Matriz a factorizar
###d: Vector a comparar
###L: Sustitución de las ecuaciones
def cholesky(A, b):
    #Se escoge el tamaño de la matriz
    N = A.shape[0]
    #Se verifica que la matriz es SPD
    if(es_pos_def(A) == False):
        A = A * np.transpose(A)
        b = b * np.transpose(A)
    else:
        pass
    #Se generan las matrices vacías necesarias
    L = np.zeros(shape = (L.shape[0], L.shape[1]), dtype = float)
    y = np.zeros(shape = (L.shape[0], L.shape[1]), dtype = float)
    x = np.zeros(shape = (L.shape[0], L.shape[1]), dtype = float)
    #Se utilizan las funciones previamente creadas para realizar el método de Cholesky
    L = fact_cholesky(A, N)
    y = sust_atras(L, b)
    x = sust_adelante(np.transpose(L), y)
    return x

def fact_lu(A, b):
    if(np.linalg.det(A) == 0):
        print("La matriz no es singular")
        return
    else:
        pass
    n = A.shape[0]
    L = np.eye(n)
    U = A
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
    print(L)
    print(U)
    y = sust_adelante(L, b)
    print(y)
    x = sust_atras(U, y)
    return x

x = np.array(['x', 'y', 'z'], dtype = object)
fx = np.array(['x**2+y**2+z**2-1', '2*x**2+y**2-4*z', '3*x**2-4*y+z**2'], dtype = object)
valores = np.array([1/2, 1/2, 1/2], dtype = float)
jacobo = jacobiano(fx, x, valores)
print(jacobo)
valFunc = np.array([-1/4, -5/4, -1], dtype = float)
y = fact_lu(jacobo, valFunc)
print(y)


        
    
