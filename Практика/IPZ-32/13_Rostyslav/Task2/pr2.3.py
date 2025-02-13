def eratosthenes_sieve(n):
    numbers = list(range(2, n + 1))

    p = 2

    while p * p <= n:

        for i in range(p * p, n + 1, p):
            if i in numbers:
                numbers.remove(i)

        for i in range(p + 1, n + 1):
            if i in numbers:
                p = i
                break

    return numbers

n = 1000
primes = eratosthenes_sieve(n)

print("Прості числа до", n, ":")
print(primes)