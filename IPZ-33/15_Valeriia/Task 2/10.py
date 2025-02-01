from itertools import combinations_with_replacement

def is_magic_vector(vector): #Check if the sum of the vector equals its product
    return sum(vector) == prod(vector)

def prod(vector): #Calculate the product of all elements in the vector
    result = 1  # Initialize the product with 1
    for num in vector:  # Iterate through all numbers in the vector
        result *= num  # Multiply each number to get the final product
    return result

def find_magic_vectors(n): #Find all magic N-vectors.
    magic_vectors = []  # List to store all found magic vectors
    
    # Generate all non-decreasing sequences of length N with values from 1 to a reasonable limit
    limit = 2 * n  # Arbitrary limit to keep numbers within a reasonable range
    for combo in combinations_with_replacement(range(1, limit), n):  
        # Generate all possible non-decreasing sequences of length N
        if is_magic_vector(combo):  # Check if the sequence satisfies the magic condition
            magic_vectors.append(combo)  # If true, add it to the list
    
    return magic_vectors  # Return the list of magic vectors

# Get user input for N
n = int(input("Число N: "))

# Find all magic vectors for the given N
magic_vectors = find_magic_vectors(n)

# Print the found magic vectors
print("\nMagic Vectors:")
for vector in magic_vectors:
    print(vector)
