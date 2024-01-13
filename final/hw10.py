import numpy as np

def solve_polynomial(coefficients):
    #use numpy
    roots = np.roots(coefficients)
    return roots

#example x^3 - 6x^2 + 11x - 6 The coefficient of is [1, -6, 11, -6]
coefficients = [1, -6, 11, -6]
roots = solve_polynomial(coefficients)

print("Roots of the polynomial:", roots)