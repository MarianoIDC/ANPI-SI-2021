#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

/**
 * @param A: matriz de coeficientes
 * @param b: vector de terminos independientes
 * @param xInicial: vector de valores iniciales
 * @param MAXIT: cantidad de iteraciones maximas
 * @param TOL: tolerancia de la respuesta
 * @return tuple<vec, double>: vector solucion, error de la solucion 
 */
tuple<vec, double> jacobi(mat A, vec b, vec xInicial, int MAXIT, double TOL)
{

    mat D(size(A), fill::zeros);
    mat U(size(A), fill::zeros);
    mat L(size(A), fill::zeros);

    for (int i = 0; i < A.n_rows; i++)
    {
        for (int j = 0; j < A.n_cols; j++)
        {
            if (j < i)
            {
                L(i, j) = A(i, j);
            }
            else if (j > i)
            {
                U(i, j) = A(i, j);
            }
            else if (i == j)
            {
                D(i, j) = A(i, j);
            }
            else
            {
                cout << "Error" << endl;
            }
        }
    }

    vec xk = xInicial;
    vec xk1;
    int iter = 0;
    double err = TOL + 1;

    while (iter < MAXIT)
    {
        xk1 = ((-D.i()) * (L + U) * (xk)) + ((D.i()) * (b));
        xk = xk1;
        err = norm(A * xk - b);

        if (err < TOL)
        {
            break;
        }
        else
        {
            iter = iter + 1;
        }
    }
    return make_tuple(xk, err);
}

/**
 * Ejemplo numerico
 */
int main()
{
    tuple<vec,double> testJ=jacobi("5 1 1;1 5 1;1 1 5","7 7 7","0 0 0",100,0.000001);
    cout << "Aproximacion: \n"
         << get<0>(testJ) << endl;
    cout << "Error: " << get<1>(testJ) << endl;
    return 0;
}