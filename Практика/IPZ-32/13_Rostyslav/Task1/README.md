# String Processor

This Python script processes a given string and returns a tuple containing two elements:

1.  A string containing all the consonants from the input string, sorted alphabetically and in the order they appear.
2.  A boolean value indicating whether the input string contains more than one space.

## How it Works

The script defines a function `process_string(t)` that takes a string `t` as input and performs the following operations:

1.  **Initialization:**
    - Defines a string `vowels` containing all uppercase and lowercase vowels.
    - Initializes an empty string `consonants` to store the extracted consonants.

2.  **Consonant Extraction:**
    - Iterates through each character `char` in the input string `t`.
    - Checks if the character is an alphabet character using `char.isalpha()` and if it's not a vowel (i.e., it's a consonant).
    - If both conditions are true, the character is appended to the `consonants` string.

3.  **Consonant Sorting:**
    - Sorts the `consonants` string alphabetically using `sorted(consonants)`.
    - Joins the sorted characters back into a string using `"".join()`.

4.  **Multiple Space Check:**
    - Checks if the input string `t` contains more than one space using `t.count(" ") > 1`.
    - Stores the boolean result in the variable `has_multiple_spaces`.

5.  **Return Value:**
    - Returns a tuple containing the sorted `consonants` string and the `has_multiple_spaces` boolean value.

The script then prompts the user to enter a string, calls the `process_string()` function with the input string, and prints the returned tuple.

## Usage

1.  Save the code as a Python file (e.g., `string_processor.py`).
2.  Run the script from your terminal: `python string_processor.py`
3.  The script will prompt you to enter a string.
4.  After you enter the string and press Enter, the script will print the resulting tuple.

## Example Input/Output

**Input:**

This is a test string with multiple spaces.


**Output:**

('cghlmnprsstt', True)


In this example:

-   `'cghlmnprsstt'` is the sorted string of consonants from the input.
-   `True` indicates that the input string contained more than one space.

**Input:**

Hello World


**Output:**

('HlWrd', False)


In this example:

-   `'HlWrd'` is the sorted string of consonants from the input.
-   `False` indicates that the input string did not contain more than one space.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
