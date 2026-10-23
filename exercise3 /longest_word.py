"""
Longest Word Finder

This program reads a sentence from the user, finds the word(s) with
the most letters, and prints them along with their length.
If several words share the longest length, all of them are shown.
"""


def find_longest_words(sentence):
    """Return a list of the longest word(s) and their length."""
    words = sentence.split()
    max_length = 0
    longest = []

    for word in words:
        length = len(word)
        if length > max_length:
            max_length = length
            longest = [word]
        elif length == max_length:
            longest.append(word)

    return longest, max_length


def main():
    """Read a sentence and print the longest word(s)."""
    sentence = input()
    longest, max_length = find_longest_words(sentence)

    print("Longest word(s):")
    for word in longest:
        print(f"{word} ({max_length} letters)")


main()
