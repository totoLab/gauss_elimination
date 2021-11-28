import math
from fractions import Fraction

def calc(x, error=0.0000001):
    n = int(math.floor(x))
    x -= n
    if x < error:
        return (n, 1)
    elif 1 - error < x:
        return (n+1, 1)

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            frac = Fraction(n * middle_d + middle_n, middle_d)
            if (frac.numerator // frac.denominator) == 0:
                return(f"{frac.numerator % frac.denominator}/{frac.denominator}")
            elif ((frac.numerator % frac.denominator)/frac.denominator) == 0/1:
                return(f"{frac.numerator // frac.denominator}")
            else:
                return(f"{frac.numerator // frac.denominator} "f"{frac.numerator % frac.denominator}/{frac.denominator}")