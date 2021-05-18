import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
from sympy import sympify, Symbol, diff

# Cálculo del Jacobiano
# Entradas:
# func: string con la funcion a evaluar
# var: lista con las variables de la ecuación
# val: lista con los valores de la ecuación
# Salidas:
# jacobiano: matriz jacobiana de la solución


def jacobiano(func, var, val):
    # Crea la matriz jacobiana de la solución
    jacobiano = np.zeros((func.size, var.size), dtype=float)
    replace = []
    for i in range(func.size):  # Itera sobre las filas de la matriz jacobiana
        for j in range(var.size):  # Itera sobre las columnas de la matriz jacobiana
            for k in range(var.size):
                replace += [[var[k], val[k]]]
            jacobiano[i][j] = diff(func[i], var[j]).subs(
                replace)  # Realiza la derivada parcial y sustituye
    return jacobiano

# Gráfica
# Entradas:
    # listaValoresX: valores que se graficarán en el eje 'x'
    # listaValoresY: valores que se graficarán en el eje 'y'
# Salidas:
    # Gráfico con los valores ingresados


def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'r-')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

# Método de Newton-Raphson
# Entradas:
    # f: es el vector de funciones a analizar
    # x: es el vector de variables en las funciones
    # x0: valor inicial
    # iterMax: es la cantidad de iteraciones maximas a realizar
    # tol: es la tolerancia del algoritmo
# Salidas:
    # xk: es la solucion, valor aproximado del vector x
    # error: vector de pocentaje de error de los resultados obtenidos
    # k: cantidad de iteraciones sobre las que se realizaron el método


def newton_raphson(x, f, x0, tol, iterMax):
    # Se definen las variables del método
    itera = 1
    error = 1
    listaIter = []
    listaError = []
    xk = x0
    # Es el vector del valor numérico del vector f(x)
    valores = np.zeros(x.size, dtype=float)
    # Es un vector que permite reemplazar todas las variables de la función por su valor numérico
    replace = []
    while(itera < iterMax):
        xAprox = xk
        for i in range(x.size):
            for k in range(x.size):
                replace += [[x[k], xAprox[k]]]  # Se toma el vector
            f[i] = sympify(f[i])  # La función se convierte en simbólica
            # Se llena el vector del valor numérico de f(x)
            valores[i] = f[i].subs(replace)
        # Se debe reiniciar el vector de las variables para la siguiente iteración
        replace = []
        # Se calcula el jacobiano
        jacobo = jacobiano(f, x, xAprox)
        # Se realiza la iteración y el error
        xk = xAprox - np.linalg.solve(jacobo, valores) # Es una función de Numpy que calcula sistemas de ecuaciones
        error = np.linalg.norm(valores)
        listaIter.append(itera)
        listaError.append(error)
        if (error < tol):
            return xk, itera, error, listaIter, listaError
        else:
            itera += 1
    # Se retorna la aproximación de la solución, el número de iteraciones, el error y las listas de la gráfica
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
