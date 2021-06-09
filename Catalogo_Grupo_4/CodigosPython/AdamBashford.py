import sympy as sym
import matplotlib.pyplot as plt
'''
Adam bashford
a 4 pasos
@ param funcion: f(x,y)=dx/dy
@ param intervalo: lista de dos números, rango de estudio
@ param paso_h: entero, cantidad de puntos por usar
@ param y0: Valor de y0
@ return: lista de tuplas de la forma {xk,yk}

'''
def adam_bashford_4(funcion,intervalo,paso_h,y0):
    x = sym.symbols('x')
    y = sym.symbols('y')
    f = sym.sympify(funcion) 
    h = (intervalo[1]-intervalo[0])/(paso_h-1)
    xn=[]
    k=0
    while k<paso_h:
        x_temp= intervalo[0]+k*h
        xn.append(x_temp)
        k=k+1
    yk=[y0]
    k=0
    while k<3:
        yn1= yk[k]+h+f.subs({x:xn[k],y:yk[k]})
        yk.append(yn1)
        k=k+1
    
    k=3
    while k<paso_h-1:
        yk1 = yk[k]+h/24 *(55* f.subs({x:xn[k],y:yk[k]})-59*f.subs({x:xn[k-1],y:yk[k-1]})+
                           37*f.subs({x:xn[k-2],y:yk[k-2]})-9*f.subs({x:xn[k-3],y:yk[k-3]}))
        yk.append(yk1)
        k=k+1
    print(xn)
    print(yk)
    plt.ylabel('yk')
    plt.xlabel('xk')
    plt.plot(xn, yk)
    plt.show()
    pares_ordenados = []
    for i in range(len(xn)):
        temp = {xn[i],yk[i]}
        pares_ordenados.append(temp)
    return temp

if __name__ == '__main__':
    
    intervalo = [1,5]
    funcion = 'x**2  - (1 / y)'
    paso = 10
    y0=1
    adam_bashford_4(funcion,intervalo,paso,y0)
    
