def palindrome(num):  # function declaration to check if a number is a palindrome
    return str(num) == str(num)[::-1]  # compare the original string and its reversed version

result = []  # list for storing numbers
for i in range(1, 100):  # iterate through numbers from 1 to 100
    if palindrome(i) and palindrome(i ** 2):  # check if the number and its square are palindromes
        result.append(i)

print("Результат", result)  # Output the result
