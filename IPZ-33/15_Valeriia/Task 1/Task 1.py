def is_vowel(char):
    return char.lower() in "аоуеиіaeiou"  # Check if the character is a vowel

def analyze():  # Function to analyze the input string
    input_string = input()  # Get the input string from the user
    
    vowels_list = []  # List for vowel letters
    consonants_list = []  # List for consonant letters
    has_digits = False  # Variable to check if there are digits in the string
    
    for char in input_string:  # Iterate through each character in the input string
        if char.isdigit():  # Check if the character is a digit
            has_digits = True
        elif char.isalpha():  # Check if the character is a letter
            if is_vowel(char):  # If the character is a vowel, add it to the vowel list
                vowels_list.append(char)
            else:  # If the character is a consonant, add it to the consonant list
                consonants_list.append(char)
    
    vowels_list.sort()  # Sort vowel letters in alphabetical order
    consonants_list.sort()  # Sort consonant letters in alphabetical order
    
    return ("".join(vowels_list), has_digits, "".join(consonants_list))  # Return a tuple with three elements

result = analyze()
print(result)  # Call the function and print the result
