def get_count(sentence):
    # Initialize a variable to count the number of vowels
    vowelcount = 0
    # Create a list containing individual vowel characters
    vowellist = ["a", "e", "i", "o", "u"]
    # Iterate over each character in the sentence
    for char in sentence:
        # Check if the current character is a vowel by testing if it's in the vowellist
        if char in vowellist:
            # If the current character is a vowel, increment the vowel count
            vowelcount += 1
    # Return the total count of vowels in the sentence
    return vowelcount

###Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.


