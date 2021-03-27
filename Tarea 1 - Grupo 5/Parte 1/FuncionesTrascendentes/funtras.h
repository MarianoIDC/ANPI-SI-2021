#ifndef FUNCIONESTRASCENDENTES_FUNTRAS_H
#define FUNCIONESTRASCENDENTES_FUNTRAS_H

#include <cmath>
#include <iostream>
#include <stdlib.h>


using namespace std;
const double TOL = 0.00000001;
const double MAXITER = 2500;

/**
 * Metodo que se encarga de calcular el calculo de la operacion
 * factorial de un numero
 * @param num: numero al que se le desea encontrar su factorial
 * @return numfact: factorial del numero ingresado
 */
double factorial(int num) {
    double numfact = 1;
    if (num < 0) {
        cout << "El factorial solo se puede calcular para numeros mayores o iguales a cero. \n";
    } else {
        for (int i = 1; i <= num; i++) {
            numfact = numfact * i;
        }
    }
    return numfact;
}

/**
 * Metodo que se encarga de obtener el valor de x^-1.
 * @param a: numero a elevar.
 * @return xk0: resultado de la operacion.
 */
double varM1(double a) {
    double xk0, xk1, eps = 2.2204E-16, facta, fact0, fact20, fact40, fact60, fact80, fact100, condParada=1;
    int i = 0;

    if (a > 0) {
        facta = a;
        fact0 = factorial(0);
        fact20 = factorial(20);
        fact40 = factorial(40);
        fact60 = factorial(60);
        fact80 = factorial(80);
        fact100 = factorial(100);

        if (facta > fact0 && facta <= fact20) {
            xk0 = pow(eps, 2);
        } else if (facta > fact20 && facta <= fact40) {
            xk0 = pow(eps, 4);
        } else if (facta > fact40 && facta <= fact60) {
            xk0 = pow(eps, 8);
        } else if (facta > fact60 && facta <= fact80) {
            xk0 = pow(eps, 11);
        } else if (facta > fact80 && facta <= fact100) {

            xk0 = pow(eps, 15);
        }
        while (condParada>TOL && i < MAXITER){
            xk0 = xk0 * (2-a*xk0);
            xk1 = xk0;
            xk1 = xk1 * (2-a*xk1);
            condParada = abs((xk1-xk0)/xk1);
        }

    }
    return xk0;
}

/**
 * Metodo que se encarga de realizar la operacion e^a.
 * @param a: exponente al cual se desea elevar e.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
float exp_t(double a) {
    int n = 0;
    float condiparada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condiparada > TOL && n < MAXITER){

        Sk0 =  (pow(a, n)) * varM1(factorial(n));
        Sk1 =  ((pow(a, n+1)) * varM1(factorial(n+1)));
        // sum+ Sk0+Sk1 - (sum+ Sk0))
        condiparada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;

    }
    return sum;
}

/**
 * Metodo que se encarga de calcular el seno de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 * Poner máximo hasta a = 15.
 */
double sin_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 =  pow(-1, n) * pow(a, (2 * n +1 )) * varM1(factorial((2 * n +1)));
        Sk1 = pow(-1, n+1) * pow(a, (2 * (n+1) +1 )) * varM1(factorial((2 * (n+1) +1)));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;
}

/**
 * Metodo que se encarga de calcular el coseno de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double cos_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 =  pow(-1, n) * pow(a, (2 * n)) * varM1(factorial((2 * n)));
        Sk1 = pow(-1, n+1) * pow(a, (2 * (n+1) )) * varM1(factorial((2 * (n+1))));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;
}

/**
 * Metodo que se encarga de calcular el tangente de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double tan_t(double a) {
    double seno, coseno, cosM1, resultado;
    seno = sin_t(a);
    coseno = cos_t(a);
    if (coseno < 0) {
        cout << "El resultado del coseno es negativo por lo tanto no se puede calcular la tangente mediante a^-1.\n";
    } else {
        cout << " ";
        cosM1 = varM1(coseno);
        resultado = seno * cosM1;
    }
    return resultado;
}

/**
 * Metodo que se encarga de calcular el logaritmo natural de un numero.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double ln_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 = (1* varM1(2*n+1)) * (pow((a - 1) *  varM1(a + 1), 2 * n));
        Sk1 = (1* varM1(2*(n+1)+1)) * (pow((a - 1) *  varM1(a + 1), 2 * (n+1)));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    sum = (2 * (a - 1) / (a + 1)) * sum;
    return sum;


}

/**
 * Metodo que se encarga de calcular el logaritmo natural de un numero.
 * @param x: exponente del logaritmo.
 * @param a: base del logaritmo.
 * @return resultado: solucion de obtener loga(x) a partir de logaritmos naturales.
 */
