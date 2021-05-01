#include <iostream>
#include <armadillo>
#include <cmath>

using namespace std;
using namespace arma;

//Función que realiza la factorización de Cholesky
//Entradas: Una matriz A de cualquier tamaño, simétrica y positiva definida
//Salidas: Una matriz L que es la factorización de la matriz A
mat cholesky(mat A) {
    mat L(A.n_rows, A.n_cols, fill::zeros);
    for (int i = 0; i < A.n_rows; i++) {
        for (int j = 0; j < i + 1; j++) {
            int suma1 = 0;
            int suma2 = 0;
            if (j == i) {
                for (int k = 0; k < j; k++) {
                    suma1 += pow((double)L(j, k), 2.0);
                L(j, j) = sqrt(A(j, j) - suma1);
                }
            } else {
                for (int k = 0; k < j; k++) {
                    suma2 += L(i, k) * L(j, k);
                L(i, j) = (A(i, j) - suma2)/L(j, j);
                }
            }
        }
    }
    return L;
}

//Función que realiza la sustitución hacia atrás
//Entradas:
// Una matriz L que es la factorización de Cholesky de otra matriz
// Un vector d que es el vector de términos independientes
//Salidas: Un vector y que es la solución de este sistema de ecuaciones
colvec sust_atras(mat L, colvec y) {
    int n = L.n_rows;
    colvec x(L.n_rows, fill::zeros);
    for (int i = n - 1; i > 0; i--) {
        int suma = 0;
        for (int j = i + 1; j < n; j++) {
            suma += L(i, j) * x(j);
        }
        x(i) = (y(i) - suma)/L(i, i);
    }
    return y;
}

//Función que realiza la sustitución hacia atrás
//Entradas:
// Una matriz L que es la transpuesta de la factorización de Cholesky de otra matriz
// Un vector y que es el vector de términos independientes
//Salidas: Un vector x que es la solución de este sistema de ecuaciones
colvec sust_adelante(mat L, colvec d) {
    int n = L.n_rows;
    colvec y(L.n_rows, fill::zeros);
    for (int i = n - 1; i > 0; i--) {
        int suma = 0;
        for (int j = 1; j < i - 1; j++) {
            suma += L(i, j) * y(j);
        }
        y(i) = (d(i) - suma)/L(i, i);
    }
    return y;
}

//Función que realiza la sustitución hacia atrás
//Entradas:
// Una matriz A de cualquier tamaño
// Un vector d que es el vector de términos independientes
//Salidas: Un vector x que es la solución del sistema de ecuaciones
colvec fact_Cholesky(mat A, colvec b) {
    //Revisa si es simétrica positiva definida con una función propia de Armadillo
    if (!A.is_sympd()) {
        A = A * trans(A);
        b = b * trans(A);
    } else {
        A = A;
        b = b;
    }
    //Llama a las demás funciones y las guarda en variables
    mat L = cholesky(A);
    colvec y = sust_adelante(L, b);
    colvec x = sust_atras(trans(L), y);
    return x;
}

int main() {
    //Matriz A que es simétrica positiva definida
    mat A = "25 15 -5 -10; 15 10 1 -7; -5 1 21 4; -10 -7 4 18";
    //Vector d de términos independientes
    colvec d = "-25 -19 -21 -5";
    //Realiza la factorización de Cholesky
    colvec testCholesky = fact_Cholesky(A, d);
    cout << "Solución del sistema: \n" << testCholesky << endl;
    return 0;
}
