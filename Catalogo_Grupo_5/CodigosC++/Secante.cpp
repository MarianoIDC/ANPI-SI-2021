#include <iostream>
#include <ginac/ginac.h>
#include <mgl2/mgl.h>
#include <cmath>

using namespace std;
using namespace GiNaC;

ex secante(string express, string firstValue, string secondValue, string tolerance, string iterations) {
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
        if (error < tol) {
            return xk;
        } else {
            ex f0 = evalf(subs(function, x == x0));
            ex f1 = evalf(subs(function, x == x1));
            xk = x1 - f1 * ((x1 - x0) / f1 - f0);
            error = abs(xk - x1)/abs(xk);
            x0 = x1;
            x1 = xk;
            iter++;
        }
    }
    cout << "Aproximación: " << xk << endl;
    cout << "Iteraciones : " << iter << endl;
    cout << "Error : " << error << endl;
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
    secante(express, x0, x1, tol, iterMax);
    return 0;
}
