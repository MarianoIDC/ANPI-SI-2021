###############################################################################
import matplotlib.pyplot as plt
import numpy as np
###############################################################################

def punto_fijo(funcion, valor_inicial, iteraciones_maximas):
    '''
    Metodo del punto fijo
    :param funcion: Funcion por aproximar - funcion lambda
    :param valor_inicial: Valor por el cual se empezara a aproximar - int, float, double
    :param iteraciones_maximas: Numero maximo de itreaciones - int
    :return: aproximacion: aproximacion de la solucion
    '''
    lista_error = []  # lista para graficar
    iteracion = 1
    b = funcion(valor_inicial)  # valor para obtener error
    error = abs(b - valor_inicial)
    while (iteracion <= iteraciones_maximas):  # condicion de parada
        valor_inicial = b  # reajuste de valores de error
        b = funcion(valor_inicial)
        error = abs(b - valor_inicial)
        lista_error.append(error)
        iteracion += 1

    aproximacion = b
    plt.plot(lista_error, label='errores por interacion')  # Construccion de tabla
    plt.ylabel('Error')
    plt.xlabel('Iteracion')
    # Los ejes estan limitados por las iteraciones y el error maximo
    plt.axis([0, iteraciones_maximas, 0, lista_error[0]])
    plt.title('Punto Fijo')
    plt.legend()
    plt.show()
    print('Aproximacion: ' + str(aproximacion) + ', error: ' + str(error))
    return aproximacion, error

if __name__ == '__main__':
    #Valor inicial
    x0 = 0
    #Maximo iteraciones
    MAXIT = 100
    #Funcion
    funcion = lambda x: np.exp(-x)
    #Llamado de la funcion
    print("######################################################")
    print("Metodo del Punto Fijo \n")
    punto_fijo(funcion, x0, MAXIT)