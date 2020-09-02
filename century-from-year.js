// The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

function century(year) {
    if (year % 100 == 0) {
        return year/100;
    } else {
        return Math.floor(year/100) + 1;
    }
}