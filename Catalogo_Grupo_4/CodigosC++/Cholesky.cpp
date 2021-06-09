#include <iostream>
#include <armadillo>
#include <cmath>

using namespace std;
using namespace arma;

/**
 * @param A: Una matriz A de cualquier tamano, simetrica y positiva definida
 * @return mat: Una matriz L que es la factorizacion de la matriz A
 */
mat cholesky(mat A)
{
    mat L(A.n_rows, A.n_cols, fill::zeros);
    for (int i = 0; i < A.n_rows; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            double suma = 0;
            if (j == i)
            {
                for (int k = 0; k < j; k++)
                {
                    suma += L(j, k) * L(j, k);
                }
                L(j, j) = sqrt(A(j, j) - suma);
            }
            else
            {
                for (int k = 0; k < j; k++)
                {
                    suma += L(i, k) * L(j, k);
                }
                L(i, j) = (A(i, j) - suma) / L(j, j);
            }
        }
    }
    return L;
}

/**
 * @param L: Una matriz L que es la factorizacion de Cholesky de otra matriz
 * @param y: Un vector d que es el vector de terminos independientes
 * @return colvec: Un vector y que es la solucion de este sistema de ecuaciones
 */
colvec sust_atras(mat L, colvec y)
{
    colvec x(L.n_rows, fill::zeros);
    for (int i = L.n_rows - 1; i > -1; i--)
    {
        int suma = 0;
        for (int j = i; j < L.n_rows; j++)
        {
            suma += L(i, j) * x(j);
        }
        x(i) = (y(i) - suma) / L(i, i);
    }
    return x;
}

/**
 * @param L: Una matriz L que es la transpuesta de la factorizacion 
 * de Cholesky de otra matriz
 * @param b: Un vector y que es el vector de terminos independientes
 * @return colvec: Un vector x que es la solucion de este sistema de ecuaciones
 */
colvec sust_adelante(mat L, colvec b)
{
    colvec y(L.n_rows, fill::zeros);
    for (int i = 0; i < L.n_rows; i++)
    {
        double suma = 0;
        for (int j = 0; j < i; j++)
        {
            suma += L(i, j) * y(j);
        }
        y(i) = (b(i) - suma) / L(i, i);
    }
    return y;
}

/**
 * @param A: Una matriz A de cualquier tamano
 * @param b: Un vector d que es el vector de terminos independientes
 */
void fact_Cholesky(mat A, colvec b)
{
    //Revisa si es simetrica positiva definida con una funcion propia de Armadillo
    if (!A.is_sympd())
    {
        A = A * trans(A);
        b = b * trans(A);
    }
    //Llama a las demas funciones y las guarda en variables
    cout << "Matriz: \n"
         << A << endl;
    cout << "Vector: \n"
         << b << endl;
    mat L = cholesky(A);
    cout << "Matriz factorizada: \n"
         << L << endl;
    colvec y = sust_adelante(L, b);
    cout << "Vector independiente: \n"
         << y << endl;
    colvec x = sust_atras(trans(L), y);
    cout << "Solucion del sistema: \n"
         << x << endl;
}

int main()
{
    //Matriz A que es simetrica positiva definida
    mat A = "25 15 -5 -10; 15 10 1 -7; -5 1 21 4; -10 -7 4 18";
    //Vector de terminos independientes
    colvec d = "-25 -19 -21 -5";
    //Realiza la factorizacion de Cholesky
    fact_Cholesky(A, d);
    return 0;
}
