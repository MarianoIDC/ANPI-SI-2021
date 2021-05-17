#include <iostream>
#include <ginac/ginac.h>
#include <armadillo>
#include <cmath>

using namespace std;
using namespace GiNaC;
using namespace arma;

/**
 * @param xv: Un vector de cualquier tamano que corresponde al eje X del polinomio
 * @param k: La cantidad de puntos que se han evaluado en el polinomio
 * @return q: La funcion de Lagrange que se le suma al polinomio de interpolacion
 * */
ex Lk(vec xv, int k)
{
    //Se carga la variable simbolica
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    //Se definen las variables
    int m = xv.size();
    ex q = 1;
    for (int i = 0; i < m; i++)
    {
        if (i != k)
        {
            //Se realiza la multiplicatoria de la funcion de Lagrange
            q *= (x - xv(i)) / (xv(k) - xv(i));
        }
        else
        {
            continue;
        }
    }
    return q;
}

/**
 * @param xv: Un vector de cualquier tamano que corresponde al eje X del polinomio
 * @param yv: Un vector de cualquier tamano que corresponde al eje Y del polinomio
 * @return p: El polinomio de interpolacion del conjunto de puntos
 */
ex lagrange(vec xv, vec yv)
{
    //Se carga la variable simbolica
    symbol x("x");
    symtab table;
    table["x"] = x;
    parser reader(table);
    //Se definen las variables
    int m = xv.size();
    int n = m - 1;
    ex p = 0;
    for (int i = 0; i < n; i++)
    {
        //Se realiza la sumatoria del polinomio de interpolacion
        p += yv(i + 1) * Lk(xv, i + 1);
    }
    return simplify_indexed(expand(p));
}

int main()
{
    //Vectores x y y tomados como ejemplo
    vec xv = "-2 0 1";
    vec yv = "0 1 -1";
    //Se carga la funcion y se ejecuta el ejemplo
    ex pol_int = lagrange(xv, yv);
    cout << "Polinomio de interpolacion : " << pol_int << endl;
    return 0;
}
