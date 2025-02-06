def is_palindrome(n):
  return str(n) == str(n)[::-1]

def find_palindromic_squares():
  palindromic_squares = []
  for i in range(1, 100):
    if is_palindrome(i) and is_palindrome(i**2):
      palindromic_squares.append(i)
  return palindromic_squares

palindromic_squares = find_palindromic_squares()
print(palindromic_squares)