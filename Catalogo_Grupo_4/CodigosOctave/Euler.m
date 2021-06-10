%{
    Metodo de Euler
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el algoritmo
        @param a: inicio del intervalo
        @param b: fin del intervalo  
        @param y0: valor inicial
        @param h: paso de iteracion  
        
    Parametros de Salida
        @return paresXnYn: pares ordenados
        @return polInter: polinomio de interpolacion
%}

clc;
clear;
pkg load symbolic;
warning("off","all");

function [paresXnYn, polInter] = euler(func, a, b, y0, h)
    syms x y;
    fs = sym(func);
    fe = matlabFunction(fs);
    xn = [a : h : b]';
    n = size(xn)(1);
    yn = zeros(1, n)';
    yn(1) = y0;
    paresXnYn = zeros(n, 2);
    
    for (i = 1 : n - 1)
        yn(i+1) = yn(i) + h * fe(xn(i), yn(i));
    endfor
  
    for (i = 1 : n)
        paresXnYn(i, :) = [xn(i) yn(i)];
    endfor
  
    grafica(xn, yn);
    polInter = dd_newton(paresXnYn);
endfunction

%{
    Metodo de Diferencias Divididas de Newton
    Parametros de Entrada
        @param listaPO: vector con los pares ordenados xk, yk
    
    Parametros de Salida
        @return polinomio: polinomio de interpolacion
%}

function polinomio = dd_newton(listaPO)
    [n, m] = size(listaPO);

    if(m ~= 2)
        disp("Error, la cantidad de puntos ingresada no es correcta");
        return;
    else
        x = sym('x');
        rk = [];
        for(i = 1 : n)
            rk = [rk listaPO(i, 2)];
        endfor

        polinomio = listaPO(1, 2);
        multi1 = 1;
        m = n - 1;
        for(i = 2 : n)
            multi1 = multi1 * (x - listaPO(i - 1, 1));
            rk1 = [];
            for(j = 1: m)
                numerador = rk(j) - rk(j + 1);
                denominador = listaPO(j, 1) - listaPO(j + i - 1, 1);
                rk1 = [rk1 (numerador / denominador)];
            endfor
            m = m - 1;
            polinomio =  polinomio + rk1(1) * multi1;
            rk = rk1;
        endfor
        polinomio = expand(polinomio);
        return;
    endif
endfunction

%{
    Parametros de Entrada
        @param listaValoresX: valores del eje 'x'
        @param listaValoresY: valores del eje 'y'
    
    Parametros de Salida
        @return: Grafico de los datos ingresados
%}

function grafica(listaValoresX, listaValoresY)
    plot(listaValoresX, listaValoresY, 'b-');
    title("Grafica Polinomio de Interpolacion");
    xlabel("Eje x")
    ylabel("Eje y");
endfunction

%Valores iniciales
a = 0;
b = 2;
y0 = 0.5;
%Numero de iteraciones 
N = 11;
h = (b - a)/(N - 1);
%Funcion 
func = 'y-x^2+1';
%Llamado de la funcion
printf("############################################ \n");
printf("Metodo de Euler \n");
[paresXnYn, polInter] =  euler(func, a, b, y0, h)


