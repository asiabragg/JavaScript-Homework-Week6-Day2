// Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits:

function div_x_y(n, x, y){
    if (n % x == 0 && n % y == 0) {
        return true;
    } else {
        return false;
    }
}

div_x_y(3, 3, 4)