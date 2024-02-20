import re  # Importing the regular expression module 're'

def find_short(s):  # Defining a function named 'find_short' that takes a string 's' as input
    splitStrings = list(map(len, re.findall(r"[\w']+", s)))  # Finding all words in the string 's' using a regular expression pattern, then mapping the length of each word, and finally converting the result into a list
    l = min(splitStrings)  # Finding the minimum length among all the words in 'splitStrings'
    return l  # Returning the minimum length, which represents the length of the shortest word in the input string 's'

#Without re
def find_short(s):
    # Split the string into words using whitespace as the delimiter
    words = s.split()
    # Map the length of each word to a list
    word_lengths = list(map(len, words))
    # Find the minimum length among all the words
    shortest_length = min(word_lengths)
    return shortest_length
