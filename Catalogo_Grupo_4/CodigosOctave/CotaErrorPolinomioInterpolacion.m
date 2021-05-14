%{
    Cota de Error del Metodo de la Interpolacion
    Parametros de Entrada
        @param f: funcion a la cual se le aplicara el algoritmo
        @param n: numero de puntos  
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
        @return error: porcentaje de error del resultado obtenido
%}

% |f(x) - p(x)| <= |f^(n+1)(Ex)*1/(n+1!)*(x-x0)(x-x1)...(x-xn)|
% Ex pertence a [a,b]

clc
clear;

function [error] = cota_poly_inter(func, vars)

pkg load symbolic
syms x 

n = length(vars)
a = 1/factorial(n+1)
f_aux = diff(func, n+1)


end
