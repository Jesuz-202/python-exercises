"""Palindrome checker using a separate function."""


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    return text == text[::-1]


s = input()

if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
