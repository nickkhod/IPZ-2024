def is_palindrome(n):
    return str(n) == str(n)[::-1]

result = [n for n in range(1, 100) if is_palindrome(n) and is_palindrome(n**2)]

print("Паліндроми першої сотні, квадрати яких теж паліндроми:", result)
