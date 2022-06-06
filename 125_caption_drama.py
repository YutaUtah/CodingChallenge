def hasSamePattern(string):
    divisors = []
    for i in range(1, len(string)):
        if len(string) % i == 0:
            divisors.append(i)

    for divisor in divisors:
        pattern = string[0:divisor]
        if string == pattern * (len(string) // divisor):
            return True
    return False

isSamePattern = hasSamePattern('abcabcabc')