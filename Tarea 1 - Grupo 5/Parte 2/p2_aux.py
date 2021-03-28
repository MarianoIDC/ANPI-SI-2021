import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con los valores ingresados
def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Grafica de Iteracion vs Error")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()
