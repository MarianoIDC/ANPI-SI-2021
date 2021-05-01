%{
    Metodo de Gauss-Seidel
    Parametros de Entrada
        @param matrizD: matriz de coeficientes
        @param matrizI: vector de terminos independientes
        @param x: valor inicial 
        @param MAXIT: iteraciones maximas
        @param TOL: tolerancia de la respuesta
    
    Parametros de Salida
        @return xAprox: valor aproximado de X
        @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;
warning('off', 'all');

function [xAprox, err] = gaussSeidel(matrizD, matrizI, x, MAXIT, TOL)

  if(estrDiag(matrizD) == 0)
    disp("La matriz no es estrictamente diagonal dominante");
    return;
  else
    L = tril(matrizD, -1);
    D = diag(diag(matrizD));
    U = triu(matrizD, 1);
    b = matrizI';
    iter = 0;
    xAprox = x';
    xAnt = xAprox;
    err = TOL + 1;
    M = L + D;
    inversa = inv(M);
    iterl = [];
    errl = [];

    while(iter < MAXIT)
        xAprox = (-inversa*U*xAnt)+(inversa*b);
        iterl(iter+1) = iter;
        errl(iter+1) = err;
        err = norm(xAprox - xAnt);
        xAnt = xAprox;
        if(err < TOL)
            grafica(iterl, errl);
            return;
        else
            iter = iter + 1;
        endif
    endwhile
    grafica(iterl, errl);
    return;
  endif
endfunction

%{
    Parametros de Entrada
        @param A: matriz a determinar si es tridiagonal dominante o no.

    Parametros de Salida
        @return ft: retorna un valor de 1 o 0 si la matriz es dominante o no.
%}
function ft = estrDiag(A)
  n = length(A);
  m = length(A(1));
  d = 0;

  for(i = 1 : n)
    suma = 0;
    for(j = 1 : m)
      if(i == j)
        d = A(i, j);
      else
        suma = suma + (A(i, j)).^2;
      endif
    endfor

    if abs(d) < sqrt(suma)
      ft = 0;
      return;
    endif
  endfor
  ft = 1;
  return;
endfunction

%{
    Parametros de Entrada
        @param listaValoresX: valores del eje 'x'
        @param listaValoresY: valores del eje 'y'
    
    Parametros de Salida
        @return: Grafico de los datos ingresados
%}
function grafica(listaValoresX, listaValoresY)
    plot(listaValoresX, listaValoresY, 'x-');
    title("Metodo de Gauss-Seidel");
    xlabel("Iteraciones");
    ylabel("% Error");
endfunction

%Valor inicial
x = [0 0 0];
%Iteraciones maximas
MAXIT = 10;
%Tolerancia
TOL = 0.000001;
%Matriz de coeficientes
A = [5 1 1; 1 5 1; 1 1 5];
%Vector de terminos independientes
B = [7 7 7];
%Llamado de la funcion
[xAprox, err] =  gaussSeidel(A, B, x, MAXIT, TOL);
printf("############################################ \n");
printf("Metodo de Gauss-Seidel \n");
printf('xAprox = %f\nxAprox = %f\nxAprox = %f\n%%Error = %d \n', xAprox, err);