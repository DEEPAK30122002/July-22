def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n_terms = int(input("Enter the number of Fibonacci terms: "))
print(fibonacci(n_terms))
