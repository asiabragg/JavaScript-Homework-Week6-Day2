# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

# Steps
# 1. Create a Function that takes in a number for the year.
# 2. Check if the year is divisible by 100.
# 3. If the year is divisible by 100 divide the year by 100 and return.
# 4. Otherwise return year divided by 100 and add 1.

def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    else:
        return int(year/100) + 1