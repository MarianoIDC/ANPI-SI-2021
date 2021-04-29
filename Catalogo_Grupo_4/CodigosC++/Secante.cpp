#include <iostream>
#include <ginac/ginac.h>

using namespace std;
using namespace GiNaC;

/**
 *
 * @param funcion: Funcion a evaluar en el metodo
 * @param x0: primer valor inicial
 * @param x1: segundo valor inicial
 * @param MAXIT: cantidad maxima de iteraciones
 * @param TOL: tolerancia del resultado
 * @return
 */
ex *secante(string funcion, ex x0, ex x1, ex MAXIT, ex TOL) {
    symbol x;
    symtab table;
    table["x"] = x;
    parser reader(table);
    ex f = reader(funcion);
    ex xk = x1;
    ex xkm1 = x0;
    ex xk1;
    int iter = 0;
    ex err = TOL + 1;
    static ex resultado[2];

    while (iter < MAXIT) {
        xk1 = xk -
              ((((xk - xkm1)) / ((evalf(subs(f, x == xk))))) - evalf(subs(f, x == xkm1))) * (evalf(subs(f, x == xk)));
        xkm1 = xk;
        xk = xk1;
        err = abs(evalf(subs(f, x == xk)));

        if (err < TOL) {
            break;
        } else {
            iter = iter + 1;
        }
    }
    resultado[0] = xk;
    resultado[1] = abs((evalf(subs(f, x == xk))));
    return resultado;
}

/**
 * Ejemplo numerico
 */
int main(void) {
    ex *testS;
    testS = secante("exp(-pow(x, 2)) - x", 0, 1, 100, 0.001);
    cout << "Aproximacion: " << *testS << endl;
    cout << "Error: " << *(testS + 1) << endl;
    return 0;
}