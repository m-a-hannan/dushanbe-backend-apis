import random, decimal, string


def random_string_id(length):
    # letters = string.ascii_lowercase
    # return ''.join(random.choice(numbers) for i in range(length))

    numbers = str(random.randrange(1020, 8090))
    return ''.join(random.choice(numbers) for i in range(length))

