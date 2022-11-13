import string
import random


def get_random_password() -> str:
    alphabet = string.ascii_lowercase+string.ascii_uppercase+string.digits
    password = random.sample(alphabet, 8)
    while len(password) != len(set(password)):
        password = random.sample(alphabet, 8)
    return password


print(get_random_password())
