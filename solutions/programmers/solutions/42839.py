import itertools

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    prime_numbers = set()
    for i in range(1, len(numbers) + 1):
        prime_numbers.update(
            set(
                filter(is_prime,
                       map(
                           lambda x: int("".join(x)),
                           itertools.permutations(numbers, i)
                       )
                )
            )
        )
    answer = len(prime_numbers)

    return answer
