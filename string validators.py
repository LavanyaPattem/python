if __name__ == '__main__':
    s = input('enter a string:').strip()
    has_alnum = has_alpha = has_digit = has_lower = has_upper = False
    has_alnum = any(c.isalnum() for c in s)
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
