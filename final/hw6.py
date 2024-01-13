import numpy as np

def objective_function(x):
    return x**2 

def gradient(x):
    return 2 * x

def gradient_descent(objective_function, gradient, initial_position, learning_rate=0.1, max_iterations=1000, tolerance=1e-6):
    current_position = initial_position

    for iteration in range(max_iterations):

        grad = gradient(current_position)
        
        new_position = current_position - learning_rate * grad

        if np.linalg.norm(new_position - current_position) < tolerance:
            break

        current_position = new_position

    return current_position

initial_position = 3.0
result = gradient_descent(objective_function, gradient, initial_position)

print("Local minimum found at x =", result)