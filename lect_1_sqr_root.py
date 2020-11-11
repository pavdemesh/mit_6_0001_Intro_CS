# # Start with guess equal to x
# If (guess * guess - x) exceeds the required precision
# Make a better guess: guess = (guess + x / guess) / 2

def rec_sqrt(x, guess, eps):
    """Returns sqr root of x with given precision eps; x and guess must be same values"""
    if (guess * guess - x) <= eps:
        return guess

    else:
        return rec_sqrt(x, (guess + x / guess) / 2, eps)


print(rec_sqrt(3, 3, 0.00001))
