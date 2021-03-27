#include <iostream>
#include "funtras.h"


int main() {
    std::cout << "Hello, World!" << std::endl;

    double fac, expe, expoNUNO, seno, coseno, tangente, logan, logb, powert, senoh, cosenoh, tanoh, raiz, raizx, aseno, atan;

    fac = factorial(7);
    cout << "El factorial de 7 es: " << fac;
    cout << "\n";
    expe = exp_t(11);
    cout << "El resultado de e^11 es: " << expe;
    cout << "\n";
    expoNUNO = varM1(144);
    cout << "El calculo de 144^-1 es: "<< expoNUNO;
    cout << "\n";
    seno = sin_t(2.33);
    cout << "El seno de 2.33 es: "<< seno;
    cout << "\n";
    coseno = cos_t(3.78);
    cout << "El coseno de 3.78 es: "<< coseno;
    cout << "\n";
    tangente = tan_t(7);
    cout << "La tangente de 7 es: "<< tangente;
    cout << "\n";
    logan = ln_t(45);
    cout << "El logaritmo natural de 45 es: "<< logan;
    cout << "\n";
    logb = log_t(33, 43);
    cout << "El logaritmo en base 5 de 2 es: "<< logb;
    cout << "\n";
    powert = power_t(2, 11);
    cout << "El resultado de 2^11 es: "<< powert;
    cout << "\n";
    senoh = sinh_t(2.1);
    cout << "El senoh de 2.1 es: "<< senoh;
    cout << "\n";
    cosenoh = cosh_t(0.89);
    cout << "El cosenoh de 0.89 es: "<< cosenoh;
    cout << "\n";
    tanoh = tanh_t(0.22);
    cout << "El tanoh de 0.22 es: "<< tanoh;
    cout << "\n";
    raiz = sqrt_t(144);
    cout << "La raiz cuadrada de 144 es: "<< raiz;
    cout << "\n";
    int a = 7;
    raizx = root_t(45, a);
    cout << "La raiz " << a<<" de 45 es:"<< raizx;
    cout << "\n";
    aseno = asin_t(2.1);
    cout << "El aseno de 2 es: "<< aseno;
    cout << "\n";
    atan = atan_t(1.37);
    cout << "El atan de 2 es: "<< atan;
    cout << "\n";

    return 0;
}
