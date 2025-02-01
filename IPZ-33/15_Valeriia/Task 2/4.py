def prime_factors(n): 
    factors = []  # list for prime factors

    while n % 2 == 0:  # check if the number is even and divide by 2 while it's even
        factors.append(2)
        n //= 2
    
    divisor = 3
    while divisor * divisor <= n:  # check for odd numbers and divide by all odd numbers from 3 to sqrt(n)
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2
    
    if n > 1:
        factors.append(n)
    
    return factors

num = int(input("Число: "))

factors = prime_factors(num)

print(f"{num} =", ", ".join(map(str, factors)))  # Output the result separated by commas