double log_t(double a, double x) {
    double lna=0, lnx=0, resultado=0;
    if (x > 0 && a > 0) {

        lnx = ln_t(x);  //??
        lna = ln_t(a);
        lnx = ln_t(x);
        resultado = lnx * varM1(lna);
    } else {
        cout << "La base y el exponente deben ser numeros positivos. \n";
    }
    return resultado;
}

/**
 * Metodo que se encarga de elevar un numero 'a' a un exponente 'x'.
 * @param x: exponente.
 * @param a: numero a elevar.
 * @return: resultado de la evauacion
 */
double power_t(double a, double x) {
    double aa= ln_t(a);
    return exp_t(x * ln_t(a));
}

/**
* Metodo que se encarga de calcular el seno hiperbolico de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double sinh_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 =  pow(a, (2 * n +1 )) * varM1(factorial((2 * n +1)));
        Sk1 = pow(a, (2 * (n+1) +1 )) * varM1(factorial((2 * (n+1) +1)));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;
}

/**
 * Metodo que se encarga de calcular el coseno hiperbolico de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double cosh_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 = pow(a, (2 * n)) * varM1(factorial((2 * n)));
        Sk1 = pow(a, (2 * (n+1) )) * varM1(factorial((2 * (n+1))));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;
}

/**
 * Metodo que se encarga de calcular el tangente hiperbolico de un numero a.
 * @param a: numero a evaluar.
 * @return Sk0: resultado de realizar la operacion mediante sumatoria.
 */
double tanh_t(double a) {
    return sinh_t(a) * varM1(cosh_t(a));
}

/**
 * Metodo que se encarga de calcular la raiz cuadradda de un numero a.
 * @param a: numero a determinar la raiz cuadrada.
 * @return xk: valor aproximado de la raiz utilizando el metodo de Newton-Raphson.
 */
double sqrt_t(double a) {
    double condParada, x0 = 1, xk;

    if (a < 0) {
        cout << "No es posible calcular la raiz cuadrada de un numero negativo.";
    } else if (a == 0) {
        xk = 0;
    } else {
        do {
            xk = x0 - (pow(x0, 2) - a) * varM1(2 * x0);
            condParada = abs((xk - x0) * varM1(xk));
            x0 = xk;
        } while (condParada > TOL);
    }
    return xk;
}

/**
 * Metodo que se encarga de calcular la raiz 'a' de un numero 'x'.
 * @param x: numero a determinar la raiz.
 * @param a: exponente de la raiz.
 * @return xk: valor aproximado de la raiz utilizando el metodo de Newton-Raphson.
 */
double root_t(double x, double a) {
    double condParada, x0, xk;
    x0 = a / 2;

    if (x == 0) {
        return 0;
    } else {
        do {
            xk = x0 - (pow(x0, a) - x) * varM1(a * (pow(x0, a - 1)));
            condParada = abs((xk - x0) * varM1(xk));
            x0 = xk;
        } while (condParada > TOL);
    }
    return xk;
}

/**
 *
 * @param a
 * @return
 */
double asin_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 = (factorial(2 * n) * varM1((pow(4, n) * pow(factorial(n), 2) * (2 * n + 1)))) * pow(a, 2 * n + 1);
        Sk1 = (factorial(2 * (n+1)) * varM1((pow(4, n+1) * pow(factorial(n+1), 2) * (2 * (n+1) + 1)))) * pow(a, 2 * (n+1) + 1);
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;
}

/**
 *
 * @param a
 * @return
 */
double atan_t(double a) {
    int n = 0;
    double condParada=1, Sk1 = 0, Sk0 = 0,sum=0;

    while (condParada > TOL && n < MAXITER){
        Sk0 = pow(-1, n) * (pow(a, 2 * n + 1) *varM1(2 * n + 1));
        Sk1 = pow(-1, n+1) * (pow(a, 2 * (n+1) + 1) *varM1(2 * (n+1) + 1));
        condParada = abs(sum+ Sk0+Sk1 - (sum+ Sk0));
        sum= sum+Sk0;
        n=n+1;
    }
    return sum;

}
#endif //FUNCIONESTRASCENDENTES_FUNTRAS_H