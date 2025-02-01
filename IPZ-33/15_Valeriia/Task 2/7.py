def prime(num):  # function to check if a number is prime
    if num <= 1:  # numbers <=1 are not prime
        return False
    for i in range(2, int(num ** 0.5) + 1):  # check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True

def find_prime_pairs(n):  # find all prime numbers
    primes = [num for num in range(n, 2 * n + 1) if prime(num)]  # create a list of numbers in the given range, checking each for primality
    pairs = []  # create a list for prime pairs
    
    for i in range(len(primes) - 1):  # iterate through all collected prime numbers
        if primes[i + 1] - primes[i] == 2:  # check for twin primes
            pairs.append((primes[i], primes[i + 1]))
    
    return pairs

n = int(input("Число n: "))
pairs = find_prime_pairs(n)

print("Пари:")
for pair in pairs:
    print(pair)
