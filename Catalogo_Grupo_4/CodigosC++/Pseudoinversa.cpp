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
    mat xk = (1/alpha)*trans(A);
    //matriz identidad
    // vec I = eye(A.n_cols);

    mat I (A.n_cols, A.n_cols, fill::eye);
    //variable para la interacion
    mat xk1;
    
     while(iter < MAXIT) {
        xk1 = xk*(2*I-A*xk);
        xk = xk1;
        err = norm(A*xk*A-A, 2);

        if(err < TOL) {
            break;
        }
        else {
            iter = iter + 1;
        }
    }
    mat A_pseudo = xk;
    vec x = A_pseudo*b;

    return make_tuple(x, err);


}

/**
 * Ejemplo numerico
 */
int main() {

    // Mat <double> A = {{}, {}, {}};
    Col <double> b = {1, 4, 5,};
    tuple<vec, double> testP = pseudoinversas("1 2 -1; -3 1 5; 1 2 3", b, 100, 0.0001);
    cout << "Aproximacion: \n" << get<0>(testP) << endl;
    cout << "Error: " << get<1>(testP) << endl;
    return 0;
}