%{
    Metodo de Eliminacion Gaussiana
    Parametros de Entrada
        @param matrizD: matriz de coeficientes
        @param matrizI: vector de terminos independientes
    
    Parametros de Salida
        @return vectorResultado: solucion del sistema
%}

clc;
clear;
warning('off', 'all');

function X = gaussiana(matrizD, matrizI)
  [n, m] = size(matrizD);
  if (n ~= m)
    disp("La matrizD debe ser cuadrada");
  endif

  n = length(matrizD);
  X = [matrizD, matrizI];
  % Por cada argumento de la matriz
  for(i = 1 : n)
    pivot = X(i, i);
    pivotRow = X(i, :);
    % Multiplica los vectores
    M = zeros(1, n - i);
    m = length(M);
    % Obtiene cada fila multiplicada
    for(k = 1 : m)
      M(k) = X(i + k, i) / pivot;
    endfor
    % Modifica cada fila
    for(k = 1 : m)
      X(i + k, :) = X(i + k, :) - pivotRow*M(k);
    endfor
  endfor
  X = sustitucionAtras(X(1 : n, 1 : n), X(:, n + 1));
endfunction

%{
    Metodo de Sustitucion Atras
    -Resuelve un sistema del tipo Ax = b
    Parametros de Entrada
        @param matrizA: matriz triangular superior NxN
        @param matrizB: matriz Nx1
    
    Parametros de Salida
        @return X: solucion de la matriz
%}

function X = sustitucionAtras(matrizA, matrizB)
  n = length(matrizB);
  X = zeros(n, 1);
  X(n) = matrizB(n)/matrizA(n, n);
    
  for(k = n-1 : -1 : 1)
    div = matrizA(k, k);
    if (div != 0)
      X(k) = (matrizB(k) - matrizA(k, k + 1 : n)*X(k + 1 : n))/matrizA(k, k);
    else
      disp("Error: se ha producido una division por cero");
    endif
  endfor
endfunction

%Matriz de coeficientes
A = [2 -6 12 16 ; 1 -2 6 6; -1 3 -3 -7; 0 4 3 -6];
%Matriz de terminos independientes
B = [70 26 -30 -26]';
%Llamado de la funcion
X = gaussiana(A, B);
printf("############################################ \n");
printf("Metodo de la Eliminacion Gaussiana \n");
printf('X = %f\n', X);