import math
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
    jacobiano = np.zeros((func.size, var.size), dtype = object) #Crea la matriz jacobiana de la solución
    for i in range(func.size): #Itera sobre las filas de la matriz jacobiana
        func[i] = sympify(func[i])
        for j in range(var.size): #Itera sobre las columnas de la matriz jacobiana
            jacobiano[i][j] = diff(func[i], var[j]).subs(Symbol(var[j]), val[j]) #Realiza la derivada parcial y sustituye
    return jacobiano

x = np.array(['x', 'y', 'z'], dtype = object)
fx = np.array(['x**2+y**2+z**2-1', '2*x**2+y**2-4*z', '3*x**2-4*y+z**2'], dtype = object)
valores = np.array([1, -2, 3], dtype = object)
jacobo = jacobiano(fx, x, valores)

        
    
