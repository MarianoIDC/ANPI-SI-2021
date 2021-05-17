#include <iostream>
#include <ginac/ginac.h>

using namespace std;
using namespace GiNaC;

/**
 * @param funcion: Funcion a evaluar en el metodo
 * @param x0: primer valor inicial
 * @param x1: segundo valor inicial
 * @param MAXIT: cantidad maxima de iteraciones
 * @param TOL: tolerancia del resultado
 * @return tuple<ex, ex>: valor aproximado, error del valor aproximado
 */
tuple<ex, ex> secante(string funcion, ex x0, ex x1, ex MAXIT, ex TOL)
{
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

    while (iter < MAXIT)
    {
        xk1 = xk -
              ((((xk - xkm1)) / ((evalf(subs(f, x == xk))))) - evalf(subs(f, x == xkm1))) * (evalf(subs(f, x == xk)));
        xkm1 = xk;
        xk = xk1;
        err = abs(evalf(subs(f, x == xk)));

        if (err < TOL)
        {
            break;
        }
        else
        {
            iter = iter + 1;
        }
    }
    xk;
    err = abs((evalf(subs(f, x == xk))));
    return make_tuple(xk, err);
}

int main(void)
{
    tuple<ex, ex> testS = secante("exp(-pow(x, 2)) - x", 0, 1, 100, 0.001);
    cout << "Aproximacion: " << get<0>(testS) << endl;
    cout << "Error: " << get<1>(testS) << endl;
    return 0;
}