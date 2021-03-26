import p2_metodo_nuevo as p1
import parte2_p2 as p2
import matplotlib.pyplot as plt

#Grafica
#Entradas:
            #listaValoresX: valores que se graficaran en el eje 'x'
            #listaValoresY: valores que se graficaran en el eje 'y'
#Salidas:
            #Grafico con los valores ingresados
def grafica(listaValoresX, listaValoresY):
    plt.plot(listaValoresX, listaValoresY, 'bx')
    plt.title("Metodo de Newton-Raphson")
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.show()

if __name__ == '__main__':
    #Intervalos
    a = 0
    b = 2
    #Tolerancia
    tol = 0.0001
    #Maximo iteraciones
    iterMax = 100
    #Funcion
    f = lambda x: p2.math.e**x - x - 2
    #Llamado de la funcion
    xk, k, err, iteraciones, errores = p2.falsa_posicion(f, a, b, iterMax, tol)
    print("Metodo de la Falsa Posicion \n")
    print('xk = {}\nk = {}\nerror = {}'.format(xk, k, err))
    print("################################################")
    grafica(iteraciones, errores)
