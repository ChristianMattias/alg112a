def hill_climbing(objective_function, initial_position, step_size=0.01, max_iterations=1000, tolerance=1e-6):
    current_position = initial_position

    for iteration in range(max_iterations):
        current_value = objective_function(current_position)

        new_position = current_position + step_size
        new_value = objective_function(new_position)

        if new_value > current_value:
            current_position = new_position

        if abs(new_value - current_value) < tolerance:
            break

    return current_position

def objective_function(x):
    return -(x - 3)**2

initial_position = 0.0
result = hill_climbing(objective_function, initial_position)

print("Local maximum found at x =", result)
