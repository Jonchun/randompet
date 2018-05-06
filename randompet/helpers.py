import secrets
import string

"""
https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
"""
def random_string(N):
    return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

def decToAlpha(n, alphabet):
    b = len(alphabet)
    if n == 0:
        return [0]
    digits = []
    while n:
        digit = alphabet[int(n % b)]
        digits.append(digit)
        n //= b
    return ''.join(digits[::-1])