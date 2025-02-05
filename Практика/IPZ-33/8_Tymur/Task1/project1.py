def process_string(s: str):
    vowels = "aeiouAEIOU"
    vowel_part = sorted([char for char in s if char in vowels], reverse=True)
    consonant_part = sorted([char for char in s if char.isalpha() and char not in vowels], reverse=True)

    vowel_str = "".join(vowel_part)
    consonant_str = "".join(consonant_part)

    return (vowel_str, len(vowel_part) > 3 if len(vowel_part) > 3 else False, consonant_str)


input_string = input("Введіть рядок: ")
print(process_string(input_string))
