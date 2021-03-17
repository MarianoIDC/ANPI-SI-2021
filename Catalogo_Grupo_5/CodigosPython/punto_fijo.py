import matplotlib.pyplot as plt
import numpy as np

#Punto Fijo
#Entradas: funcion - Funcion por aproximar - funcion lambda
#          valor_inicial - Valor por el cual se empezará a aproximar - int, float, double
#          iteraciones_maximas - Número máximo de itreaciones - int
#
#

def punto_fijo(funcion,valor_inicial,iteraciones_maximas):
    lista_error = [] #lista para graficar 
    iteracion = 1 
    b = funcion(valor_inicial)  #valor para obtener error
    error = abs(b-valor_inicial)
    while(iteracion<=iteraciones_maximas ):  #condicion de parada
        valor_inicial = b                    #reajuste de valores de error
        b = funcion(valor_inicial)
        error = abs(b-valor_inicial)
        lista_error.append(error)
        iteracion += 1
    
    aproximacion = b
    plt.plot(lista_error, label='errores por interación')    #Construcción de tabla
    plt.ylabel('Error')
    plt.xlabel('Iteracion')
    
    plt.axis([0, iteraciones_maximas,0,lista_error[0]])      #Los ejes estan limitados por las iteraciones y el error máximo
    plt.title('Punto Fijo')
    plt.legend()
    plt.show()
    print ('Aproximación: '+ str(aproximacion)+ ', error: '+ str(error))
    return aproximacion, error

funcion =lambda x: np.exp(-x) 
punto_fijo(funcion, 0, 15)
