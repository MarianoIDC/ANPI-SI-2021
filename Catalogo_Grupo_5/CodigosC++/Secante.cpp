#include <iostream>
#include <ginac/ginac.h>
#include "mgl2/mgl.h"
#include <vector>

using namespace std;
using namespace GiNaC;

/*Funcion para crear una grafica:
 * Entradas: Pares ordenados en x y y, vectores de las graficas
 * Salidas: Grafica de iteraciones vs error*/
void createGraph(double x1, double x2, double y1, double y2, vector<double> x, vector<double> y) {
    mglGraph graph;
    //Estas funciones convierten los vectores de la entrada en arreglos de datos de la grafica
    mglData xGraph(x);
    mglData yGraph(y);
    //Se diseña la grafica con los parametros
    graph.Title("Error vs Iteracion");
    graph.SetOrigin(0, 0);
    graph.SetRanges(x1, x2, y1, y2); //Limites de la grafica
    graph.Plot(xGraph, yGraph, "o!rgb"); //Valores que va a contener la grafica
    graph.Axis();
    graph.Grid();
    //Se exporta la grafica a un archivo PNG
    graph.WritePNG("Graph.png");
}

/*Metodo de la secante:
 * Entradas: Funcion a la que se le va a aplicar el metodo (express), primer valor inicial, segundo
   valor inicial, tolerancia y cantidad de iteraciones maximas
 * Salidas: Aproximacion de la solucion, error y cantidad de iteraciones realizadas*/
ex secante(string express, string firstValue, string secondValue, string tolerance, string iterations) {
    //Implementación del calculo simbolico
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    //Se traducen las entradas a variables de calculo simbolico
    ex function = reader(express);
    ex x0 = reader(firstValue);
    ex x1 = reader(secondValue);
    ex tol = reader(tolerance);
    ex iterMax = reader(iterations);
    //Se definen las variables de la iteracion, solucion y error necesarias
    int iter = 1;
    ex xk;
    ex error = tol + 1;
    //Vectores para la grafica
    vector<double> errors;
    vector<double> iters;
    //Funciones por evaluar
    ex f0 = evalf(subs(function, x == x0));
    ex f1 = evalf(subs(function, x == x1));
    while (iter < iterMax) {
        //Ecuacion del metodo de la secante
        xk = x1 - f1 * ((x1 - x0) / (f1 - f0));
        error = abs(xk - x1)/abs(xk); //Error de la solucion
        ex aux = evalf(error);
        //Se actualizan los valores
        x0 = x1;
        x1 = xk;
        iter++;
        //Los vectores de iteracion y error reciben valores
        double m = ex_to<numeric>(aux).to_double();
        errors.push_back(m);
        iters.push_back(iter);
        //Condicion de parada
        if (error <= tol) {
            break;
        }
    }
    cout << "Aproximacion: " << xk << endl;
    cout << "Iteraciones : " << iter << endl;
    cout << "Error : " << error << endl;
    //Se crea la grafica respectiva
    createGraph(0, iter + 1, -ex_to<numeric>(evalf(error)).to_double(), ex_to<numeric>(evalf(error)).to_double(), iters, errors);
    return xk;
}

int main() {
    //Se define la funcion por evaluar
    string express;
    cout << "Escriba la funcion: " << endl;
    cin >> express;
    //Se definen los valores iniciales
    string x0;
    cout << "Escriba el primer valor inicial: " << endl;
    cin >> x0;
    string x1;
    cout << "Escriba el segundo valor inicial: " << endl;
    cin >> x1;
    //Se define la tolerancia
    string tol;
    cout << "Escriba la tolerancia: " << endl;
    cin >> tol;
    //Se define el numero maximo de iteraciones
    string iterMax;
    cout << "Escriba el numero de iteraciones: " << endl;
    cin >> iterMax;
    //Metodo de la secante
    secante(express, x0, x1, tol, iterMax);
    return 0;
}
