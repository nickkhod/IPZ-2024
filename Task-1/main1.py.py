def process_string(string):
    vowels = set("aeiouy")
    line1, line3 = "", "" 
    line2 = sum(1 for char in string if char.lower().isalpha() and char.lower() not in vowels)

    for char in string:
        lower_char = char.lower()
        if lower_char in vowels:
            line1 += char
        elif lower_char.isalpha():
            line3 += char

    return f"({line1}, {line2}, {line3})"


if __name__ == "__main__":
    user_input = input("Enter the string: ")
    result = process_string(user_input)
    print(result)
