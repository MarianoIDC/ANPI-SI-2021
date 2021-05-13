%{
    Metodo de la Regla del Trapezio
    Parametros de Entrada
        @param func: funcion a la cual se le calculara el area
        @param a: valor inferior
        @param b: valor superior
    
    Parametros de Salida
        @return xAprox: valor aproximado del area
        @return err: porcentaje de error del resultado obtenido
%}

clc;
clear;
pkg load symbolic;
warning("off","all");

function [xAprox, err] = trapecio(func, a, b)
    syms f(x);
    f(x) = func;
    xAprox = ((b - a)/(2))*((func(a)) + (func(b)));
    fd = diff(f, 2);
    fd = function_handle(fd);
    lista = [];
    lista(1) = abs(fd(a));
    lista(2) = abs(fd(b));
    vmax = max(lista);
    err = (((b - a)**3)/12)*vmax;
    return;
endfunction


%Intervalo inferior
a = 2;
%Intervalo superior
b = 5;
%Funcion 
func = @(x) log(x);
%Llamado de la funcion
[xAprox, err] = trapecio(func, a, b);
% trapecio(func, a, b);
printf("############################################ \n");
printf("Metodo de la Regla del Trapecio \n");
printf('xAprox = %f\n%%Error = %i \n', xAprox, err);