def get_gcd(x, y):
    """Calculate the greatest common divisor of two numbers."""
    print('in get_gcd; x, y:', x, y)
    if y > x:
        x, y = y, x

    r = x % y
    if r == 0:
        return y
    else:
        result = get_gcd(y, r)

    return result
        

gcd = get_gcd(100, 75)
print(gcd)
