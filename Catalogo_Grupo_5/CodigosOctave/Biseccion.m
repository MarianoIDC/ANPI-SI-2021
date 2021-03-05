%{
    Metodo de la Biseccion
    Parametros de Entrada
    @param f: funcion a la cual se le aplicara el algoritmo
    @param a: limite inferior del intervalo
    @param b: limite superior del intervalo
    @param MAXIT:  iteraciones maximas
    @param TOL:  tolerencia del algoritmo
    
    Parametros de Salida
    @return xAprox: valor aproximado de x
    @return error: porcentaje de error del resultado obtenido
%}

clc;
clear;

function [xAprox, iter] = biseccion(f, a, b, MAXIT, TOL)

    if(f(a) * f(b) < 0)
    
        iter = 1;
        iterl = [];
        err = 0;
        errl = [];

        while(iter < MAXIT)
            xAprox = (a + b) / 2;
            fx = f(xAprox);

            if(f(a) * fx < 0)
                b = xAprox;
            elseif(f(b) * fx < 0)
                a = xAprox;
            elseif(abs(fx) < TOL)
                return;
            endif

            iterl(iter) = iter;
            errl(iter) = err;
           
            iter = iter + 1;
            err = (b - a)/ (2);
            
            plot(iterl, errl);
            title("Metodo de la Biseccion");
            xlabel("Iteraciones");
            ylabel("% Error");

      endwhile
    else
        error("Condiciones en los parametros de entrada no garantizan el cero de la funcion.")
    endif
    return;
endfunction

a = 0;
b = 2;
MAXIT = 100;
TOL = 0.000001;
funct = @(x) e^x - x - 2;
[xAprox, iter] =  biseccion(funct, a, b, MAXIT, TOL);
printf('xAprox = %f\nIteraciones = %i \n', xAprox, iter);