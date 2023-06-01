def fibonacci(n):
    a, b = 0, 1
    fib_list = [a, b]

    for _ in range(2, n):
        c = a + b
        fib_list.append(c)
        a, b = b, c

    return fib_list


n = int(input("Ingrese un número mayor a 1: "))

fibonacci_sequence = fibonacci(n)
print("La serie de Fibonacci hasta el número", n, "es:")
for i, num in enumerate(fibonacci_sequence, 1):
    print(f"{i}. {num}")
