import random
import string


def generate_password(length):
    letters = string.digits + string.ascii_letters + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


print(generate_password(32))
