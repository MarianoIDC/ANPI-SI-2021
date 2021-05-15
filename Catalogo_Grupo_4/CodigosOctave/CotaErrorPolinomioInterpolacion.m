%{
    Cota de Error del Metodo de la Interpolacion
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el algoritmo
        @param puntos: numero de puntos  
    
    Parametros de Salida
        @return xAprox: valor aproximado de x
        @return error: porcentaje de error del resultado obtenido
%}

% |f(x) - p(x)| <= |f^(n+1)(Ex)*1/(n+1!)*(x-x0)(x-x1)...(x-xn)|
%% fmax = f^(n+1)(Ex) ==> donde la funcion derivada a la n+1 es maxima
%% a = 1/(n+1!)       ==> alpha
%% p = (x-x0)(x-x1)...(x-xn)
% Ex pertence a [a,b]

clc
clear;
%
%Se carga el paquete simbolico%

pkg load symbolic
syms x 



function [error] = cota_poly_inter(func, puntos)

%devuelve la cantidad de puntos
n = length(puntos)

a = 1/factorial(n+1)
%
p = 1

%Encontrar el maximo de la funcion en un intervalo

%Se pasa la funcion a simbolico
f = sym(func)
%Se pasa la funcion simbolica a ecuacion
f1=matlabFunction(f);
%se deriva la funcion
fd = diff(f,x,n+1)==0;
%puntos criticos
puntos_criticos = double(cell2mat(solve(fd,x)));
%Extremos del intervalo
a = puntos[0]
b = puntos[n-1]
puntos_a_evaluar=[a b puntos_criticos'];
valores_evaluados= [f1(puntos_a_evaluar)];
[fmax,x_max]=max(valores_evaluados)


error = abs(fmax*a*p)


%f_aux = fnmax(diff(func, n+1), puntos)

%pasar a simbolico
%matlabFunction
%fnmax(f_aux, [a,b])


endfunction
