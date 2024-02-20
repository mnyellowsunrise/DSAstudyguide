def flick_switch(lst):
    # Initialize an empty list to store the boolean values
    result = []
    # Initialize a boolean variable 'switch' to True
    switch = True
    # Iterate over each element in the input list 'lst'
    for x in lst:
        # Check if the current element is equal to "flick"
        if x == "flick":
            # If it is, toggle the boolean variable 'switch' using the 'not' operator
            switch = not switch
        # Append the current value of the boolean variable 'switch' to the 'result' list
        result.append(switch)
    # Return the list containing the boolean values
    return result