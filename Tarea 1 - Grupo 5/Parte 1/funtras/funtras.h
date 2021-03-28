#include <cmath>
#include <iostream>
#include <stdlib.h>

using namespace std;
const double TOL = 0.00000001;
const double MAXITER = 2500;

double factorial(int num);
double varM1(double a);
float exp_t(double a);
double sin_t(double a);
double cos_t(double a);
double tan_t(double a);
double ln_t(double a);
double log_t(double a, double x);
double power_t(double a, double x);
double sinh_t(double a);
double cosh_t(double a);
double tanh_t(double a);
double sqrt_t(double a);
double root_t(double x, double a);
double asin_t(double a);
double atan_t(double a);
double pi_t();
double acos_t(double x);