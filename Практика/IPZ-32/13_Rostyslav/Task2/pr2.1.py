def find_pythagorean_triples(n):
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)
            if c**2 == c_squared and c <= n:
                triples.append((a, b, c))
    return triples

# Example usage:
n = 10
pythagorean_triples = find_pythagorean_triples(n)
print(f"Pythagorean triples for n = {n}:")
for a, b, c in pythagorean_triples:
    print(f"({a}, {b}, {c})")