def solve_linear_equation(a, b):
    for x in range(-100, 101):
        if a*x + b == 0:
            return x

    return None 

a = 2
b = -6

solution = solve_linear_equation(a, b)

if solution is not None:
    print("Solution found: x =", solution)
else:
    print("No solution found.")
