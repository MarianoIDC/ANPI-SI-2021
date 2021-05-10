%{
    Metodo de Diferencias Divididas de Newton
    Parametros de Entrada
        @param listaPO: vector con los pares ordenados xk, yk
    
    Parametros de Salida
        @return polinomio: polinomio de interpolacion
%}

clc;
clear;
pkg load symbolic;
warning("off","all");

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

%Vector de pares ordenados
listaPO = [-2 0; 0 1; 1 -1];
% listaPO = [1 2/3; 3 1; 5 -1; 6 0];
%Llamado de la funcion
polinomio =  dd_newton(listaPO);
printf("############################################ \n");
printf("Metodo Diferencias Divididas de Newton \n");
printf('Polinomio de Lagrange\n');
disp(polinomio);


