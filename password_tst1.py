import random
from secrets import choice
from flask import Flask
import string

def generate_password (min_length= 8):
    password = ''
    for _ in range(min_length):
        next = random.choice(string.string.ascii_letters + string.digits)
        password +=next
    return password
print(generate_password())

