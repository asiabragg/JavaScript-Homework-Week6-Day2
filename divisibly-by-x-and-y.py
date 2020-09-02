# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits:

# Steps
# 1. Create a function that takes three parameters.
# 2. Parameters will be n, x and y.
# 3. Using moodulo operator check if n is divisible by the given x and y.

def div_x_y(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False

div_x_y(12, 7, 5)