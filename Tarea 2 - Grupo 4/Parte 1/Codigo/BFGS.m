%{
    Metodo BFGS

    Esta funcion aplica el metodo BFGS para la optimizacion en varias
    variables.

    Sintaxis: bfgs(funcion, MAXIT, TOL)

    Parametros de entrada
        @param funcion: funcion a la cual se le aplicara el algoritmo
        @param MAXIT: cantidad maxima de iaciones a realizar
        @param TOL: tolerancia de la solucion

    Parametros de Salida
        @return x: vector de la aproximacion al punto minimo
        @return n: cantidad de iteraciones realizadas
        @return err: error final de la solucion
%}

clc;
clear;
close all;
warning('off', 'all');

function [x, err, n, f] = bfgs(funcion, MAXIT, TOL)
%------------------------Calculando los valores de x0-----------------%
    x0 = [];
    %Vector con la cantidad de numeros random en el rango especifico
    x0 = randi([-10, 10], 2, 1);
    x0
    %Guardando los valores de x0 en el vector X que tendra la solucion
    x(:, 1) = x0; 
%---------------------Definiendo constantes del metodo----------------%
    b = 0.8;            % Valor para reducir el lambdak
    sigma = 0.4;        % Se debe cumplir que sigma existe en (0,1)
    Bk = eye(2, 2)      % Debe ser una matriz definina positiva
%---------------------------------------------------------------------%
%--------------------------Metodo BFGS--------------------------------%
%---------------------------------------------------------------------%
    for (i = 1 : MAXIT)
%-----------------------Calculando valores inicilaes------------------%    
        [~, g] = funcion(x(:, i));
        pk = -inv(Bk) * g;
        lambdak = 1;
        xk1 = x(:, i) + lambdak * pk;
        fizquierda = funcion(xk1);
        fderecha = funcion(x(:, i));
%--------------------------Armijo-type--------------------------------%
%---------------------------------------------------------------------%
        while fizquierda > fderecha + sigma * lambdak * g' * pk
            lambdak = lambdak * b;
            xk1 = x(:, i) + lambdak * pk;
            fizquierda = funcion(xk1);
        endwhile
%---------------------------------------------------------------------%
%---------------------------------------------------------------------%
        x(:, i + 1) = xk1;
        [~, gk] = funcion(x(:, i));
        [~, gk1] = funcion(x(:, i + 1));
        yk = gk1 - gk;
        sk = x(:, i + 1) - x(:, i);
        Bk1 = Bk - (Bk*(sk)*sk'*Bk)/(sk'*Bk*sk) + (yk*yk')/(yk'*sk);
        Bk = Bk1;
        err =  norm(gk1);

        if(err < TOL)
            break;
        endif
    endfor
%---------------------------------------------------------------------%
%------------------------Fin Metodo BFGS------------------------------%
%---------------------------------------------------------------------%
    n = i;
    f = funcion(x(:, end));
endfunction


function [f, g] = funcionObjetivo(X)
    f = -3803.84 - 138.08 * X(1) - 232.92 * X(2) + 128.08 * ((X(1))^2) + 203.64 * ((X(2))^2) + 182.25 * X(1) * X(2);
    g = [(6404/25)*X(1) + (729/4)*X(2) - (3452/25); (729/4)*X(1) + (10182/25)*X(2) - (5823/25)];
endfunction

# Tolerancia
tolerancia = 0.00001;
# MAXIT
iterMax = 100;

[x, err, n, f] = bfgs(@funcionObjetivo, iterMax, tolerancia);
printf("############################################ \n");
printf("Metodo BFGS \n");
printf('xAprox = %f\n', x);
printf('%%Error = %f\n', err);
printf('Iteraciones = %f\n', n);
printf('Punto minimo = %f\n', f);
printf("############################################ \n");