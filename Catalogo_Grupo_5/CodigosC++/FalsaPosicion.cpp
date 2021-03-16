#include <iostream>
#include <ginac/ginac.h>
#include <mgl2/mgl.h>
#include <cmath>

using namespace std;
using namespace GiNaC;

ex falsaPosicion (string express, string firstValue, string secondValue, string tolerance, string iterations) {
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    ex function = reader(express);
    ex x0 = reader(firstValue);
    ex x1 = reader(secondValue);
    ex tol = reader(tolerance);
    ex iterMax = reader(iterations);
    int iter = 1;
    ex xk;
    ex error;
    while (iter < iterMax) {
        ex f0 = evalf(subs(function, x == x0));
        ex f1 = evalf(subs(function, x == x1));
        ex fx = evalf(subs(function, x == xk));
        if (f1 * f0 > 0) {
            cout << "No se cumple el Teorema de Bolzano" << endl;
            return 0;
        }
        else if (error < tol) {
            return xk;
        }
        else if (f1 * fx < 0) {
            x1 = xk;
        }
        else if (f0 * fx < 0) {
            x0 = xk;
        } else {
            xk = x1 - f1 * ((x1 - x0) / f1 - f0);
            error = abs(fx);
            iter++;
        }
    }
}

int main() {
    string express;
    cout << "Escriba la función: " << endl;
    cin >> express;
    string x0;
    cout << "Escriba el primer valor inicial: " << endl;
    cin >> x0;
    string x1;
    cout << "Escriba el segundo valor inicial: " << endl;
    cin >> x1;
    string tol;
    cout << "Escriba la tolerancia: " << endl;
    cin >> tol;
    string iterMax;
    cout << "Escriba el número de iteraciones: " << endl;
    cin >> iterMax;
    falsaPosicion(express, x0, x1, tol, iterMax);
    return 0;
}
