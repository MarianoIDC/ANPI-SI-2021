%{
    Metodo BFGS

    Esta funcion aplica el metodo BFGS para la optimizacion en varias
    variables.

    Sintaxis: bfgs(funcion, MAXIT, TOL)

    Parametros de entrada
        @param funcion: funcion a la cual se le aplicara el algoritmo
        @param vars: cantidad de variables en la funcion
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

function [x, err, n, f] = bfgs(funcion, vars, TOL)
%------------------------Calculando los valores de x0-----------------%
    x0 = [];
    iterl = [];
    errl = [];
    %Vector con la cantidad de numeros random en el rango especifico
    x0 = randi([-10, 10], vars, 1);
    x0
    %Guardando los valores de x0 en el vector X que tendra la solucion
    x(:, 1) = x0;
%---------------------Definiendo constantes del metodo----------------%
    b = 0.8;            % Valor para reducir el lambdak
    sigma = 0.4;        % Se debe cumplir que sigma existe en (0,1)
    Bk = eye(vars, vars)      % Debe ser una matriz definina positiva
%---------------------------------------------------------------------%
%--------------------------Metodo BFGS--------------------------------%
%---------------------------------------------------------------------%
    i = 1;
    err = TOL + 1;
    iterl(i) = i;
    errl(i) = err;
    while(err > TOL)
%-----------------------Calculando valores inicilaes------------------%    
        [~, g] = funcion(x(:, i));
        pk = -inv(Bk) * g;
        lambdak = 1;
        xk1 = x(:, i) + lambdak * pk;
        fizquierda = funcion(xk1);
        fderecha = funcion(x(:, i));
%--------------------------Armijo-type--------------------------------%
%---------------------------------------------------------------------%
        while(fizquierda > fderecha + sigma * lambdak * g' * pk)
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
        err =  norm(gk1);

        if(((yk'*sk)/(norm(sk))) > norm(gk))
            Bk1 = Bk - (Bk*(sk)*sk'*Bk)/(sk'*Bk*sk) + (yk*yk')/(yk'*sk);
            Bk = Bk1;
        else
            Bk = Bk;
        endif
        i = i + 1;
        iterl(i) = i;
        errl(i) = err;
        % Bk1 = Bk - (Bk*(sk)*sk'*Bk)/(sk'*Bk*sk) + (yk*yk')/(yk'*sk);
        % Bk = Bk1;
    endwhile
%---------------------------------------------------------------------%
%------------------------Fin Metodo BFGS------------------------------%
%---------------------------------------------------------------------%
    grafica(iterl, errl);
    n = i;
    f = funcion(x(:, end));
endfunction

%{
    Parametros de Entrada
        @param listaValoresX: valores del eje 'x'
        @param listaValoresY: valores del eje 'y'
    
    Parametros de Salida
        @return: Grafico de los datos ingresados
%}
function grafica(listaValoresX, listaValoresY)
    plot(listaValoresX, listaValoresY, 'g-');
    title("Metodo de la Biseccion");
    xlabel("Iteraciones");
    ylabel("% Error");
endfunction

function [f, g] = funcionObjetivo(X)
    f = -3803.84 - 138.08 * X(1) - 232.92 * X(2) + 128.08 * ((X(1))^2) + 203.64 * ((X(2))^2) + 182.25 * X(1) * X(2);
    g = [(6404/25)*X(1) + (729/4)*X(2) - (3452/25); (729/4)*X(1) + (10182/25)*X(2) - (5823/25)];
    % f = X(1)^2 + X(2)^3 + X(3)^4 + X(4)^5 + X(5)^6;
    % g = [2*X(1), 3*X(2)^2, 4*X(3)^3, 5*X(4)^4, 6*X(5)^5];
endfunction
# Cantidad de Variables
vars = 2;
# Tolerancia
tolerancia = 0.00001;

[x, err, n, f] = bfgs(@funcionObjetivo, vars, tolerancia);
printf("############################################ \n");
printf("Metodo BFGS \n");
printf('xAprox = %f\n', x);
printf('%%Error = %f\n', err);
printf('Iteraciones = %f\n', n);
printf('Punto minimo = %f\n', f);
printf("############################################ \n");