def solve_linear_equation_iterative(a, b, initial_guess=0, max_iterations=100, tolerance=1e-6):
    x = initial_guess

    for iteration in range(max_iterations):
        equation_value = a*x + b

        if abs(equation_value) < tolerance:
            return x

        x = x - equation_value / a

    return None  

a = 2
b = -6

solution = solve_linear_equation_iterative(a, b)

if solution is not None:
    print("Solution found: x =", solution)
else:
    print("No solution found.")
    
