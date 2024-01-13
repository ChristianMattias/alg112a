def find_fibonacci_with_digits(digits):
    fib_sequence = [0, 1]
    index = 1
    
    while len(str(fib_sequence[-1])) < digits:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        index += 1
    
    return index, fib_sequence[-1]

# Example: Find the first Fibonacci number with at least 4 digits
target_digits = 4 
index, fibonacci_number = find_fibonacci_with_digits(target_digits)
print(f"The first Fibonacci number with at least {target_digits} digits is at index {index}: {fibonacci_number}")
