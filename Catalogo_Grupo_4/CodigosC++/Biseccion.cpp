#include<iostream>
#include<cmath>

using namespace std;

double F(double x) {
    return exp(x) - x - 2;
}

double Biseccion(double a, double b, int MAXIT, double TOL) {
    int cont = 1;
    double x;
    double fx;
    
    while(cont < MAXIT) {
        x = (a + b)/ 2;
        fx = F(x);
        if(F(a) * fx < 0) {
            b = x;
        }
        if(F(b) * fx < 0) {
            a = x;
        }
        if(abs(fx) < TOL) {
            return x;
        }
        cont = cont + 1;
    }
    return x;
}

int main (int argc, char *argv[]) {
    cout<< Biseccion(0, 2, 100, 0.000001)<<endl;
    system("pause");
    return 0;
}