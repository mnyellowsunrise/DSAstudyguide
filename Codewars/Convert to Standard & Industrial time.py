def to_industrial(time):
    # Check if the input is a string
    if isinstance(time, str):
        # If the input is a string, split it into hours and minutes
        hours, minutes = map(int, time.split(':'))
        # Convert the time to minutes
        time = hours * 60 + minutes
    # Convert the time to decimal hours by dividing by 60 and rounding to 2 decimal places
    decimal_hours = round(time / 60, 2)
    # Return the result
    return decimal_hours

def to_normal(time):
    # Extract the integer part of the time (hours)
    hours = int(time)
    # Calculate the minutes by subtracting the integer part of the time from the time and multiplying by 60,
    # then round to the nearest integer
    minutes = round((time - hours) * 60)
    # If minutes equals 60, increment hours by 1 and set minutes to 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # Return the result in the format "h:mm"
    return f"{hours}:{minutes:02d}"


### Write two functions, one that converts standard time to decimal time and one that converts decimal time to standard time.

    ###One hour has 100 minutes (or 10,000 seconds) in decimal time, yet its duration is the same as in standard time. Thus a decimal minute consists of 36 standard seconds, which is 1/100 of an hour.
    ###Working time is usually rounded to integer decimal minutes. Thus one standard minute equals 0.02 decimal hours, while two standard minutes equal 0.03 decimal hours and so on.
    ###The terms "normal time" and "standard time" are considered synonymous in this kata.
    ###to_industrial(time) should accept either the time in minutes as an integer or a string of the format "h:mm". Minutes will always consist of two digits in the tests (e.g., "0:05"); hours can have more. Return a float that represents decimal hours (e.g. 1.75 for 1h 45m). Round to a precision of two decimal digits - do not simply truncate!
    ###to_normal(time) should accept a float representing decimal time in hours. Return a string that represents standard time in the format "h:mm".
    ###There will be no seconds in the tests. We'll neglect them for the purpose of this kata.


###Flavor text (click to expand)
###Calculations with time units can be confusing, because we are used to calculating in the decimal system in every day use. An hour, however, consists of sixty minutes, which in turn consist of sixty seconds each.

###Examples:
###to_industrial(1) => 0.02
###to_industrial("1:45") => 1.75
###to_normal(0.33) => "0:20"
