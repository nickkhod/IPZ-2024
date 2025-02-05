

def process_string(s: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_part = sorted([ch for ch in s if ch in vowels], reverse=True)
    consonant_part = sorted([ch for ch in s if ch.isalpha() and ch not in vowels], reverse=True)
    return ("".join(vowel_part), len(consonant_part) > 3, "".join(consonant_part))

user_input = input("Введіть рядок: ")
result = process_string(user_input)
print(result)