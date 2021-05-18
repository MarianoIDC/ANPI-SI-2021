import numpy as np
from parte2_p2 import *

#Se establecen las 4 incógnitas escogidas para el problema ingenieril, las cuáles son los ángulos Theta del canal de flujo
x = np.array(['x1', 'x2', 'x3', 'x4'], dtype=object)
#Valores iniciales propuestos para el canal de flujo
x0 = np.array([1, -1, 1, -1], dtype=float)
#El vector de funciones es un vector de distintas funciones seno, las cuales evalúan cada uno de los Theta divididos entre un valor específico
#Se incluye un valor tangente como cuarta función definido matemáticamente antes
f = np.array([
    '((sin(x2))/(5.08))-((sin(x1))/(3.59))',
    '((sin(x3))/(6.22))-((sin(x2))/(5.08))',
    '((sin(x4))/(7.18))-((sin(x3))/(6.22))',
    '(0.2*(tan(x1)+tan(x2)+tan(x3)+tan(x4))-2)'
],
    dtype=object)

#Se establece la tolerancia dada para el problema
tol = 0.0001
#Se establecen las iteraciones máximas
iterMax = 10
#Se ejecuta el método de Newton-Raphson sobre el problema ingenieril
print("Método de Newton-Raphson para el problema ingenieril \n")
xAprox, k, err, iter1, err1 = newton_raphson(x, f, x0, tol, iterMax)
print('xAprox = {}\nError = {}\nIteraciones = {}'.format(xAprox, err, k))
#Se realiza la gráfica de iteraciones vs error
grafica(iter1, err1)
