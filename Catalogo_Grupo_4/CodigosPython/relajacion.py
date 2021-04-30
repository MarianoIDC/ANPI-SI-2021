import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


def relajacion(A,b,maxI,tol,w):
    (P,L,U) = la.lu(A)
    D= np.diag(np.diag(U))
    k=0
    lista_error=[]
    x = []
    for i in A:
        x.append(0)
    x= np.transpose(x)
    while k<maxI:
        x0 = np.transpose(x)
        M= w**-1*(w*L+D)
        
        N = w**-1*((1-w)*D-w*U)
        
        x = np.matmul(np.matmul(np.linalg.inv(M),N),x0) + np.matmul(np.linalg.inv(M),b)
      
        errorM = b - np.matmul(A,np.transpose(x))
    
        errorM = np.transpose(errorM)
       
        error = 0
        print(x)
        for i in errorM:
            error = error+i**2
        lista_error.append(error)
        if (error**0.5 < tol):
            break
        k=k+1
    
    plt.plot(lista_error, label = 'errores por interacion') #Construccion de tabla
    plt.ylabel('Error')
    plt.xlabel('Iteracion')
    #Los ejes estan limitados por las iteraciones y el error maximo
    plt.axis([0, maxI, 0, lista_error[0]])
    plt.title('Relajacion')
    plt.legend()
    plt.show()
    return x,error
    

