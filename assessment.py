from collections import Counter

def calculate_rectangle_area(length: int or float, width: int or float) -> int or float:
    """
    Calculates the area of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float or int: The area of the rectangle.
        Returns 0 if either length or width is negative.

    Learning Outcomes: Functions, Basic error handling (simple conditional check).
    """
    pass



def sum_even_numbers(numbers_list: list)-> int:
    """
    Calculates the sum of all even numbers in a list of integers.

    Args:
        numbers_list (list of int): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
             Returns 0 if the list is empty or contains no even numbers.

    Learning Outcomes: Functions, Basic loops (for), Processing data (list iteration, conditional).
    """
    pass


def find_first_occurrence(data_list:list, target_value: any) -> int:
    """
    Finds the index of the first occurrence of a target value in a list.

    Args:
        data_list (list): A list of items.
        target_value: The value to search for.

    Returns:
        int: The index of the first occurrence of target_value in data_list.
             Returns -1 if the target_value is not found in the list.

    Learning Outcomes: Functions, Basic loops (for/while), Processing data (list search).
    """
    pass


def safe_string_to_int(input_string: str) -> int or None:
    """
    Tries to convert a string to an integer.
    If the string cannot be converted, it should return None.

    Args:
        input_string (str): The string to convert.

    Returns:
        int or None: The integer representation of the string, or None if conversion fails.

    Learning Outcomes: Functions, Basic error handling (try-except ValueError).
    """
    pass


def reverse_string_list_comprehension(text: str) -> str:
    """
    Reverses a given string using list comprehension and string join (or just slicing!).
    This is more of a Python idiom than a complex algorithm for this task.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Learning Outcomes: Functions, Processing data (strings, potentially list comprehension or slicing), Simple algorithms.
    """
    pass

def count_characters_above_threshold(text: str, threshold: int) -> int:
    """
    Counts how many characters in a string appear more times than a given threshold.
    The comparison should be case-insensitive (e.g., 'a' and 'A' are the same character).

    Args:
        text (str): The string to analyze.
        threshold (int): The minimum number of occurrences for a character to be counted.

    Returns:
        int: The number of unique characters that appear more than `threshold` times.
             Example: text="aabbc", threshold=1 -> returns 3 (a, b, c all appear > 1 if threshold=1; if threshold=2, returns 1 (only 'a' and 'b' if text="aaabbc"))
             Example: text="Hello World", threshold=1 -> should count 'h', 'e', 'l', 'o', 'w', 'r', 'd'. 'l' appears 3 times, 'o' 2 times.
                      If threshold = 1, unique chars > 1 are h,e,l,o, ,w,r,d (8)
                      If threshold = 2, unique chars > 2 are l (1)

    Learning Outcomes: Functions, Basic loops, Processing data (strings, dictionaries/counters), Simple algorithms.
    """
    pass