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



function [error] = cota_poly_inter(func, puntos)
pkg load symbolic
syms x 
%devuelve la cantidad de puntos
n = length(puntos);
puntos = sort(puntos);

a = puntos(1);
b = puntos(n);

m = 1/factorial(n+1);
p = '';

%Haciendo el polinomio p
for i = 1:length(puntos)
  if i == 1
     p = [p, '(x-',int2str(puntos(i)),')'];
  else
      p = [p, '*(x-',int2str(puntos(i)),')'];
  end
end

%Se pasa la funcion a simbolico
h = sym(p);
%Se pasa la funcion simbolica a ecuacion
h1=matlabFunction(h);
%se deriva la funcion
hd = diff(h,x)==0;
%puntos criticos
puntos_criticos_h = double(cell2mat(solve(hd,x)));
%Extremos del intervalo
puntos_a_evaluar_h=[a b puntos_criticos_h'];
valores_evaluados_h= [h1(puntos_a_evaluar_h)];
[pmax,p_max]=max(valores_evaluados_h);
  



%Encontrar el maximo de la funcion en un intervalo



%%%%Para Fmax
%Se pasa la funcion a simbolico
f = sym(func);
%Se pasa la funcion simbolica a ecuacion
f1=matlabFunction(f);
%se deriva la funcion
fd = diff(f,x,n+1)==0;
%puntos criticos
puntos_criticos = double(cell2mat(solve(fd,x)));
%Extremos del intervalo
puntos_a_evaluar=[a b puntos_criticos'];
valores_evaluados= [f1(puntos_a_evaluar)];
[fmax,x_max]=max(valores_evaluados);


error = abs(fmax*m*p);

endfunction

func = 'x^2+4';
puntos = [2, 3, 5];

[error] = cota_poly_inter(func, puntos)

