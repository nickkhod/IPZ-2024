def obs(input_string):

    vowels = "aeiouAEIOU"
    vowel_part = ''.join(sorted([char for char in input_string if char in vowels], reverse=True))

    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_list = [char for char in input_string if char in consonants]
    consonant_part = ''.join(sorted(consonant_list, reverse=True))

    has_enough_consonants = len(consonant_list) >= 4

    result = (vowel_part, has_enough_consonants, consonant_part)
    return result

inp = input(" ")
print(obs(inp))