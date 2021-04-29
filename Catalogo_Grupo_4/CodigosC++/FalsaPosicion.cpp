#include <iostream>
#include <ginac/ginac.h>

using namespace std;
using namespace GiNaC;

/**
 *
 * @param funcion: Funcion a la que se le va a aplicar el metodo
 * @param firstValue: primer valor inicial
 * @param secondValue: segundo valor inicial
 * @param TOL: tolerancia
 * @param MAXIT: cantidad maxima de iteraciones
 * @return
 * @return
 */
ex *falsaPosicion(string funcion, ex x0, ex x1, ex MAXIT, ex TOL) {

    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    ex f = reader(funcion);
    ex f0 = evalf(subs(f, x == x0));
    ex f1 = evalf(subs(f, x == x1));
    ex fxk;
    ex xk;
    ex error = TOL + 1;
    xk = x1 - ((x1 - x0) / (f1 - f0)) * f1;

    int iter = 1;
    static ex resultado[2];

    while (iter < MAXIT) {
        fxk = evalf(subs(f, x == xk));
        if (f0 * fxk < 0) {
            xk = xk - ((xk - x0) / (fxk - evalf(subs(f, x == x0)))) * fxk;
            x1 = xk;
            error = abs(evalf(subs(f, x == xk)));

            if(error < TOL) {
                break;
            }
            else {
                iter = iter + 1;
            }
        } else if (fxk * f1 < 0) {
            xk = xk - ((xk - x0) / (fxk - evalf(subs(f, x == x1)))) * fxk;
            x0 = xk;
            error = abs(evalf(subs(f, x == xk)));

            if(error < TOL) {
                break;
            }
            else {
                iter = iter + 1;
            }
        } else {
            cout << "No es posible de resolver mediante Falsa Posicion" << endl;
            return 0;
        }
    }
    resultado[0] = evalf(xk);
    resultado[1] = abs(evalf(subs(f, x == xk)));
    return resultado;
}

/**
 * Ejemplo numerico
 */
int main() {
    ex *testFP;
    testFP = falsaPosicion("cos(x)-x", 1 / 2, Pi / 4, 100, 0.0001);
    cout << "Aproximacion: " << *testFP << endl;
    cout << "Error: " << *(testFP + 1) << endl;
    return 0;
}