import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
from sympy import sympify, Symbol, diff

def jacobiano(func, variables):
    if(func.size != variables.size):
        print("Debe digitar vectores de tamaños adecuados")
    else:
        n = func.size
        jacobiano = np.zeros((n, n))
        for i in range(n):
            func[i] = sympify(func[i])
            variables[i] = [Symbol(variables[i])]
            for j in range(n):
                jacobiano[i][j] = [diff(func[i], variables[j])]
        return jacobiano
        
        
    
