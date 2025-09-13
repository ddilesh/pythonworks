
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def get_middle_five(primes):
    return primes[3:8]


def get_every_second(primes):
    return primes[::2]


def get_last_three(primes):
    return primes[-3:]


def get_reversed(primes):
    return primes[::-1]


def get_descending(primes):
    return sorted(primes, reverse=True)

print("Original list:      ", prime_numbers)
print("a) Middle five:     ", get_middle_five(prime_numbers))
print("b) Every second:    ", get_every_second(prime_numbers))
print("c) Last three:      ", get_last_three(prime_numbers))
print("d) Reversed list:   ", get_reversed(prime_numbers))
print("e) Descending list: ", get_descending(prime_numbers))
