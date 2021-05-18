clc;
clear;
close all;
warning('off', 'all');

function [f, g] = funcionObjetivo(X)
    f = 0.04*(X(1))^2 + 0.01*(X(1)*X(2)) + 0.01*(X(2))^2 + 4*(X(1)) + 2*(X(2)) + 500;
    g = [(2/25)*X(1) + X(2)/100 + 4; X(1)/100 + X(2)/50 + 2];
endfunction

# Cantidad de Variables
vars = 2;
% vars = 5;
# Tolerancia
tolerancia = 0.00001;

[x, err, n, f] = @bfgs(@funcionObjetivo, vars, tolerancia);
printf("############################################ \n");
printf("Metodo BFGS Aplicado a Eonomia\n");
printf('xAprox = %f\n', abs(x));
printf('%%Error = %f\n', err);
printf('Iteraciones = %f\n', n);
printf('Punto minimo = %f\n', f);
printf("############################################ \n");