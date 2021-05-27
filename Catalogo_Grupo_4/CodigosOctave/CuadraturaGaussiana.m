%{
    Metodo de la Cuadratura Gaussiana
    Parametros de Entrada
        @param func: funcion a la cual se le calculara el area
        @param n: orden del polinomio
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

function [xAprox, err] = cuad_gaussiana(func, n, a, b)
    syms f(x);
    f(x) = func;
    
    %Calculo de los xi
    f_aux = '(x^2-1)^n';
    fs_aux = sym(f_aux);
    fsd_aux = diff(fs_aux, n);
    %Falta resolver fsd_aux = 0 para determinar los xi
    
    %Calculo de los wi
    g_aux = diff(fsd_aux);
    
    
    
    
    
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

%orden del polinomio
n=2;
%Intervalo inferior
a = 2;
%Intervalo superior
b = 5;
%Funcion 
func = @(x) log(x);
%Llamado de la funcion
[xAprox, err] = cuad_gaussiana(func, n, a, b);
% trapecio(func, a, b);
printf("############################################ \n");
printf("Metodo de la Cuadratura Gaussinan \n");
printf('xAprox = %f\n%%Error = %i \n', xAprox, err);