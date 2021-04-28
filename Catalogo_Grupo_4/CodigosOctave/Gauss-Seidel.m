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
pkg load symbolic;
format long;
warning('off', 'all');

function [xAprox, err] = gaussSeidel(matrizD, matrizI, x, MAXIT, TOL)
    L = tril(matrizD, -1);
    D = diag(diag(matrizD));
    U = triu(matrizD, 1);
    b = matrizI';
    iter = 0;
    xAprox = x';
    err = 1;
    M = L + D;
    inversa = inv(M);
    iterl = []; % Lista que almacena el numero de iteraciones para despues graficar
    errl = []; % Lista que almacena el % de error de cada iteracion para despues graficar

    while(iter < MAXIT)
        xAprox = (-inversa*U*xAprox)+(inversa*b);

        iterl(iter+1) = iter;
        errl(iter+1) = err;
        
        err = norm(xAprox);

        %iter = iter + 1;

        if(err < TOL)
            grafica(iterl, errl);
            return;
        else
            iter = iter + 1;
        endif
    endwhile
    grafica(iterl, errl);
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
TOL = 0.0001;
%Matriz de coeficientes
A = [5 1 1; 1 5 1; 1 1 5];
%Vector de terminos independientes
B = [7 7 7];
%Llamado de la funcion
[xAprox, err] =  gaussSeidel(A, B, x, MAXIT, TOL);
printf("############################################ \n");
printf("Metodo de Gauss-Seidel \n");
printf('xAprox = %f\nxAprox = %f\nxAprox = %f\n%%Error = %d \n', xAprox, err);