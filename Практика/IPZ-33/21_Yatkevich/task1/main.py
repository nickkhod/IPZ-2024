def process_string(s: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_part = sorted([ch for ch in s if ch in vowels], reverse=True)
    consonant_part = sorted(
        [ch for ch in s if ch.isalpha() and ch not in vowels], reverse=True
    )

    return ("".join(vowel_part), len(vowel_part), "".join(consonant_part))


if __name__ == "__main__":
    input_string = input("input the string to sort") or "abcdefg"
    result = process_string(input_string)
    print(result)
