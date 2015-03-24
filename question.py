import re

SCRABBLE_SCORES = { 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
                    'D': 2, 'G': 2,
                    'B': 3, 'C': 3, 'M': 3, 'P': 3,
                    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                    'K': 5,
                    'J': 8, 'X': 8,
                    'Q': 10, 'Z': 10}


def multiplication(groups):
    res = int(groups[0]) * int(groups[1])
    if len(groups) > 2:
        match = re.search(r'plus (\d+)', groups[2])
        if match:
            res += int(match.group(1))
    return res


def largest(groups):
    numbers = map(int, groups[0].split(', '))
    return max(numbers)


def square_cube(groups):
    numbers = map(int, groups[0].split(', '))
    res = []
    for n in numbers:
        if n in [i ** 6 for i in xrange(10)]:
            res.append(str(n))
    return ', '.join(res)


def primes(groups):
    numbers = map(int, groups[0].split(', '))
    primes = range(2, max(numbers) + 1)
    index = 0
    while index < len(primes):
        current = primes[index]
        for composite in range(current * current, max(numbers) + 1, current):
            if composite in primes:
                primes.remove(composite)
        index += 1
    return ', '.join(str(n) for n in numbers if n in primes)


def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def anagram(groups):
    candidates = groups[1].split(', ')
    for c in candidates:
        if sorted(c) == sorted(groups[0]):
            return c
    return ''


def scrabble(groups):
    return sum(SCRABBLE_SCORES[c.upper()] for c in groups[0])


QUESTIONS = (
    (r'.*: what is (\d+) plus (\d+)$',                               lambda groups: sum(map(int, groups))),
    (r'.*: what is (\d+) plus (\d+) plus (\d+)',                     lambda groups: sum(map(int, groups))),
    (r'.*: what is (\d+) plus (\d+) multiplied by (\d+)',            lambda groups: int(groups[0]) + int(groups[1]) * int(groups[2])),
    (r'.*: what is (\d+) multiplied by (\d+)$',                      lambda groups: int(groups[0]) * int(groups[1])),
    (r'.*: what is (\d+) multiplied by (\d+) plus (\d+)',            lambda groups: int(groups[0]) * int(groups[1]) + int(groups[2])),
    (r'.*: which of the following numbers is the largest: (.*)',     largest),
    (r'.*: which of the following numbers is both a square and a cube: (.*)', square_cube),
    (r'.*: which of the following numbers are primes: (.*)',         primes),
    (r'.*: what colour is a banana',                                 lambda groups: 'yellow'),
    (r'.*: who is the Prime Minister of Great Britain',              lambda groups: 'David Cameron'),
    (r'.*: which city is the Eiffel tower in',                       lambda groups: 'Paris'),
    (r'.*: who played James Bond in the film Dr No',                 lambda groups: 'Sean Connery'),
    (r'.*: what currency did Spain use before the Euro',             lambda groups: 'peseta'),
    (r'.*: what is the (\d+)(st|nd|th) number in the Fibonacci sequence', lambda groups: fib(int(groups[0]))),
    (r'.*: what is (\d+) minus (\d+)',                               lambda groups: int(groups[0]) - int(groups[1])),
    (r'.*: what is (\d+) to the power of (\d+)',                     lambda groups: int(groups[0]) ** int(groups[1])),
    (r'.*: which of the following is an anagram of "(\w+)": (.*)',   anagram),
    (r'.*: what is the english scrabble score of (\w+)',             scrabble)
)