%{
    Funcion que encuentra el gradiente de una funcion
    de manera simbolica

    Sintaxis: vergradiente(funcion, vars)

    Parametros de entrada
        @param funcion: funcion a la cual se le desea encontrar el gradiente
        @param vars: variables a utilizar en la funcion

    Parametros de Salida
        @return gradiente: representacion simbolica del gradiente
%}

clc;
clear;
close all;
warning('off', 'all');
pkg load symbolic;

function [gradiente] = vergradiente(funcion, vars)
    f = sym(funcion);
    gradiente = gradient(f, vars)

endfunction

# Variables
syms x1 x2 x3 x4 x5;            % Esto es probando con el f93
variables = [x1 x2 x3 x4 x5];   % Esto es probando con el f93
% syms x1 x2;                   % Esto es probando con el f99
% variables = [x1 x2];          % Esto es probando con el f99
# Funcion
f = '(x1)**2 + (x2)**3 + (x3)**4 + (x4)**5 + (x5)**6'; % Esto es probando con el f93
% f = '-3803.84 - 138.08*x1 - 232.92*x2 + 128.08*((x1)**2) + 203.64*((x2)**2) + 182.25*x1*x2'; % Esto es probando con el f99

printf("############################################ \n");
printf("Encuentra Gradiente \n");
vergradiente(f, variables);