import numpy as np
## Problema: Columna de Absorcion de 5 Platos, con el gas especifico de Touleno
## Pagina 356 Problema 4.8
## Nieves H. A, Dominguez S. F. (2014), Metodos Numericos Aplicados a la Ingenieria 4a Edicion. Universidad Iberoamericana
## Grupo Editorial Patria, D.F., Mexico. 


from parte2_p2 import *
#Corriente de Gas, Moles de Gas sin Tolueno
#V0 = 39.6 #moles/min

#Corriente de Gas con aceite
#L0 = 6.0 #moles/min

#Los moles de tolueno/min que entran a la columna de gas y el aceite son respecivamente
#TV0 = 5.4 #moles/min
#LT0 = 0.0 #moles/min
#m = 0.155

#Fraccion de mol tolueno
#y0 = 0.12
#x0 = 0.77

#Funciones Auxiliares
#yi = (TVi) / (TVi + V0)
#TVi = (V0*mi*xi)/(1-m*xi)
#Tli = (L0*xi)/(1-xi)

#Sistema de ecuaciones no linea

## 'V0*y0 + ((V0*(y0**2))/(1-y0)) - (V0*m*x1) - ((V0*(m**2)*(x1**2))/(1-m*x1)) + (L0*x2) + ((L0*(x2**2))/(1-x2)) - (L0*x1) - ((L0*(x1**2))/(1-x1))', 
## 'V0*m*x1 + ((V0*(m**2)*(x1**2))/(1-m*x1)) - (V0*m*x2) - ((V0*(m**2)*(x2**2))/(1-m*x2)) + (L0*x3) + ((L0*(x3**2))/(1-x3)) - (L0*x2) - ((L0*(x2**2))/(1-x2))', 
## 'V0*m*x2 + ((V0*(m**2)*(x2**2))/(1-m*x2)) - (V0*m*x3) - ((V0*(m**2)*(x2**2))/(1-m*x3)) + (L0*x4) + ((L0*(x4**2))/(1-x4)) - (L0*x3) - ((L0*(x3**2))/(1-x3))',
## 'V0*m*x3 + ((V0*(m**2)*(x3**2))/(1-m*x3)) - (V0*m*x4) - ((V0*(m**2)*(x2**2))/(1-m*x4)) + (L0*x5) + ((L0*(x5**2))/(1-x5)) - (L0*x4) - ((L0*(x4**2))/(1-x4))',
## 'V0*m*x4 + ((V0*(m**2)*(x4**2))/(1-m*x4)) - (V0*m*x5) - ((V0*(m**2)*(x2**2))/(1-m*x5)) + (L0*x0) + ((L0*(x0**2))/(1-x0)) - (L0*x5) - ((L0*(x5**2))/(1-x5))'

x = np.array(['x1','x2','x3','x4','x5'], dtype = object)
x0 = np.array([0.4,0.3,0.2,0.1,0.05], dtype = float)
f = np.array([
    '39.6*0.12     + ((39.6*(0.12**2))/(1-0.12))         - (39.6*0.155*x1) - ((39.6*(0.155**2)*(x1**2))/(1-0.155*x1)) + (6.0*x2) + ((6.0*(x2**2))/(1-x2)) - (6.0*x1) - ((6.0*(x1**2))/(1-x1))', 
    '39.6*0.155*x1 + ((39.6*(0.155**2)*(x1**2))/(1-0.155*x1)) - (39.6*0.155*x2) - ((39.6*(0.155**2)*(x2**2))/(1-0.155*x2)) + (6.0*x3) + ((6.0*(x3**2))/(1-x3)) - (6.0*x2) - ((6.0*(x2**2))/(1-x2))', 
    '39.6*0.155*x2 + ((39.6*(0.155**2)*(x2**2))/(1-0.155*x2)) - (39.6*0.155*x3) - ((39.6*(0.155**2)*(x3**2))/(1-0.155*x3)) + (6.0*x4) + ((6.0*(x4**2))/(1-x4)) - (6.0*x3) - ((6.0*(x3**2))/(1-x3))',
    '39.6*0.155*x3 + ((39.6*(0.155**2)*(x3**2))/(1-0.155*x3)) - (39.6*0.155*x4) - ((39.6*(0.155**2)*(x4**2))/(1-0.155*x4)) + (6.0*x5) + ((6.0*(x5**2))/(1-x5)) - (6.0*x4) - ((6.0*(x4**2))/(1-x4))',
    '39.6*0.155*x4 + ((39.6*(0.155**2)*(x4**2))/(1-0.155*x4)) - (39.6*0.155*x5) - ((39.6*(0.155**2)*(x5**2))/(1-0.155*x5)) + (6.0*0.77) + ((6.0*(0.77**2))/(1-0.77)) - (6.0*x5) - ((6.0*(x5**2))/(1-x5))'], 
    dtype = object)
tol = 0.00001
iterMax = 10
print("Método de Newton-Raphson para el problema ingenieril \n")
xAprox, k, err, iter1, err1 = newton_raphson(x, f, x0, tol, iterMax)
print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
grafica(iter1, err1)

