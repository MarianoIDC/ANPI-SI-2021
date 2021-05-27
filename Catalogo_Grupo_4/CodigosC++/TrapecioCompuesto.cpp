#include <iostream>
#include <ginac/ginac.h>
#include <armadillo>
#include <cmath>

using namespace std;
using namespace GiNaC;
using namespace arma;

/**
 * @param func: La funcion a evaluar en la regla del trapecio
 * @param a: El primer elemento del intervalo a evaluar
 * @param b: El ultimo elemento del intervalo a evaluar
 * @return p: El polinomio de interpolacion del conjunto de puntos
 */
double trapecio(string func, double a, double b) {
    //Se carga la variable simbolica
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    ex f = reader(func);
    //Se evalua la variable simbolica en los intervalos
    ex f0 = evalf(subs(f, x == a));
    ex f1 = evalf(subs(f, x == b));
    //Se define la variable h
    ex h = (b - a)/2;
    //Se calcula la integral
    double I = ex_to<numeric>(h * (f0 + f1)).to_double();
    return I;
}

/**
 * @param func: La funcion a evaluar en la regla del trapecio compuesta
 * @param a: El primer elemento del intervalo a evaluar
 * @param b: El ultimo elemento del intervalo a evaluar
 * @param N: La cantidad de puntos que se le van a pasar al intervalo
 * @return p: El polinomio de interpolacion del conjunto de puntos
 */
tuple<double, double> trapecio_compuesto(string func, double a, double b, int N) {
    //Se carga la variable simbolica
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    ex f = reader(func);
    //Se define la variable h
    double h = (b - a)/(N - 1);
    //Se define el vector de puntos sobre el que se va a operar
    vec xv(N, fill::zeros);
    for (int i = 0; i < N; i++) {
        xv(i) = a;
        a += h;
    }
    //Se realiza el calculo de la integral mediante la regla del trapecio
    double I = 0;
    for (int i = 0; i < N - 1; i++) {
        I += trapecio(func, xv(i), xv(i + 1));
    }
    //Se obtiene la segunda derivada de la funcion
    ex fd = f.diff(x, 2);
    vec xd(2, fill::zeros);
    //Se obtiene el alfa maximo a utilizar en la cota de error mediante el maximo de la segunda derivada
    xd(0) = ex_to<numeric>(evalf(subs(fd, x == a))).to_double();
    xd(1) = ex_to<numeric>(evalf(subs(fd, x == b))).to_double();
    double alphaMax = *max_element(xd.begin(), xd.end());
    //Se obtiene la cota de error
    double error = (((b - a) * (h * h))/12) * alphaMax;
    return make_tuple(I, error);
}

int main() {
    //Funcion a integrar
    string f = "log(x)";
    //Regla del trapecio y cota de error
    tuple<double, double> testTrapecio = trapecio_compuesto(f, 2, 5, 1000);
    cout << "Regla del Trapecio: " << get<0>(testTrapecio)  << endl;
    cout << "Cota de Error: " << get<1>(testTrapecio)  << endl;
    return 0;
}
