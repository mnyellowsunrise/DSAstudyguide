def roman_to_int(s):
    # Define a dictionary to map Roman symbols to their values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result
    result = 0
    
    # Iterate through the Roman numeral from left to right
    for i in range(len(s)):
        # Check if the current symbol is smaller than the next one
        if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            # If true, subtract the current symbol's value
            result -= roman_values[s[i]]
        else:
            # Otherwise, add the current symbol's value
            result += roman_values[s[i]]
    
    return result