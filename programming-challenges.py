# 1. Hello World Function
def hello_world() -> None:
    """
    Prints "Hello, World!" to the standard output.
    """
    print("Hello, World!")


# 2. Addition Function
def add_numbers(*args: int | float) -> float:
    """
    Add any number of numbers together.

    This function takes a variable number of arguments, all of which should be integers or floats,
    and returns their sum. If any of the arguments is not a number, a TypeError is raised.

    Args:
    *args (int | float): A variable number of integers or floats to be summed.

    Returns:
    float: The sum of all provided arguments.

    Raises:
    TypeError: If any argument is not an integer or float.
    """
    if not all(isinstance(item, (int, float)) for item in args):
        raise TypeError("All arguments must be numbers")

    total = 0.0
    for number in args:
        total += number
    return total


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
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    This function checks if the given number is prime by testing divisibility of odd numbers starting from 3
    up to the square root of n. Even numbers greater than 2 are automatically considered non-prime.

    Args:
    n (int): The number to be checked.

    Returns:
    bool: True if n is a prime number, False otherwise.

    Raises:
    ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


# 10. Fibonacci Sequence
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1. This function uses memoization to efficiently compute the nth number
    in the Fibonacci sequence.

    Args:
    n (int): The position in the Fibonacci sequence to compute.

    Returns:
    int: The nth Fibonacci number.

    Raises:
    ValueError: If the input is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    memo = {0: 0, 1: 1}  # Base cases

    def helper(x):
        if x not in memo:
            memo[x] = helper(x - 1) + helper(x - 2)
        return memo[x]

    return helper(n)
