%{
    Cota de Error del Metodo de la Interpolacion
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el algoritmo
        @param a: inicio del intervalo
        @param b: fin del intervalo  
        @param h: paso de iteracion  
        
    Parametros de Salida
        @return par: pares ordenados
        @return pol: polinomio de interpolacion
        @return error: porcentaje de error del resultado obtenido
%}
clc;
clear;

function [xn yn] = euler(func,a,b,y0,N)
  pkg load symbolic;
  syms xy
  fs = sym(func);
  fe = matlabFunction(fs);
  
  h = (b-a)/(N-1);
  
  xn = a:h:b;
  yn = zeros(1,N);
  yn(1) = y0;
  
  
  
  
  for n=1:N-1
    yn(n+1)=yn(n)+h*fe(xn(n), yn(n));
    plot(xn,yn);
    par =(xn, yn)
  endfor 
endfunction

%Valores iniciales
a = 0;
b = 2;

y0 = 0.5;
%Numero de iteraciones 
N=11;
%Funcion 
func = 'y-x^2+1'
%Llamado de la funcion
printf("############################################ \n");
printf("Metodo de Euler \n");
[xn yn] =  euler(func, a, b, y0, N);


