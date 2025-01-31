def prime_factorization(n):
    factors = []
    for d in [2] + list(range(3, int(n**0.5) + 1, 2)):
        while n % d == 0:
            factors.append(d)
            n //= d
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    num = int(input("Введіть число: "))
    print(f"{num} = {', '.join(map(str, prime_factorization(num)))}")
