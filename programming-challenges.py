# 1. Hello World Function
def hello_world() -> None:
    """
    Prints "Hello, World!" to the standard output.
    """
    print("Hello, World!")


# 2. Addition Function
def add_numbers(a: int | float, b: int | float) -> float:
    """
    Add two numbers together.

    This function takes two arguments, both of which should be integers or floats,
    and returns their sum. If either of the arguments is not a number, a TypeError is raised.

    Args:
    a (int | float): The first number to be added.
    b (int | float): The second number to be added.

    Returns:
    float: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


# 3. Maximum of Any
def max_of_any(*args: int | float) -> float:
    """
    Find the maximum value among any number of numeric arguments.

    This function accepts a variable number of arguments, all expected to be integers or floats,
    and returns the largest one. If any argument is not a number, a TypeError is raised.

    Args:
    *args (int | float): A variable number of integers or floats to find the maximum from.

    Returns:
    float: The highest value among the provided arguments.

    Raises:
    TypeError: If any argument in args is not an integer or float.
    """
    if not all(isinstance(item, (int, float)) for item in args):
        raise TypeError("All arguments must be numbers")
    result = float("-inf")
    for item in args:
        result = item if item > result else result
    return result


# 4. Length of String
def string_length(s: str) -> int:
    """
    Calculate the length of a given string.

    This function determines the length of the provided string by counting its characters.
    It raises a TypeError if the input is not a string.

    Args:
    s (str): The string whose length is to be determined.

    Returns:
    int: The length of the string.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return sum(1 for _ in s)


# 5. Vowel Counter
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a given string.

    Args:
    s (str): The string to count vowels in.

    Returns:
    int: The number of vowels in the string.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    return sum(char in "aeiou" for char in s.lower())


# 6. Palindrome Checker
def is_palindrome(s):
    """
    Check if the given input is a palindrome.

    Args:
    s: The input to check. Expected to be a string.

    Returns:
    bool: True if s is a palindrome, False otherwise.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    return s == s[::-1]


help(is_palindrome)


# 7. List Sum
def sum_list(lst: list) -> float:
    """
    Calculate the sum of elements in a list.

    This function uses a generator expression to iterate over the list and sum its elements.
    It is designed to be memory-efficient for large lists.

    Args:
    lst (list): A list of numbers (integers or floats).

    Returns:
    float: The sum of the elements in the list.

    Raises:
    TypeError: If the input is not a list or if the list contains non-numeric elements.
    """
    if not all(isinstance(item, (int, float)) for item in lst):
        raise TypeError("All elements in the list must be numbers")

    return sum(item for item in lst)


# 8. Unique Elements
def unique_elements(lst: list) -> list:
    """
    Return a list of unique elements from the input list.

    This function iterates over each element in the input list and adds it to the result list
    only if it's not already present, thereby ensuring uniqueness.

    Args:
    lst (list): The list from which to extract unique elements.

    Returns:
    list: A list containing only the unique elements of the input list.

    Raises:
    TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# 9. Prime Number Checker
def is_prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result


# 10. Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
