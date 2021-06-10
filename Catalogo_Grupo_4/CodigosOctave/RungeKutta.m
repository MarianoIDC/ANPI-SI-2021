%{
    Metodo de Runge-Kutta de Orden 4
    Parametros de Entrada
        @param func: funcion a la cual se le aplicara el metodo
        @param a: valor inferior del intervalo
        @param b: valor superior del intervalo
        @param y0: valor inicial de y0
        @param pasoh: paso h
    
    Parametros de Salida
        @return paresXkYk: pares ordenados con los valores de xk yk
        @return polInter: polinomio de interpolacion
%}

clc;
clear;
pkg load symbolic;
warning("off","all");

function [paresXkYk, polInter] = runge_kutta_4(func, a, b, y0, pasoh)
    syms x y;
    x = [a : pasoh : b]';
    n = size(x)(1);
    y = zeros(1, n)';
    y(1) = y0;
    paresXkYk = zeros(n, 2);
    f = matlabFunction(sym(func));

    for(i = 1 : n - 1)
        k1 = f(x(i), y(i));
        k2 = f(x(i) + pasoh/2, y(i) + pasoh * k1/2);
        k3 = f(x(i) + pasoh/2, y(i) + pasoh * k2/2);
        k4 = f(x(i) + pasoh, y(i) + pasoh * k3);
        y(i+1) = y(i) + pasoh * (k1 + 2 * k2 + 2 * k3 + k4)/6;
    endfor

    for (i = 1 : n)
        paresXkYk(i, :) = [x(i) y(i)];
    endfor

    paresXkYk;
    polInter = dd_newton(paresXkYk);
    grafica(x, y);
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

%Intervalo inferior
a = 0;
%Intervalo superior
b = 1;
%Paso h
pasoh = 0.1;
%Valor inicial de y0
y0 = 1;
%Funcion 
funct = '-x * y + 4 * x/y';
printf("############################################ \n");
printf("Metodo de Runge-Kutta \n");
%Llamado de la funcion
[paresXkYk, polInter] =  runge_kutta_4(funct, a, b, y0, pasoh)