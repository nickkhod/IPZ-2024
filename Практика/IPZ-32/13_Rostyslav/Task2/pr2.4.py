def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

num = 250
factors = prime_factorization(num)
print(f"{num} = {', '.join(map(str, factors))}")

num = 12345
factors = prime_factorization(num)
print(f"{num} = {', '.join(map(str, factors))}")