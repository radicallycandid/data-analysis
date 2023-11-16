# 1. Hello World Function
def hello_world() -> None:
    """
    Prints "Hello, World!" to the standard output.
    """
    print("Hello, World!")


# 2. Addition Function
def add_numbers(a: int | float, b: int | float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


# 3. Maximum of Any
def max_of_any(*args: int | float) -> float:
    if not all(isinstance(item, (int, float)) for item in args):
        raise TypeError("All arguments must be numbers")
    result = float("-inf")
    for item in args:
        result = item if item > result else result
    return result


# 4. Length of String
def string_length(s: str) -> int:
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


# 7. List Sum
def sum_list(lst):
    result = 0
    for item in lst:
        result += item
    return result


# 8. Unique Elements
def unique_elements(lst):
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
