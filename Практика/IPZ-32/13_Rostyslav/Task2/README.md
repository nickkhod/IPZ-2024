# Palindromic Squares Finder

This Python script identifies and lists all palindromic numbers within the range of 1 to 100 (inclusive) whose squares are also palindromic.

## How it Works

The script defines two functions:

1.  **`is_palindrome(n)`:**
    - Takes an integer `n` as input.
    - Converts the integer to its string representation.
    - Checks if the string is equal to its reverse using string slicing `[::-1]`.
    - Returns `True` if the number is a palindrome, `False` otherwise.

2.  **`find_palindromic_squares()`:**
    - Initializes an empty list `palindromic_squares` to store the results.
    - Iterates through numbers from 1 to 100 (inclusive) using a `for` loop.
    - For each number `i`, it checks if both `i` and its square `i**2` are palindromes using the `is_palindrome()` function.
    - If both conditions are true, it appends `i` to the `palindromic_squares` list.
    - Finally, it returns the `palindromic_squares` list.

The script then calls the `find_palindromic_squares()` function to get the list of palindromic squares and prints the result to the console.

## Usage

1.  Save the code as a Python file (e.g., `palindromic_squares.py`).
2.  Run the script from your terminal: `python palindromic_squares.py`

The output will be a list of palindromic numbers within the specified range whose squares are also palindromic.

## Example Output

[1, 2, 3, 11, 22]

This output indicates that the numbers 1, 2, 3, 11, and 22 are palindromic, and their squares (1, 4, 9, 121, and 484, respectively) are also palindromic.

## Limitations

- The script currently searches for palindromic squares only within the range of 1 to 100.  You can modify the `range()` in the `find_palindromic_squares()` function to explore a different range.
- The script only considers positive integers.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
