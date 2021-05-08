import numpy as np
## Problema: Recubrimiento de Conductores Electricos
## Pagina 353 Problema 4.6
## Nieves H. A, Dominguez S. F. (2014), Metodos Numericos Aplicados a la Ingenieria 4a Edicion. Universidad Iberoamericana
## Grupo Editorial Patria, D.F., Mexico. 

from parte2_p2 import *

"""
Para el recubrimiento de conductores eléctricos se utiliza una mezcla plástica viscosa,
cuya preparación se lleva a cabo en mezcladores que trabajan por lotes.
De datos experimentales y su correlación se tiene que el tiempo de residencia en el mezclador puede aproximarse por

t = 14800*(sqr(S)/P)

donde 

t = tiempo del proceso hr/lote
S = Capacidad útil del mezclador Kg/lote
P = potencia del agitador KW

Adicionalmente se sabe que 
CE = costo de la electricidad: 0.43 $/KW hr
CM = costo del mezclador: 9500*sqr(S) S/anio
CI = costos indirectos 810*P $/anio

Produccion necesaria 500 000 Kg/anio

Calcule la capacidad optima del mezclador S*, la potencia optima del agitador P* y el costo total del proceso CT

                CT = CE + CM + CI

donde CE = 0.43*P*t*N [$/anio]

con N como el numero de lotes por anio y dado por 

                N = 5000 000/S [lote/anio]

por lo que      CE = 3.182*10exp(9) / (P*sqr(S)) [$/anio]

por lo tanto    CT =  3.182*10exp(9) / (P*sqr(S)) + 9500*sqr(S) + 810*P


Derindo parcialmente a CT con respecto a P y S se obtiene

        CTP = ((3.182*10exp(9))/((P**2)*sqr(S)))+810

        CTS = ((1.519*10exp(9))/((P*S)*sqr(S)))+(4750/sqr(S))


"""

x = np.array(['x1','x2','x3'], dtype = object)
x0 = np.array([0.7,0.2,0.1], dtype = float)
f = np.array([
    '((x1+x2)(x1-x3))-(5.97*(1-x1-x2)*(1+x1+x2))',
    '((x2+x3)*x2)-(0.27*(1+x1+x2)*(1+x1+x2))',
    '((x1+x3)*x3)-(2.8*(x1-x3)*(x2-x3))'
    ], 
    dtype = object)
tol = 0.0001
iterMax = 10
print("Método de Newton-Raphson para el problema ingenieril \n")
xAprox, k, err, iter1, err1 = newton_raphson(x, f, x0, tol, iterMax)
print('xAprox = {}\n%Error = {}\n%Iteraciones = {}'.format(xAprox, err, k))
grafica(iter1, err1)

