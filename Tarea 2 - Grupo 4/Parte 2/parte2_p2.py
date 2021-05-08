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
    replace = []
    for i in range(func.size): #Itera sobre las filas de la matriz jacobiana
        for j in range(var.size):#Itera sobre las columnas de la matriz jacobiana
            for k in range(var.size):
                replace += [[var[k], val[k]]]
            jacobiano[i][j] = diff(func[i], var[j]).subs(replace) #Realiza la derivada parcial y sustituye
    return jacobiano

#Gráfica
#Entradas:
    #listaValoresX: valores que se graficarán en el eje 'x'
    #listaValoresY: valores que se graficarán en el eje 'y'
#Salidas:
    #Gráfico con los valores ingresados
def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

#Sustitución hacia atrás
#Entradas:
    #L: Matriz a factorizar
    #d: Tamaño de la matriz
#Salidas
    #y: Sustitución de las ecuaciones
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
#Entradas:
    #L: Matriz a factorizar
    #d: Tamaño de la matriz
#Salidas:
    #x: Sustitución de las ecuaciones
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

#Método de factorización LU
#Entradas:
    #A: Matriz a factorizar
    #d: Vector a comparar
#Salida:
    #x: Sustitución de las ecuaciones
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
    y = sust_adelante(L, b)
    x = sust_atras(U, y)
    return x

# Método de Newton-Raphson
# Entradas:
    #f: es el vector de funciones a analizar
    #x: es el vector de variables en las funciones
    #x0: valor inicial
    #iterMax: es la cantidad de iteraciones maximas a realizar
    #tol: es la tolerancia del algoritmo
# Salidas:
    #xk: es la solucion, valor aproximado del vector x
    #error: vector de pocentaje de error de los resultados obtenidos
    #k: cantidad de iteraciones sobre las que se realizaron el método
def newton_raphson(x, f, x0, tol, iterMax):
    #Se definen las variables del método
    itera = 1
    error = 1
    listaIter = []
    listaError = []
    xk = x0
    #Es el vector del valor numérico del vector f(x)
    valores = np.zeros(x.size, dtype = float)
    #Es un vector que permite reemplazar todas las variables de la función por su valor numérico
    replace = []
    while(itera < iterMax):
        xAprox = xk
        for i in range(x.size):
            for k in range(x.size):
                replace += [[x[k], xAprox[k]]] #Se toma el vector 
            f[i] = sympify(f[i]) #La función se convierte en simbólica
            valores[i] = f[i].subs(replace) #Se llena el vector del valor numérico de f(x)
        #Se debe reiniciar el vector de las variables para la siguiente iteración
        replace = []
        #Se calcula el jacobiano
        jacobo = jacobiano(f, x, xAprox)
        #Se realiza la iteración y el error
        xk = xAprox - fact_lu(jacobo, valores) #Es una función de Numpy que calcula sistemas de ecuaciones
        error = np.linalg.norm(valores)
        listaIter.append(itera)
        listaError.append(error)
        if (error < tol):
            return xk, itera, error, listaIter, listaError 
        else:
            itera += 1
    #Se retorna la aproximación de la solución, el número de iteraciones, el error y las listas de la gráfica
    return xk, itera, error, listaIter, listaError
        
##x = np.array(['x', 'y', 'z'], dtype = object)
##f = np.array(['x**2+y**2+z**2-1', '2*x**2+y**2-4*z', '3*x**2-4*y+z**2'], dtype = object)
##x0 = np.array([1/2, 1/2, 1/2], dtype = float)
##tol = 0.00001
##iterMax = 10
##print("Método de Newton-Raphson \n")
##xAprox, k, err, iter1, err1 = newton_raphson(x, f, x0, tol, iterMax)
##print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
##grafica(iter1, err1)
