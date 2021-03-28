#include <iostream>
#include "funtras.h"

using namespace std;

int main()
{

    double resultado = root_t((sin_t(3 * varM1(7)) + ln_t(2)), 3) * varM1(sinh_t(sqrt_t(2))) + atan_t(varM1(exp_t(1)));
    cout << "El resultado de la funcion para el punto 1.1 es: " << resultado;
    cout << "\n";

    return 0;
}