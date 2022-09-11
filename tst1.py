import random
from flask import Flask
import string

def generate_password (min_length= 8):
    return ''.join(
        [
            random.choice(string.ascii_letters + string.digits)
            for _ in range(min_length)
                    ]
    )

print(generate_password())

