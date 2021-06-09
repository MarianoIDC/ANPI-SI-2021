###############################################################################
import sympy as sym
###############################################################################


def simpson_compuesto(funcion, numero_puntos, intervalo):
    '''
    Metodo de Simpson Compuesto para calculo de integrales    
    :param funcion: funcion con al menos 4ta deriva 
    :param numero_puntos: Cantidad de puntos a utilizar 
    :param intervalo: lista con valor inicial a final que define 
    los limites de la integral 
    :return: integral, error: Resultado de integral y error 
    '''
    x = sym.symbols('x')
    f = sym.sympify(funcion)
    suma_pares = 0
    suma_impares = 0
    x0 = intervalo[0]
    h = (intervalo[1]-intervalo[0])/(numero_puntos-1)
    lista_x = []
    lista_x.append(x0)
    k = 1
    while k <= numero_puntos:
        temp = x0+k*h
        lista_x.append(temp)
        k = k+1
    for i in range(len(lista_x)-1):
        if i == 0:
            pass
        else:
            if i % 2 == 0:
                suma_pares = suma_pares+f.subs(x, i)
            else:
                suma_impares = suma_impares+f.subs(x, i)
    integral = h/3 * \
        (f.subs(x, lista_x[0])+2*suma_pares +
         4*suma_impares+f.subs(x, lista_x[-1]))
    integral = float(integral)
    f4 = sym.diff(f, x, 4)
    error = (intervalo[1]-intervalo[0])/180 * abs(f4.subs(x, intervalo[0]))
    print("La integral da como resultado " +
          str(integral)+" con un error de "+str(error))
    return integral, error


if __name__ == '__main__':
    funcion = 'ln(x)'
    # Llamado de la funcion
    print("######################################################")
    print("Metodo de Simpson Compuesto y Cota de Error \n")
    simpson_compuesto(funcion, 7, [2, 5])
