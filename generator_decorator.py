import time


def time_taken(func):
    def wrapper(n):  # Explicitly specify parameter 'n'
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print("Time taken:", end_time - start_time, "seconds")
        return result

    return wrapper


@time_taken
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Test the generator with a Fibonacci series of length 10
n = 10
print("Fibonacci series of length", n, ":", list(fibonacci_generator(n)))
