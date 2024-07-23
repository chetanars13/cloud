def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = 10
result = fibonacci(num)
print(f"The first {num} numbers in the Fibonacci sequence are: {result}")
