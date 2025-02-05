import textwrap


#   <------TASK 1------>
def find_triples(n):
    """
        The find_triples function generates all triples (a, b, c) such that a^2 + b^2 = c and c <= n.
        :param n: The maximum value for c in the generated triples
        :return: A list of tuples (a, b, c) satisfying the condition a^2 + b^2 = c, where 1 <= a <= b <= n and c <= n
        """
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = a ** 2 + b ** 2
            if c <= n:
                triples.append((a, b, c))
    return triples


#   <------TASK 2------>
def pascal_triangle(n):
    """
       The pascal_triangle function generates Pascal's triangle up to the n-th row.
       :param n: The number of rows to generate in Pascal's triangle
       :return: A list of lists representing Pascal's triangle, where each inner list is a row of the triangle
       """
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle


#   <------TASK 3------>
def eratosfen_():
    """
        The eratosfen_ function attempts to implement the Sieve of Eratosthenes to find all prime numbers between 2 and 1000.
        - Inefficient list manipulation and indexing
        - Logical error when checking divisibility (index mismatch)
        - Potential for an out-of-range index during list operations
        :return: This function does not return a value but prints steps and operations during the algorithm
        """
    all_numbers = []
    numbers_to_remove = []
    number_sadist_ID = 0

    for i in range(2, 1001, 1):
        all_numbers.append(i)
    finished = False
    while finished == False:
        for y in range(number_sadist_ID + 1, len(all_numbers)):
            if y % all_numbers[number_sadist_ID] == 0:
                if len(all_numbers) > y:
                    numbers_to_remove.append(all_numbers[y])
        for u in range(0, len(numbers_to_remove)):
            all_numbers.remove(numbers_to_remove[u])

        if number_sadist_ID >= len(all_numbers):
            print("It is over")
            finished = True
        else:
            number_sadist_ID += 1
            print("Changing_number")
            numbers_to_remove = []


#   <------TASK 4------>
def prime_factors(n):
    """
        The prime_factors function finds the prime factors of a given integer n.
        :param n: An integer to factorize
        :return: A list of prime factors of n
        """
    factors = []
    divisor = 2
    while n >= divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


#   <------TASK 5------>
def palindroms():
    """
        The palindroms function finds all numbers between 0 and 99 whose squares are also palindromes.
        :return: A list of integers between 0 and 99 satisfying the palindromic square condition
        """
    palindromic_numbers = []
    for num in range(0, 100):
        mirror_check = ""
        a = num
        for i in range(len(str(a)) - 1, -1, -1):
            mirror_check += str(a)[i]
        if str(a) == mirror_check:
            mirror_check = ""
            a = a * a
            for i in range(len(str(a)) - 1, -1, -1):
                mirror_check += str(a)[i]
            if str(a) == mirror_check:
                palindromic_numbers.append(num)
    return palindromic_numbers


#   <------TASK 6------>
def number_to_words(n):
    """
       The number_to_words function converts an integer n (from 1 to 1000) into its Ukrainian text representation.
       :param n: An integer in the range from 1 to 1000
       :return: A string representing the number in Ukrainian words
       """
    ones = ["", "один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
    teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять",
             "сімнадцять", "вісімнадцять", "дев’ятнадцять"]
    tens = ["", "десять", "двадцять", "тридцять", "сорок", "п’ятдесят", "шістдесят", "сімдесят", "вісімдесят",
            "дев’яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п’ятсот", "шістсот", "сімсот", "вісімсот", "дев’ятсот"]

    if n == 1000:
        return "тисяча"

    result = []

    h = n // 100
    t = (n % 100) // 10
    o = n % 10

    if h:
        result.append(hundreds[h])

    if t == 1:
        result.append(teens[o])
    else:
        if t:
            result.append(tens[t])
        if o:
            result.append(ones[o])

    return " ".join(result)


#   <------TASK 7------>
def is_prime(num):
    """
        The is_prime function checks whether a given number is a prime number.
        :param num: The integer to check for primality
        :return: True if num is a prime number, False otherwise
        """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_twin_primes(n):
    """
        The find_twin_primes function finds twin prime pairs starting from n and up to 2 * n.
        Twin primes are pairs of prime numbers that differ by 2.
        :param n: The starting integer for the search
        :return: A list of tuples (p1, p2) where p1 and p2 are twin primes
        """
    twin_primes = []
    for num in range(n, 2 * n):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes


#   <------TASK 8------>
def format_text(text: str, n: int) -> str:
    """
        The format_text function reformats a block of text into lines of specified width.
        :param text: The input text to be formatted
        :param n: The maximum line width for each paragraph
        :return: A string with formatted paragraphs, each wrapped to the specified width
        """
    paragraphs = text.split("\n\n")
    formatted_paragraphs = ["\n".join(textwrap.wrap(par, width=n)) for par in paragraphs]
    return "\n\n".join(formatted_paragraphs)



def main():
    """
        The main function serves as an entry point for executing different tasks based on user selection.
        Available tasks:
        1. Find triples (a, b, c) where a^2 + b^2 = c and c <= n
        2. Generate Pascal's triangle up to n rows
        3. Execute a modified version of the Sieve of Eratosthenes for primes up to 1000
        4. Find prime factors of a given number n
        5. Find numbers whose squares are palindromic
        6. Convert an integer (1 ≤ n ≤ 1000) into its Ukrainian text representation
        7. Find twin primes starting from n and up to 2 * n
        8. Format a block of text into lines of specified width
        :return: None
        """
    choose = int(input(f'Choose a number of task: '))
    match choose:
        case 1:
            n = 50
            result = find_triples(n)
            print(result)
        case 2:
            n = 10
            triangle = pascal_triangle(n)
            for row in triangle:
                print(" ".join(map(str, row)))
        case 3:
            eratosfen_()
        case 4:
            n = 250
            factors = prime_factors(n)
            print(f"{n} = {', '.join(map(str, factors))}")
        case 5:
            print(palindroms())
        case 6:
            n = int(input("Введіть число (≤1000): "))
            if 1 <= n <= 1000:
                print(number_to_words(n))
            else:
                print("Число повинно бути від 1 до 1000!")
        case 7:
            n = 10
            print(find_twin_primes(n))
        case 8:
            text = """Привіт, як справи?.
            Привіт! В мене все добре, а в тебе?."""
            n = 60
            formatted_text = format_text(text, n)
            print(formatted_text)


if __name__ == '__main__':
    main()