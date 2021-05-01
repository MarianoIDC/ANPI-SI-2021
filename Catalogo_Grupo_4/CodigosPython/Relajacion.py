import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


def relajacion(A,b,maxI,tol,w):
    if (np.all(np.linalg.eigvals(A) > 0)):
        pass
    else:
        print("La matriz no es definida positiva")
        return
    for i in range(len(A)):
        for j in range(len(A[0])):
            i0= j-1
            i1= j+1
            if (i==j):
                if i0<0 or i0>=len(A[0]):
                    if A[i][j]<0 or A[i1][j]<0:
                        print(1)
                        print("La matriz no es tridiagonal")
                        return
                elif i1<0 or i1>=len(A[0]):
                    if A[i][j]<0 or A[i0][j]<0:
                        print(2)
                        print("La matriz no es tridiagonal")
                        return
                else:
                    if A[i][j]<0 or A[i0][j]<0 or A[i1][j]<0 :
                        print(3)
                        print("La matriz no es tridiagonal")
                        return
            else:
                if abs(i-j)>1:
                    if A[i][j]!=0:
                        print(i)
                        print(j)
                        print("La matriz no es tridiagonal")
                        return
    
           
    (P,L,U) = la.lu(A)
    D= np.diag(np.diag(U))
    k=0
    x = D+w*L
    try:
        inverse = np.linalg.inv(x)
    except np.linalg.LinAlgError:
        print("D+wL no es invertible")
        return
    else:
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
    

