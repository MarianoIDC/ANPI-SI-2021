%{
    Metodo BFGS

    Esta funcion aplica el metodo BFGS para la optimizacion en varias
    variables.

    Sintaxis: bfgs(funcion, vars, MAXIT, TOL)

    Parametros de entrada
        @param funcion: funcion a la cual se le aplicara el algoritmo
        @param vars: variables a utilizar en la funcion
        @param MAXIT: cantidad maxima de iteraciones a realizar
        @param TOL: tolerancia de la solucion

    Parametros de Salida
        @return xk: aproximacion al punto minimo
        @return iteraciones: cantidad de iteraciones realizadas
        @return err: error final de la solucion
%}

clc;
clear;
warning('off', 'all');
pkg load symbolic;


function [xk, err, iter] = bfgs(funcion, vars, MAXIT, TOL)
%---------------------------Preparando utilitarios--------------------%
    n = length(vars);
    f = sym(funcion);
    x0 = [];
    i = 1;
    iterl = [];
    errl = [];
%------------------------Calculando los valores de xi----------------%
# -10 <= xi <= 10
    while(i <= n)
        % x0 = [x0 1/randi(100)]; % Esto es probando con el f93
        x0 = [x0 randi(10)]; % Esto es probando con el f99
        i++;
    endwhile
    double(x0);
    x0 = reshape(x0, n, 1)  %Vector ahora como matriz
%---------------------Definiendo constantes del metodo----------------%
    lambdak = 1;    % Al utilizar Wolf-type se define lambdak = 1
    sigma1 = 0.0025;  % Se debe cumplir que sigma1 < sigma 2
    sigma2 = 0.050;  % Se debe cumplir qur sigma2 < 1
    xk = x0;
    B = eye(n, n);  % Debe ser una matriz definina positiva
    Bk = B;         % es por esto que se utiliza la Midentidad
%-----------------------Calculando valores inicilaes------------------%
    g = gradient(f, vars);
    gxk = subs(g, vars, xk);
    err = double(norm(subs(g, vars, xk)));
    k = 1;
    iter = 0;
%---------------------------------------------------------------------%
%--------------------------Metodo BFGS--------------------------------%
%---------------------------------------------------------------------%
    while(iter < MAXIT && err > TOL)
        gxk = subs(g, vars, xk);
        pk = inv(B)*(-gxk);
%---------------------------Wolf-type---------------------------------%
        fizquierda = double(subs(f, vars, (xk + lambdak * pk)));
        fderecha = double(subs(f, vars, xk)) + sigma1 * lambdak * double(transpose(gxk) * pk);
        gizquierda = double(double(transpose(subs(g, vars, xk + lambdak * pk))) * pk);
        gderecha = double(double(transpose(subs(g, vars, xk))) * pk) * sigma2;

        while(!((fizquierda <= fderecha) && (gizquierda >= gderecha)))
            lambdak = double(lambdak/2);
            if(lambdak < TOL);
                break;
            endif
            fizquierda = double(subs(f, vars, (xk + lambdak * pk)));
            fderecha = double(subs(f, vars, xk)) + sigma1 * lambdak * double(transpose(gxk) * pk);
            gizquierda = double(double(transpose(subs(g, vars, xk + lambdak * pk))) * pk);
            gderecha = double(double(transpose(subs(g, vars, xk))) * pk) * sigma2;
        endwhile
%----------------------------Wolf-type--------------------------------%
        xk1 = xk + lambdak*pk;
        sk = xk1 - xk;
        yk = double(subs(g, vars, xk1) - subs(g, vars, xk));
        skt = transpose(sk);
        ykt = transpose(yk);
        Bk1 = Bk - ((Bk*sk*skt*Bk)/(skt*Bk*sk)) + ((yk*ykt)/(ykt*sk));
        xk = xk1
        err = double(norm(subs(g, vars, xk)));
        iter++;
    endwhile
%---------------------------------------------------------------------%
%------------------------Fin Metodo BFGS------------------------------%
%---------------------------------------------------------------------%
    xk = double(xk);
    return;
endfunction

# Variables
% syms x1 x2 x3 x4 x5;            % Esto es probando con el f93
% variables = [x1 x2 x3 x4 x5];   % Esto es probando con el f93
syms x1 x2;                   % Esto es probando con el f99
variables = [x1 x2];          % Esto es probando con el f99
# Funcion
% f = '(x1)**2 + (x2)**3 + (x3)**4 + (x4)**4 + (x5)**6'; % Esto es probando con el f93
f = '-3803.84 - 138.08*x1 - 232.92*x2 + 128.08*((x1)**2) + 203.64*((x2)**2) + 182.25*x1*x2'; % Esto es probando con el f99
# Tolerancia
tolerancia = 0.00001;
# MAXIT
iterMax = 3;

[xk, err, iter] = bfgs(f, variables, iterMax, tolerancia);
printf("############################################ \n");
printf("Metodo BFGS \n");
printf('xAprox = %f\n', xk);
printf('%%Error = %f\n', err);
printf('Iteraciones = %f\n', iter);
printf("############################################ \n");