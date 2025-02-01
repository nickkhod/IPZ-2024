def sieve(limit):  # creating the list
    sieve = [True] * (limit + 1)  # mark all numbers as prime
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers 
    
    for start in range(2, int(limit**0.5) + 1):  # loop through each number starting from 2
        if sieve[start]:  
            for multiple in range(start*start, limit + 1, start):  # cross out all multiples from start*start to limit
                sieve[multiple] = False 

    return [num for num, is_prime in enumerate(sieve) if is_prime]  # create a list containing only prime numbers 

primes = sieve(1000)

print("Решет Ератосфена", primes)  # print the list of prime numbers
