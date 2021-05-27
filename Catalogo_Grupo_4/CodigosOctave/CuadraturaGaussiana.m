%{
    Metodo de Diferencias Divididas de Newton
    Parametros de Entrada
        @param funcion: funcion a calcular la integral
        mediante el metodo de cradraturas gaussianas
        @param a: intervalo inferior de la integral
        @param b: intervalo superior de la integral
        @param n: orden del polinomio
    
    Parametros de Salida
        @return xAprox: aproximacion de la integral
        @return err: error del calculo
%}

clc;
clear;
warning("off","all");
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Se utiliza el paquete miscellaneous, este se puede
#instalar utilizando el comando:
% pkg install -forge miscellaneous
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [xAprox, err] = cuad_gaussiana(funcion, a, b, n)
    xAprox = 0;
    i = 1;
    legendrePol = legendrepoly(n);
    cerosPol = roots(legendrePol);
    derPol = polyder(legendrePol);
    while(i <= n)
        xi = cerosPol(i);
        Pi = polyval(derPol, xi);
        wi = 2/((1-(xi^2))*(Pi)^2);
        xAprox = xAprox + wi*funcion(xi);
        i = i + 1;
    endwhile
    q = integral(funcion, a, b);
    xAprox;
    err = abs(xAprox - q);
endfunction

%Intervalos de la integral
a = -1;
b = 1;
%Grado del polinomio
n = 3;
%Funcion 
funct = @(x) exp(x).*cos(x);
%Llamado de la funcion
[xAprox, err] =  cuad_gaussiana(funct, a, b, n);
printf("############################################ \n");
printf("Metodo de las Cuadraturas Gaussianas \n");
printf('xAprox = %f\n%%Error = %d \n', xAprox, err);