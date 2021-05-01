#include <iostream>
#include <armadillo>


using namespace std;
using namespace arma;


/**
 * @param A: matriz de coeficientes
 * @param b: vector de terminos independientes
 * @param MAXIT: cantidad de iteraciones maximas
 * @param TOL: tolerancia de la respuesta
 * @return tuple<vec, double>: vector solucion, error de la solucion 
 */

tuple<vec, double> pseudoinversas(mat A, vec b, int MAXIT, double TOL){

    int iter = 0;
    double err = TOL + 1;


    // Se definie el valor de alpha para el metodo iterativo de Schlutz
    int alpha = eig_sym(A*trans(A)).max();
    //Se genera la el vector inicial
    vec xk = (1/alpha)*trans(A);
    //matriz identidad
    vec I = eye(A.n_cols);

    //variable para la interacion
    vec xk1;
    
     while(iter < MAXIT) {
        xk1 = xk*(2*I-A*xk);
        xk = xk1;
        err = norm(A*xk*A-A,);

        if(err < TOL) {
            break;
        }
        else {
            iter = iter + 1;
        }
    }
    return make_tuple(xk, err);


}

/**
 * Ejemplo numerico
 */
int main() {
    tuple<vec, double> testJ = pseudoinversas("5 1 1; 1 5 1; 1 1 5", "7 7 7", 100, 0.000001);
    cout << "Aproximacion: \n" << get<0>(testJ) << endl;
    cout << "Error: " << get<1>(testJ) << endl;
    return 0;
}